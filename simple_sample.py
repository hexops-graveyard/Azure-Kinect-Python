
"""
This is a python port of the simple-sample project from.
    https://github.com/microsoft/Azure-Kinect-Samples/blob/bf2f8cf95d969dcc7842c4c450052fe5a943c756/body-tracking-samples/simple_sample/main.c
"""

import traceback
import sys
import ctypes

import pyk4a

def VERIFY(result, error):
    if result != pyk4a.k4a_result_t.K4A_RESULT_SUCCEEDED:
        print(error)
        traceback.print_stack()
        sys.exit(1)

if __name__ == "__main__":
    device_config = pyk4a.K4A_DEVICE_CONFIG_INIT_DISABLE_ALL
    device_config.depth_mode = pyk4a.k4a_depth_mode_t.K4A_DEPTH_MODE_NFOV_UNBINNED

    device = pyk4a.k4a_device_t()
    VERIFY(pyk4a.k4a_device_open(0, ctypes.byref(device)), "Open K4A Device failed!")
    print("Didn't crash!")