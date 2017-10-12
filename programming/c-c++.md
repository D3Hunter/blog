## C/gcc
### 获取当前调用栈
`libc`中提供`backtrace*`方法，可访问当前函数栈信息（在程序中直接得到）
在`windows`下可使用`CaptureStackBackTrace`或者`StackWalk*`来访问.
- 使用gcc编译除了要加`-g -ggdb`外，还要添加`-rdynamic`使`ld`将所有符号都添加到动态符号表中
使用addr2line将函数地址转成函数名，或libunwind

### C
`snprintf`会自动加`null`字符
`read/write`读取`socket`，返回`0`表示对方关闭连接
`linux`栈溢出不报错，如果访问相关地址则会导致`SIGSEGV`
如果修改了头文件中结构体信息比如将某指针换成值，而`makefile`又没将头文件作为依赖, 这时某些已经编译过的源文件就不会再编译，也会链接成功，但执行时会出现很奇怪的段错误,（比如指向同一地址的两个指针再`gdb`中打印出不同的结果）
编译时除了库一致，头文件也要一样（不然出现类似`undefined reference to __poll_chk`的错误）
`va_list`变量多次使用可能会出现问题（段错误等），跟实现有关
若想多次使用，可以用`va_copy`拷贝一份（最后仍要`va_end`). 参考http://julipedia.meroh.net/2011/09/using-vacopy-to-safely-pass-ap.html
`write`在`buf`地址为非法的地址时`errno`为`EFAULT`，**可以用来验证地址是否合法**
`SIGCHILD`被mask不会影响`wait/waitpid`
`setlocal`非常损耗性能，不嗯作为循环内函数
`snprintf/vsnprintf`对性能影响较大，基于循环的拷贝次之，`memcpy`就好些（估计被优化过）
`()`表示函数接收任意个参数，`(void)`表示接收0个参数,使用`strict-prototype`后，如果定义了`()`但没使用其参数，会报`warning`
`strspn/strcspn`
`Cproto`获取C文件中的函数列表
centos5.5下编译找不到`pthread_mutexattr_settype`，需要定义`-D_GNU_SOURCE`
对于对齐的变量的读写操作硬件保证不会出现一半旧一半新的情况, 这是原子操作
`dyncall`库可以动态调用C中的函数
表示`section`开始结尾：`__start_SECTION and __stop_SECTION`，如果段为空，则对于符号未定义
对外使用的数据结构要定义在`.h`中，否则编译会有`incomplete type`错误
`shmget`设置的`shared memory`不会自动在引用进程数为0时自动删掉，看一下`mmap`
有些符号如果是用宏生成的，搜索时需要注意
`memset std::string`导致崩溃，面向对象的，c++会初始化`vtable`
linux下堆上申请的空间在未使用时是不占用内存页的，实际写入时再分配，因此仅`malloc`在,`free`中是看不到的
`glibc`是向后兼容的

#### 以下语法可以方便的`break`（类似`goto`的效果）
```
do {
    // xxx
}while(false);
```
#### 让动态库可以运行：
1. 有`x`权限
2. 设置`entry point`: `-Wl,-e entry_point`
3. 设置`Interpreter(.interp section)`:
```
const char my_interp[] __attribute__((section(".interp"))) = "/lib/ld-linux.so.2";
```
#### `.so`构造、析构函数
- `-init,<function name> -fini`可用来指定`.so`的`ctor/dtor`,这会在`.so`中生成对应`section`
- `__attribute__((constructor))`好像是等效的。貌似用`-init`和`-fini`不能使用名为`init/fini`的函数名称，其他的可以
#### `全局变量`可以声明一次，然后在后面再初始化，初始化必须加上类型表示，比如：
```
    int global;
    int global = 1;
```
#### pthread
`pthread_cleanup_push/pop`
`pthread_cond_wait`调用完仍然是可以cancel的，应该是用信号实现的, cancel时不消耗cond的signal计数
`pthread_mutex_lock/unlock`隐含memory barriar操作

unix-socket如果文件存在，bind会提示INUSE，另外该文件在试用期间不能随意删除，否则其他进程连不上
    使用文件权限设置连接权限，根据需要需要设定umask或者设定文件mode

### Data Model
Data model  Sample operating systems
:-:         :-:
LLP64       Windows (x86-64 and IA-64)
LP64        Most Unix and Unix-like systems, Solaris, Linux, BSD, OS X; z/OS
ILP64       HAL port of Solaris to the SPARC64
SILP64      Classic UNICOS[34]
ILP32       基本上所有的32系统都使用该模型

Datatype    LP64    ILP64   LLP64   ILP32   LP32
char        8       8       8       8       8
short       16      16      16      16      16
_int32              32
int         32      64      32      32      16
long        64      64      32      32      32
long long                   64
pointer     64      64      64      32      32

