#!/bin/sh
# locally install the plugin files - call as OMD-User

# exit immediately on error
set -e 

if type -p check_mk >/dev/null 2>&1; then
	: OK
else
	echo "error: check_mk not found. Cannot install." >&2
	exit 1
fi

TMPFILE=$( mktemp /tmp/$TPRO.XXXXXX) || exit 1
trap "rm -f $TMPFILE" EXIT SIGHUP SIGINT SIGQUIT SIGABRT SIGTERM


check_mk --paths | grep -e '^[ 	][ 	]*Locally installed' >$TMPFILE
if [ -s $TMPFILE ]; then
	: ok
fi

# get and check installation paths
PATH_CHECKS=$(grep 'Locally installed checks' $TMPFILE | sed 's/^[^:]*:[ 	]*//')
PATH_CHECK_MAN=$(grep 'Locally installed check man pages' $TMPFILE | sed 's/^[^:]*:[ 	]*//')
PATH_CHECK_AGENTS=$(grep 'Locally installed agents and plugins' $TMPFILE | sed 's/^[^:]*:[     ]*//')
PATH_CHECK_WEB=$(grep 'Locally installed Multisite addons' $TMPFILE | sed 's/^[^:]*:[  ]*//')
PATH_CHECK_PNP=$(grep 'Locally installed PNP templates' $TMPFILE | sed 's/^[^:]*:[     ]*//')
PATH_CHECK_DOC=$(grep 'Locally installed documentation' $TMPFILE | sed 's/^[^:]*:[     ]*//')
 
PATH_PERFOMETER=$PATH_CHECK_WEB/plugins/perfometer
PATH_WATOPLUGIN=$PATH_CHECK_WEB/plugins/wato
PATH_AGENT_PLUGINS=$PATH_CHECK_AGENTS/plugins


for DIR in $PATH_CHECKS $PATH_CHECK_MAN $PATH_CHECK_AGENTS $PATH_CHECK_WEB $PATH_CHECK_PNP \
	$PATH_CHECK_DOC $PATH_PERFOMETER $PATH_WATOPLUGIN $PATH_AGENT_PLUGINS; do
	if [ ! -d $DIR  -o ! -w $DIR ]; then
		echo "error: directory $DIR doesn't exist or ist not writable." >&2
		exit 1
	fi 
done


# installation:
# checks:
echo "installing files:"
for FILE in checks/*; do
	echo " $FILE"
	install -m 644 $FILE $PATH_CHECKS/
done

# # checkman:
for FILE in checkman/*; do
	echo " $FILE"
	install -m 644 $FILE $PATH_CHECK_MAN/
done

for FILE in pnp-templates/*; do
	echo " $FILE"
	install -m 644 $FILE $PATH_CHECK_PNP/
done

for FILE in agents/*; do
	echo " $FILE"
	install -m 644 $FILE $PATH_AGENT_PLUGINS/
done


for FILE in *perfometer*py; do
	echo " $FILE"
	install -m 644 $FILE $PATH_PERFOMETER/
done

for FILE in wato/*; do
	echo " $FILE"
	install -m 644 $FILE $PATH_WATOPLUGIN/
done

echo "installation complete"
