#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arun/Documents/python/ooT/gr-FM_Switch/python
export PATH=/home/arun/Documents/python/ooT/gr-FM_Switch/python:$PATH
export LD_LIBRARY_PATH=/home/arun/Documents/python/ooT/gr-FM_Switch/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/arun/Documents/python/ooT/gr-FM_Switch/swig:$PYTHONPATH
/usr/bin/python2 /home/arun/Documents/python/ooT/gr-FM_Switch/python/qa_FM_switchCPP.py 
