### build 7u
按照`README-builds.html`进行
这个文档略旧，比如里面说要用jdk6作为BOOTDIR，实际上需要跟当前编译的匹配
另外`ALT_JDK_IMPORT_PATH`可能是需要设置的
会遇到的错误，参考 https://community.oracle.com/docs/DOC-983184
`LANG=C`  否则会报字符错误
缺少头文件使用 `yum provides \*/Intrinsic.h` 查询
test_gamma 报 failed to initilized VM
1. 将hotspot/make/linux/Makefile中有关test_gamma的去掉，貌似跟当前系统
    已经安装的openjdk有关系
2. 使用oracle的jdk不会报错

sh ./make/scripts/hgforest.sh 可以对forest中的所有repo执行同样的命令
