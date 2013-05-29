# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_openmoc_cuda', [dirname(__file__)])
        except ImportError:
            import _openmoc_cuda
            return _openmoc_cuda
        if fp is not None:
            try:
                _mod = imp.load_module('_openmoc_cuda', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _openmoc_cuda = swig_import_helper()
    del swig_import_helper
else:
    import _openmoc_cuda
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class dev_material(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dev_material, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dev_material, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_uid"] = _openmoc_cuda.dev_material__uid_set
    __swig_getmethods__["_uid"] = _openmoc_cuda.dev_material__uid_get
    if _newclass:_uid = _swig_property(_openmoc_cuda.dev_material__uid_get, _openmoc_cuda.dev_material__uid_set)
    __swig_setmethods__["_id"] = _openmoc_cuda.dev_material__id_set
    __swig_getmethods__["_id"] = _openmoc_cuda.dev_material__id_get
    if _newclass:_id = _swig_property(_openmoc_cuda.dev_material__id_get, _openmoc_cuda.dev_material__id_set)
    __swig_setmethods__["_sigma_t"] = _openmoc_cuda.dev_material__sigma_t_set
    __swig_getmethods__["_sigma_t"] = _openmoc_cuda.dev_material__sigma_t_get
    if _newclass:_sigma_t = _swig_property(_openmoc_cuda.dev_material__sigma_t_get, _openmoc_cuda.dev_material__sigma_t_set)
    __swig_setmethods__["_sigma_a"] = _openmoc_cuda.dev_material__sigma_a_set
    __swig_getmethods__["_sigma_a"] = _openmoc_cuda.dev_material__sigma_a_get
    if _newclass:_sigma_a = _swig_property(_openmoc_cuda.dev_material__sigma_a_get, _openmoc_cuda.dev_material__sigma_a_set)
    __swig_setmethods__["_sigma_f"] = _openmoc_cuda.dev_material__sigma_f_set
    __swig_getmethods__["_sigma_f"] = _openmoc_cuda.dev_material__sigma_f_get
    if _newclass:_sigma_f = _swig_property(_openmoc_cuda.dev_material__sigma_f_get, _openmoc_cuda.dev_material__sigma_f_set)
    __swig_setmethods__["_nu_sigma_f"] = _openmoc_cuda.dev_material__nu_sigma_f_set
    __swig_getmethods__["_nu_sigma_f"] = _openmoc_cuda.dev_material__nu_sigma_f_get
    if _newclass:_nu_sigma_f = _swig_property(_openmoc_cuda.dev_material__nu_sigma_f_get, _openmoc_cuda.dev_material__nu_sigma_f_set)
    __swig_setmethods__["_chi"] = _openmoc_cuda.dev_material__chi_set
    __swig_getmethods__["_chi"] = _openmoc_cuda.dev_material__chi_get
    if _newclass:_chi = _swig_property(_openmoc_cuda.dev_material__chi_get, _openmoc_cuda.dev_material__chi_set)
    __swig_setmethods__["_sigma_s"] = _openmoc_cuda.dev_material__sigma_s_set
    __swig_getmethods__["_sigma_s"] = _openmoc_cuda.dev_material__sigma_s_get
    if _newclass:_sigma_s = _swig_property(_openmoc_cuda.dev_material__sigma_s_get, _openmoc_cuda.dev_material__sigma_s_set)
    def __init__(self): 
        this = _openmoc_cuda.new_dev_material()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openmoc_cuda.delete_dev_material
    __del__ = lambda self : None;
dev_material_swigregister = _openmoc_cuda.dev_material_swigregister
dev_material_swigregister(dev_material)

class dev_flatsourceregion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dev_flatsourceregion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dev_flatsourceregion, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_uid"] = _openmoc_cuda.dev_flatsourceregion__uid_set
    __swig_getmethods__["_uid"] = _openmoc_cuda.dev_flatsourceregion__uid_get
    if _newclass:_uid = _swig_property(_openmoc_cuda.dev_flatsourceregion__uid_get, _openmoc_cuda.dev_flatsourceregion__uid_set)
    __swig_setmethods__["_material_uid"] = _openmoc_cuda.dev_flatsourceregion__material_uid_set
    __swig_getmethods__["_material_uid"] = _openmoc_cuda.dev_flatsourceregion__material_uid_get
    if _newclass:_material_uid = _swig_property(_openmoc_cuda.dev_flatsourceregion__material_uid_get, _openmoc_cuda.dev_flatsourceregion__material_uid_set)
    __swig_setmethods__["_volume"] = _openmoc_cuda.dev_flatsourceregion__volume_set
    __swig_getmethods__["_volume"] = _openmoc_cuda.dev_flatsourceregion__volume_get
    if _newclass:_volume = _swig_property(_openmoc_cuda.dev_flatsourceregion__volume_get, _openmoc_cuda.dev_flatsourceregion__volume_set)
    def __init__(self): 
        this = _openmoc_cuda.new_dev_flatsourceregion()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openmoc_cuda.delete_dev_flatsourceregion
    __del__ = lambda self : None;
dev_flatsourceregion_swigregister = _openmoc_cuda.dev_flatsourceregion_swigregister
dev_flatsourceregion_swigregister(dev_flatsourceregion)


def cloneOnDevice(*args):
  return _openmoc_cuda.cloneOnDevice(*args)
cloneOnDevice = _openmoc_cuda.cloneOnDevice
class dev_segment(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dev_segment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dev_segment, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_length"] = _openmoc_cuda.dev_segment__length_set
    __swig_getmethods__["_length"] = _openmoc_cuda.dev_segment__length_get
    if _newclass:_length = _swig_property(_openmoc_cuda.dev_segment__length_get, _openmoc_cuda.dev_segment__length_set)
    __swig_setmethods__["_material_uid"] = _openmoc_cuda.dev_segment__material_uid_set
    __swig_getmethods__["_material_uid"] = _openmoc_cuda.dev_segment__material_uid_get
    if _newclass:_material_uid = _swig_property(_openmoc_cuda.dev_segment__material_uid_get, _openmoc_cuda.dev_segment__material_uid_set)
    __swig_setmethods__["_region_uid"] = _openmoc_cuda.dev_segment__region_uid_set
    __swig_getmethods__["_region_uid"] = _openmoc_cuda.dev_segment__region_uid_get
    if _newclass:_region_uid = _swig_property(_openmoc_cuda.dev_segment__region_uid_get, _openmoc_cuda.dev_segment__region_uid_set)
    def __init__(self): 
        this = _openmoc_cuda.new_dev_segment()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openmoc_cuda.delete_dev_segment
    __del__ = lambda self : None;
dev_segment_swigregister = _openmoc_cuda.dev_segment_swigregister
dev_segment_swigregister(dev_segment)

class dev_track(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dev_track, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dev_track, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_uid"] = _openmoc_cuda.dev_track__uid_set
    __swig_getmethods__["_uid"] = _openmoc_cuda.dev_track__uid_get
    if _newclass:_uid = _swig_property(_openmoc_cuda.dev_track__uid_get, _openmoc_cuda.dev_track__uid_set)
    __swig_setmethods__["_azim_angle_index"] = _openmoc_cuda.dev_track__azim_angle_index_set
    __swig_getmethods__["_azim_angle_index"] = _openmoc_cuda.dev_track__azim_angle_index_get
    if _newclass:_azim_angle_index = _swig_property(_openmoc_cuda.dev_track__azim_angle_index_get, _openmoc_cuda.dev_track__azim_angle_index_set)
    __swig_setmethods__["_segments"] = _openmoc_cuda.dev_track__segments_set
    __swig_getmethods__["_segments"] = _openmoc_cuda.dev_track__segments_get
    if _newclass:_segments = _swig_property(_openmoc_cuda.dev_track__segments_get, _openmoc_cuda.dev_track__segments_set)
    __swig_setmethods__["_num_segments"] = _openmoc_cuda.dev_track__num_segments_set
    __swig_getmethods__["_num_segments"] = _openmoc_cuda.dev_track__num_segments_get
    if _newclass:_num_segments = _swig_property(_openmoc_cuda.dev_track__num_segments_get, _openmoc_cuda.dev_track__num_segments_set)
    __swig_setmethods__["_track_in_i"] = _openmoc_cuda.dev_track__track_in_i_set
    __swig_getmethods__["_track_in_i"] = _openmoc_cuda.dev_track__track_in_i_get
    if _newclass:_track_in_i = _swig_property(_openmoc_cuda.dev_track__track_in_i_get, _openmoc_cuda.dev_track__track_in_i_set)
    __swig_setmethods__["_track_in_j"] = _openmoc_cuda.dev_track__track_in_j_set
    __swig_getmethods__["_track_in_j"] = _openmoc_cuda.dev_track__track_in_j_get
    if _newclass:_track_in_j = _swig_property(_openmoc_cuda.dev_track__track_in_j_get, _openmoc_cuda.dev_track__track_in_j_set)
    __swig_setmethods__["_track_out_i"] = _openmoc_cuda.dev_track__track_out_i_set
    __swig_getmethods__["_track_out_i"] = _openmoc_cuda.dev_track__track_out_i_get
    if _newclass:_track_out_i = _swig_property(_openmoc_cuda.dev_track__track_out_i_get, _openmoc_cuda.dev_track__track_out_i_set)
    __swig_setmethods__["_track_out_j"] = _openmoc_cuda.dev_track__track_out_j_set
    __swig_getmethods__["_track_out_j"] = _openmoc_cuda.dev_track__track_out_j_get
    if _newclass:_track_out_j = _swig_property(_openmoc_cuda.dev_track__track_out_j_get, _openmoc_cuda.dev_track__track_out_j_set)
    __swig_setmethods__["_refl_in"] = _openmoc_cuda.dev_track__refl_in_set
    __swig_getmethods__["_refl_in"] = _openmoc_cuda.dev_track__refl_in_get
    if _newclass:_refl_in = _swig_property(_openmoc_cuda.dev_track__refl_in_get, _openmoc_cuda.dev_track__refl_in_set)
    __swig_setmethods__["_refl_out"] = _openmoc_cuda.dev_track__refl_out_set
    __swig_getmethods__["_refl_out"] = _openmoc_cuda.dev_track__refl_out_get
    if _newclass:_refl_out = _swig_property(_openmoc_cuda.dev_track__refl_out_get, _openmoc_cuda.dev_track__refl_out_set)
    __swig_setmethods__["_bc_in"] = _openmoc_cuda.dev_track__bc_in_set
    __swig_getmethods__["_bc_in"] = _openmoc_cuda.dev_track__bc_in_get
    if _newclass:_bc_in = _swig_property(_openmoc_cuda.dev_track__bc_in_get, _openmoc_cuda.dev_track__bc_in_set)
    __swig_setmethods__["_bc_out"] = _openmoc_cuda.dev_track__bc_out_set
    __swig_getmethods__["_bc_out"] = _openmoc_cuda.dev_track__bc_out_get
    if _newclass:_bc_out = _swig_property(_openmoc_cuda.dev_track__bc_out_get, _openmoc_cuda.dev_track__bc_out_set)
    def __init__(self): 
        this = _openmoc_cuda.new_dev_track()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _openmoc_cuda.delete_dev_track
    __del__ = lambda self : None;
dev_track_swigregister = _openmoc_cuda.dev_track_swigregister
dev_track_swigregister(dev_track)


def cloneTrack(*args, **kwargs):
  return _openmoc_cuda.cloneTrack(*args, **kwargs)
cloneTrack = _openmoc_cuda.cloneTrack
# This file is compatible with both classic and new-style classes.


