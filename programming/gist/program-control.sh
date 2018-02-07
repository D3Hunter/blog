#!/bin/bash


action=$1
argument=$2
program_name="xxxxxxxx"
regex="[p]ython xxxxxxxx.py"
directory="xxxxxxxx"
exec_command="python xxxxxxxx.py"

function print_help() {
    cat << EOF
controling life cycle of non-service programs.
Run with: $0 action [argument]
    valid actions are :
    start
    stop
    restart
    status
    top [interval]
EOF
}

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

function view_in_top() {
    pid=$(getpid)
    if [ "$pid" != "" ]; then
        if [ "$argument" = "" ]; then
            argument=1.5
        fi
        top -p $pid -d $argument
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
    restart)
        stop
        sleep 1
        start
        ;;
    top)
        view_in_top
        ;;
    help)
        print_help
        ;;
    *)
        echo "invalid action $action"
        print_help
        ;;
esac
