编译gcc/glibc: Ubuntu14.04, gcc4.82, glibc2.19, kernel3.13, x86_64-linux-gnu
编译时最好指定`--host=x86_64-linux-gnu`
编译时一定要加上`CFLAGS="-U_FORTIFY_SOURCE -O2 -fno-stack-protector"`,命令行或者修改`config.make`,
因为`ubuntu`默认加了`-D_FORTIFY_SOURCE=1` 和 `-fstack-protector`, 编译旧版本`gcc/glibc`会导致各种问题
比如下面的:
    `error: call to ‘__open_missing_mode’ declared with`

1. 编译gcc时,由于Ubuntu对x86和x64链接库的处理和旧版的不同,可参考下面列出的patch处理
    http://www.trevorpounds.com/blog/?p=111
    http://www.trevorpounds.com/blog/?p=513
2. error: field `info' has incomplete type
    grep "struct siginfo" -r . -l | xargs -I{} sed -i 's/struct\ siginfo/siginfo_t/g' {}
    http://stackoverflow.com/questions/26375445/error-compiling-gcc-3-4-6-in-ubuntu-14-04
3. ./../include/obstack.h:426:30: error: lvalue required as increment operand
    使用gcc3.4.6, 高版本gcc报该错误
4. ./.libs/libgcj.so: undefined reference to `__cxa_call_unexpected'
    可以只开启c和c++, 即可避免上面的问题(libjava导致）, --enable-languages=c,c++
5. /usr/bin/ld: cannot find crti.o: No such file or directory
    find到该文件,拷贝到当前目录或者CFLAGS中加-L
6. 编译glibc需要kernel header，高版本的未必能够编译成功，可能出现一堆符号错误
    --with-headers=/home/j/Downloads/linux-2.6.32.64/include
    ersion.h有些kernel版本没有:make include/linux/version.h
    其他有可能一些头文件找不到,可在kernel目录find并拷贝
7. 低版本glibc不带linuxthreads,但又需要,需要自己下载,configure添加--enable-add-ons=linuxthreads
8. #error "glibc cannot be compiled without optimization"
    上面添加的-O2, 有时候-O2会导致问题,可尝试-O或者-O3
9. version-info.h:1: error: missing terminating " character
    version-info.h由csu/Makefile生成，echo的问题导致双引号换行,使用以下patch(printf比echo有更好的可移植性)
    --- aaa/glibc-2.3/csu/Makefile	2002-08-15 15:54:11.000000000 +0800
    +++ glibc-2.3/csu/Makefile	2014-11-25 11:53:21.676369719 +0800
    @@ -210,14 +210,15 @@
     		   if [ -z "$$os" ]; then \
     		     os=Linux; \
     		   fi; \
    -		   echo "\"Compiled on a $$os $$version system" \
    -			"on `date +%Y-%m-%d`.\\n\"" ;; \
    +		   printf '"Compiled on a %s %s system on %s.\\n"\n' \
    +			"$$os" "$$version" "`date +%Y-%m-%d`" ;; \
     	   *) ;; \
     	 esac; \
     	 files="$(all-Banner-files)";				\
     	 if test -n "$$files"; then				\
    -	   echo "\"Available extensions:\\n\"";			\
    +	   printf '"Available extensions:\\n"';			\
10. sscanf.c:37: error: `va_start' used in function with fixed args
    修改stdio-common/sscanf.c，添加“,...”到函数参数
11. 使用2.6的内核编译，报一堆__NR_系统调用找不到,换kernel版本,不能太高也不能太低
    有些glibc还不支持x86_64需要强制设置成固定的
12. gen-sorted.awk: line 19: regular expression compile failed (bad class -- [], [^] or [)
    http://stackoverflow.com/questions/6396923/error-while-using-make-to-compile-glibc-2-11-1-for-linux-from-scratch
    安装gawk,并在编译时添加AWK=gawk,或按上面链接修改
13. make[2]: *** [/home/j/Downloads/glibc-2.12.1/build/sunrpc/xnlm_prot.stmp] 错误 139
    Segmentation fault (core dumped)
    -O以上好像会导致该问题，尝试更换binutils不管用
14. sorry, unimplemented: inlining failed in call to ‘syslog’: function body not available
    -U_FORTIFY_SOURCE 到 CFLAGS
15. multiple definition of `_dl_addr_inside_object'
    -fno-stack-protector 到 CFLAGS
16. 编译binutils需要添加--with-sysroot，不然glibc将无法使用--version-script
17. configure error  compiler must support C cleanup handling
     /tmp/ccd21eFw.s:13: Error: expecting string instruction after `rep'
    binutils版本太低与gcc版本不匹配导致的
18. x86_64编译32b的glibc
    ../configure  --prefix=/home/j/glibc-2.13-32/ CC="gcc -m32" CXX="g++ -m32" --host=i686-linux-gnu --build=x86_64-linux-gnu
    No rule to make target  /nptl/pthread_spin_trylock.o', needed by `lib-noranlib'.
    x86_64的cpu架构支持i686（兼容386），所以i386报错,改成上面的686即可

