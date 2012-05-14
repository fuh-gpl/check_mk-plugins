# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 
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

def perfometer_check_check_informix_sessions(row, check_command, perf_data):
    color = { 0: "#a4f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
    return "%d" % int(perf_data[0][1]), perfometer_logarithmic(perf_data[0][1], 40, 2, color)

def perfometer_check_check_informix_locks(row, check_command, perf_data):
    color = { 0: "#a4f", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
    return "%d" % int(perf_data[0][1]), perfometer_logarithmic(perf_data[0][1], 40, 2, color)

def perfometer_informix_dbspaces(row, check_command, perf_data):
    current = float(perf_data[0][1])
    used = float(perf_data[1][1])
    max = float(perf_data[2][1])
    used_perc = used / max * 100
    curr_perc = (current / max * 100) - used_perc
    h = '<table><tr>'
    h += perfometer_td(used_perc, "#f0b000");
    h += perfometer_td(curr_perc, "#00ff80");
    h += perfometer_td(100 - used_perc - curr_perc, "#80c0ff");
    h += '</tr></table>'
    return "%.1f%%" % used_perc, h

perfometers["check_mk-informix_dbspaces"] = perfometer_informix_dbspaces
perfometers["check_mk-informix_sessions"] = perfometer_check_check_informix_sessions
perfometers["check_mk-informix_locks"] = perfometer_check_check_informix_locks
