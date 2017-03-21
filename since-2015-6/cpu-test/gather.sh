#!/usr/bin/env bash

if [ $# -lt 3 ]; then
  echo "Usage $0 <pid> <count> <suffix>"
  exit
fi

pid=$1
count=$2
suffix=$3
data_file="cpu-$pid-$suffix.txt"
script_file="plot-script.plot"

top -p $pid -b -n$count > ${data_file}.raw

grep -w $pid ${data_file}.raw > ${data_file}

cat > ${script_file}  << EOF
#!/usr/bin/gnuplot

set terminal png
set term png size 800,400
set output "cpu-mem-$suffix-$pid.png"
set title "cpu-memory-$suffix-$pid"
set key top left box reverse

set xrange [0:*]
set yrange [0:*]
set y2range [0:*]
set y2tics
set format y '%.0f%%'
set format y2 '%.0f%%'
set ylabel 'cpu usage'
set y2label 'memory usage'

plot '${data_file}' using 9 axes x1y1 title 'cpu' with linespoints, \
    '${data_file}' using 10 axes x1y2 title 'mem' with linespoints
EOF

chmod +x ${script_file}
#./${script_file}

rm -f ${data_file}.raw ${script_file}
