/* -*- c++ -*- */
/*
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "FM_switchCPP_impl.h"

namespace gr {
  namespace FM_Switch {

    FM_switchCPP::sptr
    FM_switchCPP::make(float threshold)
    {
      return gnuradio::get_initial_sptr
        (new FM_switchCPP_impl(threshold));
    }

    /*
     * The private constructor
     */
    FM_switchCPP_impl::FM_switchCPP_impl(float threshold)
      : gr::sync_block("FM_switchCPP",
              gr::io_signature::make(4, 4, sizeof(float)),
              gr::io_signature::make(4, 4, sizeof(float)))
    {}

    /*
     * Our virtual destructor.
     */
    FM_switchCPP_impl::~FM_switchCPP_impl()
    {
    }

    int
    FM_switchCPP_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
        <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

        // Do <+signal processing+>

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace FM_Switch */
} /* namespace gr */

