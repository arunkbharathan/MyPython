#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arun/Documents/python/ooT/gr-FM_Switch/lib
export PATH=/home/arun/Documents/python/ooT/gr-FM_Switch/lib:$PATH
export LD_LIBRARY_PATH=/home/arun/Documents/python/ooT/gr-FM_Switch/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-FM_Switch 
