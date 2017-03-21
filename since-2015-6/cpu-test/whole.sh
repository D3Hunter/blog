#!/usr/bin/env bash
#set -x
current_dir=`pwd`
ips=$1
count=$2
script=$3
suffix=$4

function show_usage {
	echo "$0 <ip-list> <count> <script> <suffix>, eg: 239,228,233,234"
}

if [ -z "$script"]; then
	echo "script name can not be null: $script"
	show_usage
	exit
fi

if [ -z "$ips" -o -z $count ]; then
	show_usage
	exit
fi

function kill_weblogic {
        echo "--- killing weblogic"
        cd /root/Oracle/Middleware/user_projects/domains/base_domain/bin
        ./kill.sh &>/dev/null
        sleep 1
        cd $current_dir
}

function restart_weblogic {
	echo "--- restarting weblogic"
	kill_weblogic
	cd /root/Oracle/Middleware/user_projects/domains/base_domain/bin
	bash $script.sh &>/dev/null &
	sleep 1
	pid=$(ps -ef | grep [w]eblogic | awk '{print $2}')
	echo "--- current pid is: $pid"
	cd $current_dir
}

function update_script {
	servlet=$1
	echo "--- updating $servlet"
	cd $current_dir
	cp test_locust.py-template test_locust.py
	sed -i 's/REPLACE/'$servlet'/g' test_locust.py
	./control.sh update $ips
	sleep 1
}

function gather_data {
	echo "--- gathering data"
	servlet=$1
	pid=$(ps -ef | grep [w]eblogic | awk '{print $2}')
	./gather.sh $pid $count ${script}_${servlet}_${suffix}
}

restart_weblogic
sleep 20 # wait for startup

for test in Redis MongoDB Cassandra Memcached Spymemcached Xmemcached; do
	echo "------ Testing $test"
	./control.sh stop $ips
	update_script $test
	./control.sh swarm $ips
	sleep 1
	./wait-full-running.py $ips 2800 # wait for full running
	gather_data $test
done

