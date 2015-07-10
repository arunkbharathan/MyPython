/* -*- c++ -*- */

#define FM_SWITCH_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "FM_Switch_swig_doc.i"

%{
#include "FM_Switch/FM_switchCPP.h"
#include "FM_Switch/FM_switchCPP.h"
%}


%include "FM_Switch/FM_switchCPP.h"
GR_SWIG_BLOCK_MAGIC2(FM_Switch, FM_switchCPP);
%include "FM_Switch/FM_switchCPP.h"
GR_SWIG_BLOCK_MAGIC2(FM_Switch, FM_switchCPP);