#### function without declaration
编译`C`程序，如果函数没声明就使用，编译器会设置默认返回`int`，在`32`位环境下没问题，在`64`位环境下可能会导致严重错误
比如返回一个`64`位指针，则会被强转成`32`位`int`，导致错误
所以在编译程序时，要特别注意警告，最好设置成存在警告则编译失败
`-Werror-implicit-function-declaration`
`-Werror`使所有警告变成错误
该错误源自`gcc`默认使用`gnu89`标准,该标准会默认使函数返回`int`,故可使用`-std=c90`或`c99`来避免该问题

### 提高程序的兼容性:
1. 完全静态链接libc libc++可避免出现GLIBC_2.14 not found等错误
        -static-libgcc -static-libstdc++ -static
        -static 和 -ldl是冲突的，但是gcc允许同时指定，只有-static有效
2. 静态链接不是最好的支持程序可移植的方式, 见下
        http://people.redhat.com/~drepper/no_static_linking.html
3. 较好的方式是获得另一个libc/c++库, 连接时使用-L(或LIBRARY_PATH,但在64上编32位程序时失效,估计跟gcc默认设置有关)指定过去
        (或者使用--sysroot, 测试发现我的系统不管用)
4. 在一个支持的最底版本系统上编译(chroot, docker等)

### gcc
`gcc`会按命令行从左往右的顺序扫描符号，使用`gcc`编译程序时一定注意链接库指定顺序，否则可能出现明明指定了正确的库，但是仍然报找不到符号的问题。
`glibc`编译后`libpthread.so`和`libc.so`都是脚本，里面指定实际库所在绝对位置，如果更改了位置需要进行修改。这可能会导致可能出现加了`-L`,但是`ld`找的库却在另一个目录的情况,导致链接失败
`gcc`中`-Wl`向`ld`传参数, 比如`-Wl,--verbose`查看链接使用的库路径及详细检索过程
`gcc -print-search-dirs | sed 's/:/\n/g'`查看默认库及头文件搜索路径
`gcc -dumpspecs`可查看默认的`flag`等信息, `-specs`指定使用的`specs`
`gcc4.1.2(CentOS 5.5)`要使用`PTHREAD_MUTEX_ERRORCHECK`需`-D_GNU_SOURCE`
`-fdata-sections -ffunction-sections`加`-Wl,--gc-sections`去掉不用的函数，需要rebuild
`ar rcs libout.a out.o`生成静态库
`-H -M`显示include tree，`-MM`跳过系统头文件

