#!/bin/bash
# controling life cycle of non-service programs.
# valid actions are start/stop/status


action=$1
program_name="xxxxxxxx"
regex="[p]ython xxxxxxxx.py"
directory="xxxxxxxx"
exec_command="python xxxxxxxx.py"

function getpid() {
    ps -ef | grep "$regex" | awk '{print $2}' 2> /dev/null
}

function status() {
    pid=$(getpid)
    if [ "$pid" != "" ]; then
        echo "pid of $program_name is $(getpid)"
    else
        echo "$program_name hasn't started yet."
    fi
}

function start() {
    pid=$(getpid)
    if [ "$pid" != "" ]; then
        echo "$program_name has started already."
        echo "pid of $program_name is $(getpid)"
    else
        pushd $directory > /dev/null
        nohup $exec_command &> /dev/null &
        popd > /dev/null
        echo "$program_name started successfully with pid $(getpid)."
    fi
}

function stop() {
    pid=$(getpid)
    if [ "$pid" != "" ]; then
        echo "killing $program_name with pid $pid"
        kill $pid
    else
        echo "$program_name hasn't started yet."
    fi
}

case $action in
    status)
        status
        ;;
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
        echo "invalid action $action"
        ;;
esac
