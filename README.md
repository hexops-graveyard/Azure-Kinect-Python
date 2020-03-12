# Azure-Kinect-Python

Python 3 bindings for the Azure Kinect SDK

## Setup

https://docs.microsoft.com/en-us/azure/kinect-dk/sensor-sdk-download version 1.3.0
https://docs.microsoft.com/en-us/azure/kinect-dk/body-sdk-download version 0.9.5

Add the following to your path:

* `C:\Program Files\Azure Kinect SDK v1.3.0\sdk\windows-desktop\amd64\release\bin`

* `C:\Program Files\Azure Kinect Body Tracking SDK\sdk\windows-desktop\amd64\release\bin`


(Or relevant paths for your platform containing the the `k4a(.so|.dll)` and `k4abt(.so|.dll)` dynamic libraries)

## Feature support

Currently only body tracking is wrapped, but adding further wrappings should be easy and PRs would be appreciated!

## Demos

We are using it to develop an Azure Kinect plugin for [Blender](https://blender.org), which you can see a very early demo of here:

[![Azure Kinect for Blender](https://img.youtube.com/vi/jFVq6SdOdHw/0.jpg)](https://www.youtube.com/watch?v=jFVq6SdOdHw)

The plugin is not currently available publicly.
