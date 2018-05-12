#!/bin/bash


action=$1
target=$2
argument=$3

local_ip=$(ifconfig | sed -En 's/127.0.0.1//;s/10\.//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p')

function print_help() {
    cat << EOF
controling life cycle of non-service programs.
Run with: $0 action target [argument]
    valid actions are :
        start
        stop
        restart
        status
        top [interval]
        start-record [filename]:default to cpu.log
        restart-record [filename]:default to cpu.log
        stop-record
EOF
}

case $target in
    abcdefg)
        program_name="abcdefg"
        ps_regex="[p]ython abcdefg.py"
        directory="abcdefg"
        exec_command="python abcdefg.py"
        ;;
    tools_site)
        program_name="tools_site"
        ps_regex="server/bin/python manage.p[y] runserver"
        directory="tools_site"
        exec_command="python manage.py runserver $local_ip:8000"
        ;;
    *)
        echo "invalid target $target"
        print_help
        exit
        ;;
esac

function getpid() {
    regex=$1
    ps -ef | grep "$regex" | awk '{print $2}' 2> /dev/null
}

function status() {
    regex=$1
    name=$2
    pid=$(getpid "$regex")
    if [ "$pid" != "" ]; then
        echo "pid of $name is $(getpid "$regex")"
    else
        echo "$name hasn't started yet."
    fi
}

function start() {
    regex=$1
    name=$2
    dir=$3
    cmd=$4
    pid=$(getpid "$regex")
    if [ "$pid" != "" ]; then
        echo "$name has started already."
        echo "pid of $name is $(getpid "$regex")"
    else
        pushd $dir> /dev/null
        nohup $cmd &> nohup.out &
        popd > /dev/null

        # wait a while to get pid, in case there're delay in $cmd
        sleep 0.5
        pid=$(getpid "$regex")
        echo "$name started successfully with pid $pid."
    fi
}

function stop() {
    regex=$1
    name=$2
    pid=$(getpid "$regex")
    if [ "$pid" != "" ]; then
        echo "killing $name with pid $pid"
        kill $pid
    else
        echo "$name hasn't started yet."
    fi
}

function view_in_top() {
    regex=$1
    name=$2
    delay=$3
    pid=$(getpid "$regex")
    if [ "$pid" != "" ]; then
        if [ "$delay" = "" ]; then
            delay=1.5
        fi
        top -p $pid -d $delay
    else
        echo "$name hasn't started yet."
    fi
}

function view_in_gcutil() {
    regex=$1
    name=$2
    delay=$3
    pid=$(getpid "$regex")
    if [ "$pid" != "" ]; then
        if [ "$delay" = "" ]; then
            delay=1000
        fi
        jstat -gcutil $pid $delay
    else
        echo "$name hasn't started yet."
    fi
}

function start_record_cpu() {
    regex=$1
    filename=$2
    if [ "$filename" = "" ]; then
        filename="cpu.log"
    fi
    pid=$(getpid "$regex")
    top -bp $pid -d 5 | grep --line-buffered 'python' | awk -W interactive '{print $9}' > $filename &
}

function stop_record_cpu() {
    regex=$1
    pid=$(getpid "$regex")
    kill $(ps -ef | grep "[t]op -bp $pid" | awk '{print $2}' 2> /dev/null)
}

case $action in
    status)
        status "$ps_regex" "$program_name"
        ;;
    start)
        start "$ps_regex" "$program_name" "$directory" "$exec_command"
        ;;
    restart)
        stop "$ps_regex" "$program_name"
        sleep 1
        start "$ps_regex" "$program_name" "$directory" "$exec_command"
        ;;
    stop)
        stop "$ps_regex" "$program_name"
        ;;
    top)
        view_in_top "$ps_regex" "$program_name" "$argument"
        ;;
    gcutil)
        view_in_gcutil "$ps_regex" "$program_name" "$argument"
        ;;
    start-record)
        start_record_cpu "$ps_regex" "$argument"
        ;;
    restart-record)
        stop_record_cpu "$ps_regex"
        sleep 1
        start_record_cpu "$ps_regex" "$argument"
        ;;
    stop-record)
        stop_record_cpu "$ps_regex"
        ;;
    help)
        print_help
        ;;
    *)
        echo "invalid action $action"
        print_help
        ;;
esac
