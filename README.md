# Azure-Kinect-Python

Python 3 bindings for the Azure Kinect SDK

## Changelog

- v1.1.0: Updated supported SDK and firmware versions to latest
- v1.0.0: Initial release

## Setup

Install the Kinect SDKs, update device firmware version if needed:

* [Sensor SDK v1.4.1](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/blob/develop/docs/usage.md#installation)
* [Body tracking SDK v1.0.1](https://docs.microsoft.com/en-us/azure/kinect-dk/body-sdk-download)
* Device firmware version must be at least 1.6.110079014 or higher.

If on Linux, ensure the relevant `k4a.so` and `k4abt.so` dynamic libraries are on your path.

## Feature support

Currently only body tracking is wrapped, but adding further wrappings should be easy and PRs would be appreciated!

## Examples

There is a very simple example you can run via:

```sh
py -3 example/simple_sample.py
```

## Demos

We are using it to develop an Azure Kinect plugin for [Blender](https://blender.org), which you can see a very early demo of here:

[![Azure Kinect for Blender](https://img.youtube.com/vi/jFVq6SdOdHw/0.jpg)](https://www.youtube.com/watch?v=jFVq6SdOdHw)

The plugin is available for early access and will be open-sourced soon, please email stephen@hexops.com to gain early access.

## Troubleshooting

### Do NOT use Python from the Windows Store

If you get the error:

```
[2021-01-18 14:05:28.307] [error] [t=6336] [K4ABT] D:\a\1\s\src\TrackerHost\TrackerHost.cpp (157): Create(). Find onnxruntime.dll at C:\Program Files\Azure Kinect Body Tracking SDK\tools\onnxruntime.dll but it doesn't load correctly!
```

It is because the Windows Store installs Python to a restricted user directory which cannot access external DLLs.
