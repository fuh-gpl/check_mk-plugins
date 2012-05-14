#!/usr/bin/python
# encoding: utf-8
#
aggregations += [
  ( "Hosts", FOREACH_HOST, ALL_HOSTS, "db_informix", ["$1$"] ),
]

aggregation_rules["db_check_informix"] = (
  "Informix IDS - $DB$",
  [ "HOST", "DB" ],
  "worst",
  [
      ( "$HOST$", ".*IDS $DB$[ .]" ),
  ]
)

### Datenbanken allgemein
aggregation_rules["db_informix"] = (
  "Informix Databases",
  [ "HOST" ],
  "worst",
  [
      ( FOREACH_SERVICE, "$HOST$", "IDS ([^ ]*)  status", "db_check_informix", ["$HOST$", "$1$" ] ),
      ( "$HOST$", ".*LOG.*online.log" ),
  ]
)
