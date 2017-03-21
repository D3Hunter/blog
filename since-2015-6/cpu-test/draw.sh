#!/usr/bin/env bash

suffix=$1
script_file=run.plot
tmp_file=${script_file}.tmp

cat > ${tmp_file}  << EOF
#!/usr/bin/gnuplot

name = 'cpu-${suffix}'
set terminal png
set term png size 1200,800
set output name.".png"
set title name
set key bottom right box reverse

set xrange [0:*]
set yrange [0:*]
set ytics  10 out mirror
set y2tics 10 out mirror
set grid ytics
set format y '%.0f%%'
set ylabel 'cpu usage'

plot \\
EOF
for name in $(ls *.txt); do
	suffix=${name##*-}
	suffix=${suffix%.*}
        color="linecolor rgbcolor 'black'"
        echo "'$name' using 9 title '$suffix' with linespoints, \\" >> ${tmp_file}
done

head -c -4 ${tmp_file} > ${script_file}

chmod +x ${script_file}
./${script_file}

rm -f ${tmp_file} ${script_file}

