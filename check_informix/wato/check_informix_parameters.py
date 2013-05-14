#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Rules for configuring parameters of checks (services) -- check_informix

register_check_parameters(
    subgroup_applications, 
    "informix_dbspaces", 
    _("IBM Informix dbspaces"), 
    Dictionary(
        help = _("This check monitors various aspects of IBM Informix dbspaces"), 
        elements = [ 
            ("levels",
                Alternative(
                    title = _("Dbspace usage levels"), 
		    elements = [
                        Tuple( 
                             title = _("Percentage free space"), 
                             elements = [ 
                                 Percentage(title = _("Warning below"),  unit = _("% free")), 
                                 Percentage(title = _("Critical below"), unit = _("% free")), 
                             ],),
                        Tuple( 
                             title = _("Absolute free space"), 
                             elements = [ 
                                 Integer(title = _("Warning lower than"), unit = _("MB")), 
                                 Integer(title = _("Critical lower than"), unit = _("MB")), 
                             ],),
		    ]
                ),
            ), 
	], 
    ), 
    TextAscii( 
        title = _("Dbspace"), 
        allow_empty = False
    ), 
    None) 

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


