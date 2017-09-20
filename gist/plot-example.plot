#!/usr/bin/gnuplot

name = 'metric-size-compare'
set terminal png
set term png size 800,600
set output name.".png"
set title name
set key top right box reverse

set xrange [0:*]
set yrange [0:*]
set ytics  5 out mirror 
set y2tics 5 out mirror 
show y2tics
set grid ytics
set format y '%.0f%%'
set ylabel 'percentage'

plot \
     'metric_datasize.txt' using (100*($1-$3)/$1) title 'none' with linespoints, \
     'metric_datasize.txt' using (100*($2-$4)/$2) title 'compressed' with linespoints

