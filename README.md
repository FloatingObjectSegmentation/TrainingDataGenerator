# TrainingDataGenerator
A tool for generating point cloud data of objects scanned with various range scanners

## Dependencies

This tool is realized using the open source sensor simulation toolkit [Blensor](http://www.blensor.org/), based on the Blender 3D Software tool.
It uses and extends its own version of Blender, which is stripped of Blender utilities that are not immediately relevant to the purpose of the program.

### Installing and using Blensor

- Tested with Ubuntu 18.04 LTS
- Download and decompress the Blensor binary found on this [link](https://blensor-downloads.hosted-secure.com/blensor_1.0.18-RC9_x64.tbz).
  - install ```numpy``` for ```python3``` using ```pip```
  - Fix the link to numpy in the following path within the Blensor installation directory
    - ```rm ./2.79/python/lib/python3.6/site-packages/numpy```
    - ```ln -s /usr/lib/python3/dist-packages/numpy/ ./2.79/python/lib/python3.6/site-packages/numpy```
        - /usr/lib/python3/dist-packages/numpy/ may not be the path to your installation of numpy. Search perhaps within /usr/lib/local if you installed it using pip.
  - ```sudo apt-get install libopenjpeg2 libjpeg62 libpng12-0```
    - These libraries have been removed from apt-get on Ubuntu 18.04 LTS, so you may need to install by downloading binaries from [packages.ubuntu.com](packages.ubuntu.com)
  - Install OpenImageIO.so, by searching for it online
  - Install libjemalloc.so.1, by searching for it online
Start the tool, by writin ```./blender``` at the root of the directory.
