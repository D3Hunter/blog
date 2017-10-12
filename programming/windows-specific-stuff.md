### Windows配置及工具使用
appwiz.cpl打开卸载程序
控制面板对应的命令为`control`

`tasklist /m xxx.profile.dll`查看是否有进程加载该dll
`dumpbin /all` 在.text段可看到IL code使用RVA查看方法体
`dumpbin /headers`查看64或者86
`nmake`里的macro类似make里的variable，引用方法也相同，大小写敏感，需要注意的是nmake本身的关键词是大小写不敏感的
vs中`ERR, hr`可查看上一个错误
`gacutil -i <>` 安装某个.net的DLL，有时.net的msi安装包安装不上，有时报找不到某个库的某个符号，但该版本的DLL都是正确的，原因有可能为该DLL未注册上
解压msi包：`msiexec /a /path/to/msi /qb TARGETDIR=/absolute/extract/path`

windows xp系统名称里，只要没写64那就是32

windows本地策略->审核策略->开启登陆审核，这样才会记录错误登陆事件
键盘按键慢，可设置键盘的字符重复速度

安装service: `sc create MathsService binPath= %SYSTEMROOT%\System32\Maths.exe type= own type= interact start= demand DisplayName= "My fabulous Maths service"`

`msiexec`安装程序，`/i /x /l*`(输出日志)，可查看帮助看看
`net start/stop`和`sc start/stop`都可用来管理服务，但sc直接返回不会等待启动完成

在notepad++中查找unicode字符[^\x00-\x7F]，vs的`warning C4819`


### bat脚本
变量赋值`set xxx=yyy`等号前面的空格会被当成变量名，后面的空格会被当作值因此需要注意，引用改变量使用`%xxx%`
`if`不支持 `and or`，需要自行实现
`goto`标签的冒号在前面
查看帮助，直接在cmd里输入`if /?`
`echo.`才能输出空行，否则只是显示是否处于打开状态
`"echo."`可以打印字符串，`"."`后面的都会被打印出来
当前路径为`%~dp0`，可以参考`for /?`
`cmd`里的函数用goto标签实现，函数结束为`goto:eof`，然后call标签就行
`exit`默认会连上层cmd一块退出，使用`exit /B`
cmd里的注释使用`"::"`

避免某个bat影响当前环境，使用`setlocal/endlocal`
- setlocal
- call %VS100COMNTOOLS%vsvars32.bat
- devenv myProject.sln /Build "Debug|Win32"
- endlocal
cmd在if里设置环境变量如果存在带空格路径会报错，在if外就没事

###windows编程
`strcasecmp`最初出现在string.h，glibc中有，但posix标准将其定义在strings.h中
`snprintf`保证最后一个字符为0，windows下的`_snprintf`不保证这点
windows上的`select`中至少有一个`fd-set`必须不为null，且还得有至少一个handle，因此不好用来实现nanosleep
`__impl__`是windows的动态库链接用lib的符号前缀, `name decoration`
DLL导出的符号必须要`__declspec(dllexport)`、`#progma(linker)`或者使用`DEF`表
`__stdcall`即`WINAPI`，由`callee`释放栈，不适合变长参数函数，这类使用`__cdecl`
Windows下DLL会在`PATH`目录中搜索，优先级稍微靠后

忽略编译警告：c/c++高级，忽略特定警告（只有数字，不包含前面的c）
忽略链接警告，在所有选项的命令行里：/ignore:4099，但是4099被标定为不可忽略。4244;4018;4267
nmake里INCLUDE 和LIB都是预设好的指向vs目录的，覆盖后会提示找不到头文件等错误
vc++2012编译的程序在xp上报：`Invalid win32 application`.安装`vs2012 update1/3/4`, 安装update2貌似不行，然后在项目属性`General -> Platform toolset`里选择`v110_xp`
`Tools – Options – Projects and Solutions` – 取消打开错误列表选项.
vs2012 solution explorer有个预览，关闭就可以取消在右边打开文件
查看include-tree: `Project Settings -> Configuration Properties -> C/C++ -> Advanced -> Show Includes`

在命令行里使用`v110_xp`除了要使用vcvarsall还要设置INCLUDE/PATH/LIB/CL/LINK等变量，并在编译时添加`/D_USING_V110_SDK71_`(设置了CL貌似就不用了)

windows上如果一个extern符号设置错了,比如使用阶段，但设置了__declspec(export)，这就会导致linker找不到符号，因为linker会尝试在本地代码中寻找符号，相比起来linux并不把符号绑定到某个库上，.so在链接阶段并不会去解析外部符号，而是推迟到load阶段，但windows上强制在链接阶段必须指定lib(对应的DLL)

可通过`FD_SETSIZE`设置`select`支持的socket数目，这需要在引入`winsock2.h`的头文件前添加，可通过工程或makefile设置`-DFD_SETSIZE=xxxx`。参考https://msdn.microsoft.com/zh-cn/library/windows/desktop/ms739169(v=vs.85).aspx

### windows下编译zlib/curl/sigar库
`ZLIB`：windows上incluede `zlib.h`，默认为`__cdecl`，使用`win32/Makefile.msc`编译的也是如果使用的是`zlibwapi.lib`，则需要在include前定义`ZLIB_WINAPI`切换windows上编译zlib，使用win32下的Makefile，在contrib\vstudio目录下有sln工程，但编译出来有问题

`CURL`：curl默认使用DLL链接，`#define CURL_STATICLIB`使用静态库，在linux下没有该问题，因为linux下不会单独生成一个.lib的文件，.a的符号是与.so的符号是一致的。使用vs编译curl：winbuild目录下`nmake /f Makefile.vc VC=11 mode=static MACHINE=x64`
`curlbuild.h`为平台相关的内容，该文件并不包含在git代码库中，而在每日的`tar.gz`中。cmake过程中可生成该文件

`SIGAR`：sigar在windows上`sigar_proc_exe_get`引用`sigar_proc_exe_wmi_get`，而该函数是在一个cpp文件内定义的，需要改成c++编译器`Properties>C/C++>Advanced>C++ Code(/TP)`。错误为：`Native Compiler support only available in C++ compiler`

