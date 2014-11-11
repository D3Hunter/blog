## Linux命令相关

传统gnome桌面，可用Super+Alt+RB弹出任务条菜单

    gnome-session-fallback
    dconf-editor

卸载wine×后倒在Unity不可用，gnome界面也出不来，重装gnome
xwininfo xprop查看当前窗口信息
中文目录转成英文
    export LANG=en_US
    xdg-user-dirs-gtk-update
    export LANG=zh_CN

tar -xzf出错 先看看是否仅仅是tar而没有zip
command直接执行，不使用alias
打开的文件（加载的库）lsof -p <pid> 或者直接看/proc/<pid>/maps|fd|exe|cwd|exe 等文件

## dep包相关
安装dep包 sudo dpkg -i *.dep
apt-get download 下载dep包，安装过程可参考man dpkg主要执行特定脚本，然后复制文件（和/目录结构类似）
ar -x pakname.deb解压deb包

## emacs相关
emacs：indent-region format code
    没有redo的概念，可以按任意建使undo也可以undo，即时redo
    ctrl-q 加tab就可以输入tab

## linux自启动程序
service需要root才能看的所有service的状态
自启动方法
    1. use update-rc: Start in serial at boot time, make boot slow
    add filename ad /etc/init.d/filename
    add execute privldge to that filename
    update-rc.d filename defaults
    2. Ubuntu use Upstart to manage upstart services: can run in parallel
    add /etc/init/filename.conf, then filename will start on boot
    initctl list ; list state of all upstart services
    edit /etc/init/filename.conf to disable service or add manual to /etc/init/filename.override
Ref:http://askubuntu.com/questions/19320/how-to-enable-or-disable-services

## bash相关
让bash配置对所有用户生效：可在/etc/profile.d/中添加脚本，重启后则会生效，或者source /etc/profile && source ~/.bashrc让设置对当前终端生效

## 一些软件安装
部署OpenNote
    sqlite
    php5-fpm
    php5-sqlite
    libpcre3 for nginx
    sudo chown www-data:www-data OpenNote/（更改数据库权限）

配置php输出Debug错误
    /etc/php5/fpm/pool.d/www
    catch_workers_output = yes
    /etc/php5/fpm/php.ini
    log_errors = On
    在php中使用error_log
    public array PDOStatement::errorInfo ( void )

安装mysql
	sudo apt-get install mysql-server
	sudo apt-get install mysql-client
	grant select,insert,update,delete on mikehogue.* to adminSLMrZdy@localhost Identified by "M9wH6K-IlmtY";
tomcat
	$ sudo apt-get install tomcat7-admin
	$ sudo apt-get install tomcat7
	Tomcat bin folder is created in /usr/share/tomcat7
	Tomcat conf and logs folders are created in /var/lib/tomcat7
	创建可用manager ： conf/tomcat-users.xml
	 <user username="admin" password="admin" roles="admin-gui,manager-gui"/>
	在tomcat管理界面里可以reload工程以加载修改后的serverlet

## java相关
unsupported major.minor version：高版本编译的class尝试用低版本jvm运行
JVM内存介绍
	Heap Memory
	Eden Space: The pool from which memory is initially allocated for most objects.
	Survivor Space: The pool containing objects that have survived the garbage collection of the Eden space.
	Tenured Generation: The pool containing objects that have existed for some time in the survivor space.

	Non-heap memory
	Permanent Generation: The pool containing all the reflective data of the virtual machine itself, such as class and method objects. With Java VMs that use class data sharing, this generation is divided into read-only and read-write areas.
	Code Cache: The HotSpot Java VM also includes a code cache, containing memory that is used for compilation and storage of native code.

部署MySQLMyNotes要改名为MyNotes，修改MySQLConnection.jsp后需重新编译
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib:${CATALINA_HOME}/lib/servlet-api.jar


chrome F12 Network 看pending可以看什么在阻塞网页的显示（比如访问被墙的google服务）

OneAPM外部服务中不包含访问外部css或js，其实这个只能在浏览器端抓取
OneAPM对java7-8都不支持

CSS使用相对于应用根目录用/xx.css，但这样需要设置web能访问该文件

设置能够在特定位置打开应用程序,然后更改/usr/share/applications/defaults.list中对应.desktop
	gedit -g 955x1027+964+28
	gnome-terminal --geometry 103x55+0+0


tomcat中在</Host>前加以下控制访问权限（全局）
	<Valve className="org.apache.catalina.valves.RemoteAddrValve" allow="192.168.1.10" deny=""/>
	<Valve className="org.apache.catalina.valves.RemoteHostValve" allow="abc.com" deny=""/>

可使用javascript获取保存的密码（OpenNote）
document.getElementById('login').getElementsByTagName('input')[1].value
jQuery中可以按id class 和标签类型获取对象，分别为$('#id') $('.class') $('input:text')之类的
还可按属性选择，获取其值用val()函数，而不能使用上面的value

OpenNote 已保存密码不会设置到$scope中的相应字段中，必须每次都输入（loginController.js）
且可用chrome打开，但是不能使用firefox打开
cellular automaton Game of Life

看一下书签中的链接

