<?php
# check_informix - check_mk plugin to monitor IBM Informix databases
# Copyright (c) 2012 FuH Entwicklungsgesellschaft mbH, Umkirch, Germany. All rights reserved.
# Author: Philipp Hoefflin, 2012, hoefflin+cmk@fuh-e.de
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation in version 2.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 675 Mass Ave, Cambridge MA 02139, USA or see <http://www.gnu.org/licenses/>

$title = str_replace("_", " ", $servicedesc);


$opt[1] = "--vertical-label 'GB' -l0 --title \"$title\" ";
#
$def[1] =  "DEF:current=$RRDFILE[1]:$DS[1]:MAX " ;
$def[1] .= "DEF:used=$RRDFILE[2]:$DS[2]:MAX " ;
$def[1] .= "DEF:max=$RRDFILE[1]:$DS[1]:MAX " ;
$def[1] .= "CDEF:current_gb=current,1073741824.0,/ ";
$def[1] .= "CDEF:max_gb=max,1073741824.0,/ ";
$def[1] .= "CDEF:used_gb=used,1073741824.0,/ ";

$def[1] .= "AREA:max_gb#80c0ff:\"Maximum size\" " ;
$def[1] .= "LINE:max_gb#6080c0:\"\" " ;
$def[1] .= "GPRINT:max_gb:LAST:\"%2.2lfGB\" ";
$def[1] .= "AREA:current_gb#00ff80:\"Current size\" " ;
$def[1] .= "LINE:current_gb#008040:\"\" " ;
$def[1] .= "GPRINT:current_gb:LAST:\"%2.2lfGB\" ";
$def[1] .= "AREA:used_gb#f0b000:\"Used by user data\" " ;
$def[1] .= "LINE:used_gb#806000:\"\" " ;
$def[1] .= "GPRINT:used_gb:LAST:\"%2.2lfGB\" ";

?>
