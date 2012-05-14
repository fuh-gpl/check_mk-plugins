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
$opt[1] = "--vertical-label 'active sessions' -l0 -u $CRIT[1] --title \"$title\" ";

$def[1] = "DEF:sessions=$RRDFILE[1]:$DS[1]:MAX ";
$def[1] .= "AREA:sessions#00ff48: ";
$def[1] .= "LINE:sessions#008f38: ";
$def[1] .= "GPRINT:sessions:LAST:\"last\: %3.0lf\" ";
$def[1] .= "GPRINT:sessions:AVERAGE:\"avg\: %3.0lf\" ";
$def[1] .= "GPRINT:sessions:MAX:\"max\: %3.0lf\" ";
$def[1] .= "HRULE:$WARN[1]#ffcf00:\"Warning at $WARN[1]\" ";
$def[1] .= "HRULE:$CRIT[1]#ff0000:\"Critical at $CRIT[1]\" ";
?>