#### 查看`gcc`默认的`include`路径
- gcc -xc -E -v -
- gcc -xc++ -E -v -
- gcc -Wp,-v -x c++ - -fsyntax-only
- gcc -print-prog-name=cc1plus` -v显示include路径
#### 通过环境变量设置路径：
- include: `C_INCLUDE_PATH` `CPLUS_INCLUDE_PATH`或者`CPATH`
- library: `LIBRARY_PATH`
#### 符号表
`gcc -s strip`掉符号表
创建shared library时，`gcc`默认所有全局符号都会被导出（`visibility=default`）.可以设置`-fvisibility=hidden`，再对需要的符号设置`visible`
`gcc -rdynamic` 将所有符号放到`dynamic symbol table`, `dlsym/backtrace`都需要. 非动态符号（导出符号），使用`dlsym`是得不到其地址的
#### gcov
- 编译`-fprofile-arcs -ftest-coverage`链接阶段`-lgcov`，`--coverage`可替代前两者
- `exit`可以`gcov`得到，`_exit`，`_Exit`会导致`__gcov_flush`不被调用而得不到coverage
- `.gcno`编译时生成，记录行号及块信息
- `.gcda`运行时生成，记录实际执行的位置及分支，多次运行会追加
- `gcov-tool`可以用来merge`.gcda`文件，2014.9后的版本才有，还得从源码编译
`GCOV_PREFIX/GCOV_PREFIX_STRIP`设置`gcda`输出位置，但是使用`gcov`时仍然需要拷贝回object目录,否则`gcov`不能正确寻找对应文件
##### code coverage可以使用gcov，用gcovr或lcov生成结果
生成报告`gcovr -r .. -e 'test.*' -e 'third*' --html --html-details -o daemon_cov.html`

### Makefile
`makefile`里直接调用`make`不会继承当前的参数比如`-f`，导致奇怪的结果 `${MFLAGS}`为传入的参数
`makefile`里的`target`，如果没有`prerequisites`，且当前目录下已经有同名文件/目录，`make`会把其当作up to date，而不去执行，这时将其放入`.PHONY`中即可避免该问题
`VPATH`: Search Path for All Prerequisites and targets 如果在当前目录找不到会使用`vpath`做prefix来查找
make VERBOSE=1

Makefile里执行shell：`$(shell <command>)`
make SHELL='sh -x'

编译32b添加CC="gcc -m32" CXX="g++ -m32"

### ld/ld.so/elf
编译动态库,允许动态库中有`U`符号,编译可执行时,则需要使用下面的选项
- `ld --allow-shlib-undefined`允許定义的符号
- `ld -z lazy`指定`lazy loading`

`/lib/ld.so a.out` dynamic linker/loader
`/lib/ld-linux.so.{1,2}` ELF dynamic linker/loader
`/etc/ld.so.cache` File containing a compiled list of directories in which to search for shared objects and an ordered list of candidate shared objects
`/etc/ld.so.preload` File containing a whitespace-separated list of ELF shared objects to be loaded before the program.
`RPATH`里可以使用：`$ORIGIN`可以用相对于`elf`的路径，`$LIB`解析成`lib/lib64,$PLATFORM`,可以使用`chrpath`修改`RPATH`
加载某个动态库除了`LD_PRELOAD`，还可用`/etc/ld.so.preload`，但后者是全局的。或使用`ptrace ATTACH`到进程，向暂时无用的代码段写入代码，修改寄存器来执行
`LD_LIBRARY_PATH`运行时`.so`搜索地址

`ld.so`调试功能
`LD_BIND_LAZY` `LD_BIND_NOW`
`LD_DEBUG`
- libs        display library search paths
- reloc       display relocation processing
- files       display progress for input file
- symbols     display symbol table processing
- bindings    display information about symbol binding
- versions    display version dependencies
- all         all previous options combined
- statistics  display relocation statistics
- unused      determined unused DSOs
- help        display this help message and exit

`readelf -a` 查看符号是变量还是函数(`nm`看不出来)
readelf -s --wide
`ldd -v` 可显示所依赖的库版本

#### 仅静态链接部分library：
`gcc <objectfiles> -Wl,-Bstatic -lstatic1 -lstatic2 -Wl,-Bdynamic -ldynamic1 -ldynamic2`
`-Wl,-Bstatic`换成`-static`是不行的，这会导致`ld`设置错误的`ld.so`，可执行程序不能运行

### gdb
常用命令及选项
- list/list -
- break/delete/info break
- info inferiors/locals/args/signals [signal]
- inferior <N>
- handle signal <op>
- file/attach/kill/continue/run后面可接参数（或再命令行使用`--args`)
- next/step
- print/set print elements 0 设置`gdb`的打印元素上限，`0`为不限制
- printf "%s\n", some_string 不escape打印
- bt/where
- set/show args
- cd/pwd
- info program
- display
- watch
- call
- layout src.
- info threads/thread/frame
- `print mutex`可查看那个线程拥有`mutex`
- `set follow-fork-mode <mode>` 调试`child/parent`
- `gdb`调动态库，设置函数断点后会提示你加载动态库，适合调使用`dlopen`打开的动态库
- call可直接调用函数
- 断点后执行命令：
```
break 403
    commands
        silent
        set x = y + 4
        cont
    end
```

detach-on-fork
- on，根据`follow-fork-mode`其中一个被debug，一个detach. 需要注意的是，只有第一个child会被catch，所以如果遇到某个断点怎么都触发不了, 可能是因为该断点不在第一个child触发导致
- off，根据`follow-fork-mode`一个debug一个suspended

`gdb --pid  attch`进程
使用`valgrind`和`gdb`一起查`mem leak`
`gdb7.7`内置的`python3`, 有些包（`voidwalker`）执行不了
`gdb`的`prompt`由于不能使用`\[\]`故可使用`\001\002`，参考`linux_related.txt`
`gdb`启动出现`《PRESS ENTER`时，就会出现关闭echo的问题，启动gdb时扩大terminal大小就没问题,该问题也会导致上面的问题
`set detach-on-fork off`可以同时调试parent-child
`printf "%s\n", string`
打印数组：`p *list@20`
内存断点 `watch/rwatch/weatch`
条件断点`break x:20 if strcmp(y, "hello") == 0`

看内存：`x/nfu addr`
1. `nfu` means: repeat count, format, unit size
2. `format`: ‘x’, ‘d’, ‘u’, ‘o’, ‘t’, ‘a’, ‘c’, ‘f’, ‘s’
3. unit size:
    - b Bytes.
    - h Halfwords (two bytes).
    - w Words (four bytes). This is the initial default.
    - g Giant words (eight bytes).

### g++
`-isystem` dir Search dir for header files, after all directories specified by `-I` but before the standard system directories.

### misc
直接运行`/lib/libc.so.6`可查看其信息
缩减二进制尺寸
http://www.amigacoding.de/index.php?topic=168.0