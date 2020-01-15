import ctypes
import enum
import sys

from .pyk4a import k4a_float3_t, k4a_result_t, k4a_wait_result_t, k4a_calibration_t, k4a_capture_t, k4a_image_t
from .enumstruct import StructureWithEnums, CtypeIntEnum

try:
    _k4abt = ctypes.CDLL('k4abt.dll')
except:
    try:
        _k4abt = ctypes.CDLL('k4abt.so')
    except:
        print("Failed to load library")
        sys.exit(1)

# K4A_DECLARE_HANDLE(k4abt_tracker_t);
class _handle_k4abt_tracker_t(StructureWithEnums):
     _fields_= [
        ("_rsvd", ctypes.c_size_t),
    ]
k4abt_tracker_t = ctypes.POINTER(_handle_k4abt_tracker_t)

# K4A_DECLARE_HANDLE(k4abt_frame_t);
class _handle_k4abt_frame_t(StructureWithEnums):
     _fields_= [
        ("_rsvd", ctypes.c_size_t),
    ]
k4abt_frame_t = ctypes.POINTER(_handle_k4abt_frame_t)

class k4abt_joint_id_t(CtypeIntEnum):
    K4ABT_JOINT_PELVIS = 0,
    K4ABT_JOINT_SPINE_NAVEL = 1,
    K4ABT_JOINT_SPINE_CHEST = 2,
    K4ABT_JOINT_NECK = 3,
    K4ABT_JOINT_CLAVICLE_LEFT = 4,
    K4ABT_JOINT_SHOULDER_LEFT = 5,
    K4ABT_JOINT_ELBOW_LEFT = 6,
    K4ABT_JOINT_WRIST_LEFT = 7,
    K4ABT_JOINT_HAND_LEFT = 8,
    K4ABT_JOINT_HANDTIP_LEFT = 9,
    K4ABT_JOINT_THUMB_LEFT = 10,
    K4ABT_JOINT_CLAVICLE_RIGHT = 11,
    K4ABT_JOINT_SHOULDER_RIGHT = 12,
    K4ABT_JOINT_ELBOW_RIGHT = 13,
    K4ABT_JOINT_WRIST_RIGHT = 14,
    K4ABT_JOINT_HAND_RIGHT = 15,
    K4ABT_JOINT_HANDTIP_RIGHT = 16,
    K4ABT_JOINT_THUMB_RIGHT = 17,
    K4ABT_JOINT_HIP_LEFT = 18,
    K4ABT_JOINT_KNEE_LEFT = 19,
    K4ABT_JOINT_ANKLE_LEFT = 20,
    K4ABT_JOINT_FOOT_LEFT = 21,
    K4ABT_JOINT_HIP_RIGHT = 22,
    K4ABT_JOINT_KNEE_RIGHT = 23,
    K4ABT_JOINT_ANKLE_RIGHT = 24,
    K4ABT_JOINT_FOOT_RIGHT = 25,
    K4ABT_JOINT_HEAD = 26,
    K4ABT_JOINT_NOSE = 27,
    K4ABT_JOINT_EYE_LEFT = 28,
    K4ABT_JOINT_EAR_LEFT = 29,
    K4ABT_JOINT_EYE_RIGHT = 30,
    K4ABT_JOINT_EAR_RIGHT = 31,
    K4ABT_JOINT_COUNT = 32

class k4abt_sensor_orientation_t(CtypeIntEnum):
    K4ABT_SENSOR_ORIENTATION_DEFAULT = 0,
    K4ABT_SENSOR_ORIENTATION_CLOCKWISE90 = 1,
    K4ABT_SENSOR_ORIENTATION_COUNTERCLOCKWISE90 = 2,
    K4ABT_SENSOR_ORIENTATION_FLIP180 = 3,
    
class k4abt_tracker_processing_mode_t(CtypeIntEnum):
    K4ABT_TRACKER_PROCESSING_MODE_GPU = 0,
    K4ABT_TRACKER_PROCESSING_MODE_CPU = 1,

class _k4abt_tracker_configuration_t(StructureWithEnums):
    _fields_= [
        ("sensor_orientation", ctypes.c_int),
        ("processing_mode", ctypes.c_int),
        ("gpu_device_id", ctypes.c_int32),
    ]
    _map = {
        "sensor_orientation", k4abt_sensor_orientation_t,
        "processing_mode", k4abt_tracker_processing_mode_t,
    }
k4abt_tracker_configuration_t = _k4abt_tracker_configuration_t

