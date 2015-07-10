#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arun/Documents/python/ooT/gr-FM_Switch/python
export PATH=/home/arun/Documents/python/ooT/gr-FM_Switch/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/arun/Documents/python/ooT/gr-FM_Switch/build/swig:$PYTHONPATH
/usr/bin/python2 /home/arun/Documents/python/ooT/gr-FM_Switch/python/qa_FM_stereo_mono_switch.py 
