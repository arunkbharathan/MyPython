import numpy
from gnuradio import gr

class square3_ff(gr.sync_block):
    " Squaring block " 
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name = "square3_ff",
            in_sig = [numpy.float32,numpy.float32,numpy.float32,numpy.float32], # Input signature: 1 float at a time
            out_sig = [numpy.float32,numpy.float32], # Output signature: 1 float at a time
        )

    def work(self, input_items, output_items):
        #from pudb import set_trace; set_trace()
        for index in xrange(len(input_items[0][:])):
            if input_items[0][index] != 1:
                output_items[0][index] = input_items[1][index]
                output_items[1][index] = input_items[1][index]
            else:
                output_items[0][index] = input_items[2][index]
                output_items[1][index] = input_items[3][index]
        return len(output_items[0])
