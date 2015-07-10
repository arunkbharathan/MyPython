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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from FM_stereo_mono_switch import FM_stereo_mono_switch

class qa_FM_stereo_mono_switch (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data0 = (20,121,210,11,110)
        src_data1 = (-3.0, 4.0, -5.5, 2.0, 3.0)
        src_data2 = (2.0, 2.0, 2.0, 2.0, 2.0)
        src_data3 = (2.7, 2.7, 2.1, 2.3, 2.5)
        expected_result0 = (-3.0, 2.0, 2.0, 2.0, 2.0)
        expected_result1 = (-3.0, 2.7, 2.1, 2.0, 2.5)
        src0 = blocks.vector_source_f (src_data0)
        src1 = blocks.vector_source_f (src_data1)
        src2 = blocks.vector_source_f (src_data2)
        src3 = blocks.vector_source_f (src_data3)
        switch = FM_stereo_mono_switch (75.0)
        dst0 = blocks.vector_sink_f ()
        dst1 = blocks.vector_sink_f ()
        self.tb.connect (src0, (switch,0))
        self.tb.connect (src1,(switch,1))
        self.tb.connect (src2,(switch,2))
        self.tb.connect (src3,(switch,3))
        self.tb.connect ((switch,0), dst0)
        self.tb.connect ((switch,1), dst1)
        self.tb.run ()
        result_data0 = dst0.data ()
        result_data1 = dst1.data ()
        #from pudb import set_trace; set_trace()
        self.assertFloatTuplesAlmostEqual (expected_result0, result_data0, 6)
        self.assertFloatTuplesAlmostEqual (expected_result1, result_data1, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_FM_stereo_mono_switch, "qa_FM_stereo_mono_switch.xml")
