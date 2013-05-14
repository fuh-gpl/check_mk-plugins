#!/usr/bin/python
# encoding: utf-8
#
aggregations += [
  ( "Hosts", FOREACH_HOST, ALL_HOSTS, "db_informix", ["$1$"] ),
]

aggregation_rules["db_check_informix"] = (
  "IBM Informix database $DB$",
  [ "HOST", "DB" ],
  "worst",
  [
      ( "$HOST$", ".*IDS $DB$[ .]" ),
      # if the servername is part of the message files:
      ( "$HOST$", ".*LOG.*online.log.$DB$" ),
      ( "$HOST$", ".*LOG.*online.$DB$.log" ),
      ( "$HOST$", ".*LOG.*online.con.$DB$" ),
      ( "$HOST$", ".*LOG.*online.$DB$.con" ),
  ]
)

### Datenbanken allgemein
aggregation_rules["db_informix"] = (
  "IBM Informix databases",
  [ "HOST" ],
  "worst",
  [
      ( FOREACH_SERVICE, "$HOST$", "IDS ([^ ]*)  status", "db_check_informix", ["$HOST$", "$1$" ] ),
      ( "$HOST$", ".*LOG.*online.log" ),
      ( "$HOST$", ".*LOG.*online.con" ),
  ]
)
