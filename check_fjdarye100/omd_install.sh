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

for DIR in $PATH_CHECKS $PATH_CHECK_MAN ; do
	if [ ! -d $DIR  -o ! -w $DIR ]; then
		echo "error: directory $DIR doesn't exist or ist not writable." >&2
		exit 1
	fi 
done


# installation:
# checks:
echo "installing files:"
for CHECK in checks/*; do
	echo " $CHECK"
	install -m 644 $CHECK $PATH_CHECKS/
done
# checkman:
for CHECKMAN in checkman/*; do
	echo " $CHECKMAN"
	install -m 644 $CHECKMAN $PATH_CHECK_MAN/
done

echo "installation complete"