class _wxyz(StructureWithEnums):
    _fields_= [
        ("w", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
    ]

class k4a_quaternion_t(ctypes.Union):
   _fields_= [
        ("wxyz", _wxyz),
        ("v", ctypes.c_float * 4)
    ]

class k4abt_joint_confidence_level_t(CtypeIntEnum):
    K4ABT_JOINT_CONFIDENCE_NONE = 0,
    K4ABT_JOINT_CONFIDENCE_LOW = 1,
    K4ABT_JOINT_CONFIDENCE_MEDIUM = 2,
    K4ABT_JOINT_CONFIDENCE_HIGH = 3,
    K4ABT_JOINT_CONFIDENCE_LEVELS_COUNT = 4,


class _k4abt_joint_t(StructureWithEnums):
    _fields_= [
        ("position", k4a_float3_t),
        ("orientation", k4a_quaternion_t),
        ("confidence_level", ctypes.c_int),
    ]
    _map = {
        "confidence_level", k4abt_joint_confidence_level_t,
    }
k4abt_joint_t = _k4abt_joint_t

class k4abt_skeleton_t(StructureWithEnums):
    _fields_= [
        ("joints", _k4abt_joint_t * k4abt_joint_id_t.K4ABT_JOINT_COUNT),
    ]

class k4abt_body_t(StructureWithEnums):
    _fields_= [
        ("id", ctypes.c_uint32),
        ("skeleton", k4abt_skeleton_t),
    ]

K4ABT_BODY_INDEX_MAP_BACKGROUND = 255
K4ABT_INVALID_BODY_ID = 0xFFFFFFFF
K4ABT_DEFAULT_TRACKER_SMOOTHING_FACTOR = 0.0

# TODO(Andoryuuta): Not sure if a single instance of the default config like this will work, might need a creation function.
K4ABT_TRACKER_CONFIG_DEFAULT = k4abt_tracker_configuration_t()
K4ABT_TRACKER_CONFIG_DEFAULT.sensor_orientation = k4abt_sensor_orientation_t.K4ABT_SENSOR_ORIENTATION_DEFAULT
K4ABT_TRACKER_CONFIG_DEFAULT.processing_mode = k4abt_tracker_processing_mode_t.K4ABT_TRACKER_PROCESSING_MODE_GPU
K4ABT_TRACKER_CONFIG_DEFAULT.gpu_device_id = 0

# Functions
k4abt_tracker_create = _k4abt.k4abt_tracker_create
k4abt_tracker_create.restype=k4a_result_t
k4abt_tracker_create.argtypes=(ctypes.POINTER(k4a_calibration_t), k4abt_tracker_configuration_t, ctypes.POINTER(k4abt_tracker_t))

k4abt_tracker_destroy = _k4abt.k4abt_tracker_destroy
k4abt_tracker_destroy.argtypes=(k4abt_tracker_t,)

k4abt_tracker_set_temporal_smoothing = _k4abt.k4abt_tracker_set_temporal_smoothing
k4abt_tracker_set_temporal_smoothing.argtypes=(k4abt_tracker_t, ctypes.c_float)

k4abt_tracker_enqueue_capture = _k4abt.k4abt_tracker_enqueue_capture
k4abt_tracker_enqueue_capture.restype=k4a_wait_result_t
k4abt_tracker_enqueue_capture.argtypes=(k4abt_tracker_t, k4a_capture_t, ctypes.c_int32)

k4abt_tracker_pop_result = _k4abt.k4abt_tracker_pop_result
k4abt_tracker_pop_result.restype=k4a_wait_result_t
k4abt_tracker_pop_result.argtypes=(k4abt_tracker_t, ctypes.POINTER(k4abt_frame_t), ctypes.c_int32)

k4abt_tracker_shutdown = _k4abt.k4abt_tracker_shutdown
k4abt_tracker_shutdown.argtypes=(k4abt_tracker_t,)

k4abt_frame_release = _k4abt.k4abt_frame_release
k4abt_frame_release.argtypes=(k4abt_frame_t,)

k4abt_frame_reference = _k4abt.k4abt_frame_reference
k4abt_frame_reference.argtypes=(k4abt_frame_t,)

k4abt_frame_get_num_bodies = _k4abt.k4abt_frame_get_num_bodies
k4abt_frame_get_num_bodies.restype=ctypes.c_uint32
k4abt_frame_get_num_bodies.argtypes=(k4abt_frame_t,)

k4abt_frame_get_body_skeleton = _k4abt.k4abt_frame_get_body_skeleton
k4abt_frame_get_body_skeleton.restype=k4a_result_t
k4abt_frame_get_body_skeleton.argtypes=(k4abt_frame_t, ctypes.c_uint32, ctypes.POINTER(k4abt_skeleton_t))

k4abt_frame_get_body_id = _k4abt.k4abt_frame_get_body_id
k4abt_frame_get_body_id.restype=ctypes.c_uint32
k4abt_frame_get_body_id.argtypes=(k4abt_frame_t, ctypes.c_uint32)

k4abt_frame_get_device_timestamp_usec = _k4abt.k4abt_frame_get_device_timestamp_usec
k4abt_frame_get_device_timestamp_usec.restype=ctypes.c_uint64
k4abt_frame_get_device_timestamp_usec.argtypes=(k4abt_frame_t,)

k4abt_frame_get_body_index_map = _k4abt.k4abt_frame_get_body_index_map
k4abt_frame_get_body_index_map.restype=k4a_image_t
k4abt_frame_get_body_index_map.argtypes=(k4abt_frame_t,)

k4abt_frame_get_capture = _k4abt.k4abt_frame_get_capture
k4abt_frame_get_capture.restype=k4a_capture_t
k4abt_frame_get_capture.argtypes=(k4abt_frame_t,)

if __name__ == "__main__":
    print("Main called okay.")
