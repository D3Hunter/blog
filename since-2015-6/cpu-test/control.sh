#!/usr/bin/env bash

action=$1
list=$2

if [ -z "$action" -o -z "$list" ]; then
	echo "$0 <action> <server-list>"
	echo "    action : swarm/update/stop"
	echo "    server-list : comma seperated ip list"
	echo "                  eg: 239,228,233,234"
	exit
fi

oIFS=$IFS
IFS=","
if [ $action == "swarm" ]; then
	for i in $list; do curl -X POST -d "locust_count=4000&hatch_rate=1000" "http://10.128.6.${i}:8089/swarm"; echo ; done
elif [ $action == stop ]; then
	for i in $list; do curl "http://10.128.6.$i:8089/stop"; echo; done
elif [ $action == "update" ]; then
	for i in $list; do scp test_locustio.py root@10.128.6.$i:/root/script; done
	for i in $list; do ssh root@10.128.6.$i 'cd /root/script; ./kill.sh'; done
	for i in $list; do ssh root@10.128.6.$i 'cd /root/script; ./run.sh; ./slave-local.sh'; done
else
	echo "invalid action $action"
fi
IFS=$oIFS

