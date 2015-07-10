from gnuradio import gr, gr_unittest
from gnuradio import blocks

from square3_ff import square3_ff

class qa_square_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    # [...] Skipped the other test cases

    def test_003_square3_ff (self):
        src_data0 = (0,1,0,1,0)
        src_data1 = (-3.0, 4.0, -5.5, 2.0, 3.0)
        src_data2 = (2.0, 2.0, 2.0, 2.0, 2.0)
        src_data3 = (2.7, 2.7, 2.1, 2.3, 2.5)
        expected_result0 = (-3.0, 2.0, -5.5, 2.0, 3.0)
        expected_result1 = (-3.0, 2.7, -5.5, 2.3, 3.0)
        src0 = blocks.vector_source_f (src_data0)
        src1 = blocks.vector_source_f (src_data1)
        src2 = blocks.vector_source_f (src_data2)
        src3 = blocks.vector_source_f (src_data3)
        sqr = square3_ff ()
        dst0 = blocks.vector_sink_f ()
        dst1 = blocks.vector_sink_f ()
        self.tb.connect (src0, (sqr,0))
        self.tb.connect (src1,(sqr,1))
        self.tb.connect (src2,(sqr,2))
        self.tb.connect (src3,(sqr,3))
        self.tb.connect ((sqr,0), dst0)
        self.tb.connect ((sqr,1), dst1)
        self.tb.run ()
        result_data0 = dst0.data ()
        result_data1 = dst1.data ()
        from pudb import set_trace; set_trace()
        self.assertFloatTuplesAlmostEqual (expected_result0, result_data0, 6)
        self.assertFloatTuplesAlmostEqual (expected_result1, result_data1, 6)

if __name__ == '__main__':
    gr_unittest.main ()

