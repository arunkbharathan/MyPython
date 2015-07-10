#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class FM_stereo_mono_switch(gr.sync_block):
    """
    docstring for block FM_stereo_mono_switch
    """
    def __init__(self, Threshold):
	self.Threshold = Threshold
        gr.sync_block.__init__(self,
            name="FM_stereo_mono_switch",
            in_sig = [numpy.float32,numpy.float32,numpy.float32,numpy.float32],
            out_sig = [numpy.float32,numpy.float32])


    def work(self, input_items, output_items):
        
        #from pudb import set_trace; set_trace()
	
	      
        input_items[1][input_items[0][:] > self.Threshold] = 0
        input_items[2][input_items[0][:] < self.Threshold] = 0
        input_items[3][input_items[0][:] < self.Threshold] = 0
        output_items[0][:] = input_items[1] + input_items[2]
        output_items[1][:] = input_items[1] + input_items[3]
        return len(output_items[0])

