#! /bin/sh
# reside in /etc/init.d/
set -e

DESC="nginx daemon"
NAME=nginx
DAEMON=/usr/local/nginx/sbin/$NAME
SCRIPTNAME=/etc/init.d/$NAME
test -x $DAEMON || exit 0

d_start() {
	$DAEMON || echo -n " already running"
}
d_stop() {
	$DAEMON -s stop || echo -n " not running"
}
d_reload() {
	$DAEMON -s reload || echo -n " could not reload"
}
case "$1" in
	start)
		echo -n "Starting $DESC: $NAME"
		d_start
		echo "."
		;;
	stop)
		echo -n "Stopping $DESC: $NAME"
		d_stop
		echo "."
		;;
	reload)
		echo -n "Reloading $DESC configuration..."
		d_reload
		echo "reloaded.";;
	restart)
		echo -n "Restarting $DESC: $NAME"
		d_stop
		sleep 2
		d_start
		echo "."
		;;
	*)
		echo "Usage: $SCRIPTNAME {start|stop|restart|reload}" >&2
		exit 3
		;;
esac
exit 0
