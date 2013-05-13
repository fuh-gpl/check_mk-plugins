#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Rules for configuring parameters of checks (services)


register_check_parameters(
    subgroup_applications,
    "informix_locks",
    _("IBM Informix locks"),
    Dictionary(
        help = _("This check monitors the current number of active locks on IBM Informix"), 
        elements = [ 
            ("levels",
                Tuple( 
                     title = _("Number of active sessions"), 
                     elements = [ 
                         Integer(title = _("Warning at"),  unit = _("sessions"), default_value = 100), 
                         Integer(title = _("Critical at"), unit = _("sessions"), default_value = 200), 
                     ], 
                ), 
            ), 
	], 
    ), 
    TextAscii( 
        title = _("Servername (informixserver)"), 
        allow_empty = False
    ), 
    None) 

register_check_parameters(
    subgroup_applications, 
    "informix_sessions", 
    _("IBM Informix sessions"), 
    Dictionary(
        help = _("This check monitors the current number of active sessions on IBM Informix"), 
        elements = [ 
            ("levels",
                Tuple( 
                     title = _("Number of active sessions"), 
                     elements = [ 
                         Integer(title = _("Warning at"),  unit = _("sessions"), default_value = 100), 
                         Integer(title = _("Critical at"), unit = _("sessions"), default_value = 200), 
                     ], 
                ), 
            ), 
	], 
    ), 
    TextAscii( 
        title = _("Servername (informixserver)"), 
        allow_empty = False
    ), 
    None) 

register_check_parameters(
    subgroup_applications, 
    "informix_tabextents", 
    _("IBM Informix table extents"), 
    Dictionary(
        help = _("This check monitors the max number of table extents on IBM Informix"), 
        elements = [ 
            ("levels",
                Tuple( 
                     title = _("Max number of table extents"), 
                     elements = [ 
                         Integer(title = _("Warning at"),  unit = _("extents"), default_value = 40), 
                         Integer(title = _("Critical at"), unit = _("extents"), default_value = 70), 
                     ], 
                ), 
            ), 
	], 
    ), 
    TextAscii( 
        title = _("Servername (informixserver)"), 
        allow_empty = False
    ), 
    None) 


