`RemoveFolder`不指定Directory默认为起父目录，如果有多个父目录报`not listed in the RemoveFile table.`
Wix里的NOT Installed指的是当前程序还未安装过
`没有权限启动service`设置`Account="LocalSystem"`，当程序不能运行也会报这个错误，如缺少DLL等
本地化通过 `-cultures:zh-CN`设置，本地化文件`.wxl`通过`-loc`设置
**另一个版本已经安装，先卸载**问题，是Product设置了GUID的问题，设置成*
`AllowSameVersionUpgrades`设置成yes，这样同版本安装才不会成为两个，而是当作升级
`candle`中定义变量`-dMyVariable="Hello World"`
由于`WindowsInstall`非事件驱动，`根据输入enable下一步`并不会自动刷新，需要切换dialog才能刷新，但`licenseAgreement`界面的checkbox可以
调试服务DLL: 可以在DLL前搞个`MessageBox`，然后附加调试，或者使用`MsiBreak`
DLL默认导出的符号有Decoration，在wix中使用时需要保持符号名称在DLL中存在，因
    此最好使用上面的方法将其Decoration去掉
`KeyPath`用于表示一个`component`，WindowsInstall使用其对应资源确定该Component是否损坏和需要修复，因此最好的做法是**一个文件一个component**这样当文件丢失时，WI可以修复，如果多个文件，但`KeyPath`文件存在WI会认为其没有损坏
如果添加到Programs的folder内容为空，Wix不会生成该目录，至少要一个item才行，可以使用`CreateFolder`创建空目录，但不能创建空文件
`AO_WixUI_FeatureTree`的Back最高的order为2，要想覆盖该设置需要设置更高的order
customaction设置了sequence后仍是随机执行的，不保证顺序
Wix使用IniFile可直接更改`Ini`文件，可在安装过程中修改，可避免用customAction输出到ini文件带来的权限及顺序问题，Ini修改应该是在安装Component过程中进行的，且在`StartService`之前。类似的，Wix也支持对xml格式的配置进行设置
CustomAction如果需要权限应设置`Execute="deferred"`或者Commit且`Impersonate="no"`
`Advertised`只有个feature可用，但是并没安装，当用户想使用时（点击快捷方式）再安装，而`non-advertised`则是直接安装上
WindowsInstall定义了一些Property（变量，比如`CommonAppDataFolder`等），wix本身也有些`Built-in Variables`，两者有重复
Wix中的变量必须要加`var.`前缀才能访问

candle的`-arch`会设置sys.BUILDARCH和sys.PLATFORM，默认为x86，如果该设置与ProgramFiles目录设置不匹配会报error，因此ProgramFiles需要根据arch设置，如果安装包里既有32又有64，可用component的Win64属性设置
Package的Platform属性也可以设置arch，但推荐使用-arch