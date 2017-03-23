#include "../../../src/CPUSolver.h"
#include "../../../src/CPULSSolver.h"
#include "../../../src/log.h"
#include "../../../src/Mesh.h"
#include <array>
#include <iostream>
#include "helper-code/group-structures.h"

int main(int argc,  char* argv[]) {

#ifdef MPIx
  MPI_Init(&argc, &argv);
  log_set_ranks(MPI_COMM_WORLD);
#endif

  /* Define geometry to load */
  //std::string file = "few-pins-reduced-ref-v2.geo";
  //std::string file = "full-assembly-final.geo";
  //std::string file = "beavrs-2D-v2-NULL-corr.geo";
  //std::string file = "beavrs-2D-v2.geo";
  //std::string file = "beavrs-2D-v3.geo"; //FIXME
  std::string file = "full-core-beavrs-new.geo";

  /* Define simulation parameters */
  #ifdef OPENMP
  int num_threads = omp_get_num_procs();
  #else
  int num_threads = 1;
  #endif
 
  double azim_spacing = 0.1;
  int num_azim = 8;
  double polar_spacing = 1.5;
  int num_polar = 6; //FIXME 6 / 2

  /*
  double azim_spacing = 0.1;
  int num_azim = 32;
  double polar_spacing = 5.0; // 1.0
  int num_polar = 6;
  */

  double tolerance = 1e-4;
  int max_iters = 30;

  /* Create CMFD lattice */
  Cmfd cmfd;
  cmfd.useAxialInterpolation(true);
  cmfd.setLatticeStructure(17*17, 17*17, 200); //FIXME 1 / 200
  cmfd.setKNearest(1);
  std::vector<std::vector<int> > cmfd_group_structure =
      get_group_structure(70, 8);
  cmfd.setGroupStructure(cmfd_group_structure);
  cmfd.setCMFDRelaxationFactor(0.5);
  cmfd.setSORRelaxationFactor(1.6);
  cmfd.useFluxLimiting(true);

  /* Load the geometry */
  log_printf(NORMAL, "Creating geometry...");
  Geometry geometry;
  geometry.loadFromFile(file);
  //geometry.manipulateXS(); // FIXME ON / OFF

  //FIXME
  int num_rad_discr = 96;
  int rad_discr_domains[96*2];
  int ind = 0;
  for (int i=0; i < 17; i++) {
    int offset = std::abs(8-i);
    if (offset == 8) {
      for (int j=0; j < 17; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
    }
    else if (offset == 7) {
      for (int j=0; j < 5; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
      for (int j=12; j < 17; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
    }
    else if (offset == 6) {
      for (int j=0; j < 3; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
      for (int j=14; j < 17; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
    }
    else if (offset == 5 || offset == 4) {
      for (int j=0; j < 2; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
      for (int j=15; j < 17; j++) {
        rad_discr_domains[2*ind] = i;
        rad_discr_domains[2*ind+1] = j;
        ind++;
      }
    }
    else if (offset < 4) {
      rad_discr_domains[2*ind] = i;
      rad_discr_domains[2*ind+1] = 0;
      ind++;
      rad_discr_domains[2*ind] = i;
      rad_discr_domains[2*ind+1] = 16;
      ind++;
    }
  }


  geometry.setCmfd(&cmfd); //FIXME OFF /ON
  log_printf(NORMAL, "Pitch = %8.6e", geometry.getMaxX() - geometry.getMinX());
  log_printf(NORMAL, "Height = %8.6e", geometry.getMaxZ() - geometry.getMinZ());
#ifdef MPIx
  geometry.setDomainDecomposition(17, 17, 4, MPI_COMM_WORLD); //FIXME 1/2
#else
  //geometry.setNumDomainModules(2,2,4);
#endif
  geometry.setOverlaidMesh(2.0, 17*17*3, 17*17*3, num_rad_discr, 
                           rad_discr_domains);
  geometry.initializeFlatSourceRegions();

  /* Create the track generator */
  log_printf(NORMAL, "Initializing the track generator...");
  TrackGenerator3D track_generator(&geometry, num_azim, num_polar, azim_spacing,
                                   polar_spacing);
  track_generator.setTrackGenerationMethod(MODULAR_RAY_TRACING);
  track_generator.setNumThreads(num_threads);
  track_generator.setSegmentFormation(OTF_STACKS);
  /*
  std::vector<FP_PRECISION> zones;
  zones.push_back(0.0);
  zones.push_back(20.0);
  zones.push_back(380.0);
  zones.push_back(400.0);
  track_generator.setSegmentationZones(zones);
    */
  track_generator.generateTracks();

  /* Run simulation */
  CPULSSolver solver(&track_generator); //FIXME LS / FS
  solver.setNumThreads(num_threads);
  solver.setVerboseIterationReport();
  solver.setConvergenceThreshold(tolerance);
  //solver.correctXS();
  solver.setCheckXSLogLevel(INFO);
  solver.computeEigenvalue(max_iters);
  solver.printTimerReport();

  Lattice mesh_lattice;
  Mesh mesh(&solver);
  mesh.createLattice(17*17, 17*17, 1);
  Vector3D rx_rates = mesh.getFormattedReactionRates(FISSION_RX);

  int my_rank = 0;
#ifdef MPIx
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
#endif
  if (my_rank == 0) {
    for (int k=0; k < rx_rates.at(0).at(0).size(); k++) {
      std::cout << " -------- z = " << k << " ----------" << std::endl;
      for (int j=0; j < rx_rates.at(0).size(); j++) {
        for (int i=0; i < rx_rates.size(); i++) {
          std::cout << rx_rates.at(i).at(j).at(k) << " ";
        }
        std::cout << std::endl;
      }
    }
  }

  log_printf(TITLE, "Finished");
#ifdef MPIx
  MPI_Finalize();
#endif
  return 0;
}
