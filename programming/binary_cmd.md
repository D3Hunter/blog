### od
- -A[doxn] 地址显示模式
- -jBYTES  跳过BYTES字节
- -tTYPE 显示格式  可多次指定,则多次显示
- -v 同hexdump
- -wBYTES 显示宽度
- -NBYTES 显示字节数
`BYTES`:可加0x前缀,可加bKM后缀,分别表示512 1024 1024*1024
`TYPE`: SIZE为数字,下列格式都可加后缀z, 表示在最后在打印可见字符
    SIZE大于1时会考虑端序再显示,所以可用来检查端序
       a       named character, ignoring high-order bit
       c       ASCII character or backslash escape
       d[SIZE] signed decimal, SIZE bytes per integer
       f[SIZE] floating point, SIZE bytes per integer
       o[SIZE] octal, SIZE bytes per integer
       u[SIZE] unsigned decimal, SIZE bytes per integer
       x[SIZE] hexadecimal, SIZE bytes per integer
       后面追加`z`可以并排显示可打印字符
### xxd
-b       以2进制显示
-c cols  每行字节数
-g bytes 每组字节数,默认2
-l len   只显示len个字节
-p       postscript连续hexdump
-r       revert(无-p要求每行输入有行号,从0开始,形式为"0: "),只能无格式revert
### int转成binary,考虑端序
printf "%.8x" $int | sed -E 's/(..)(..)(..)(..)/\4\3\2\1/' | xxd -r -p >>file
查看端序echo -n 12 | od -tx2
