清除linux缓存echo 3 > /proc/sys/vm/drop_caches
DistroWatch可查看个linux/bsd发行版携带的软件版本情况，及其他各类信息
getenforce/setenforce控制SELinux，centos默认开启，ubuntu默认关闭
yum install lrzsz
atyle --style=kr --mode=c -H 格式化代码
`yum provides \*/Intrinsic.h` 查看哪个package提供了对应的头文件

DMI Desktop Management Interface; SMBIOS, System Management BIOS

### update-alternatives - maintain symbolic links determining default commands,
比如在多个JDK版本中切换，针对java/javac需要单独切换
update-alternatives --config java

### 重启网络
ifdown/ifup，/etc/init.d/networking restart是重启所有网络
ip link set eth0 promisc on
ip link set eth0 multicast off

### 文件编码
enca filename查看文件编码
enconv -L zh_CN -x UTF-8 filename转换编码
iconv -f encoding -t encoding inputfile
convmv -f UTF-8 -t GBK -notest filename 文件名编码转换

### terminal出现乱码
`terminal`的输出变乱（按回车会打印PS1但并不换行，输入也不显示），是`echo`被关闭导致,可使用`reset`，或`stty echo`打开echo（`stty -echo`用来关闭echo）
bash里`\[\]`用来表示non-printable字符的开始结束，否则针对过长的命令，会导致bash不能正确显示输入
对应到ascii代码为`\001`和`\002`，在不能使用`\[\]`的情况可以使用这两个，如gdb prompt

### job 管理
jobs/disown/fg/bg/跟作业管理相关，disown解除关系（不再在shell接受到HUP时向该进程发送HUP）
使用时jobspec需要加前缀%
先将作业stop（Ctrl-z）然后bg即可将作业放置后台

### ubuntu开启root的ssh登陆
- sudo passwd root
- sudo passwd -u root
- /etc/ssh/sshd_config中的PermitRootLogin设为yes
- service ssh restart

### LVM: logical volume management
VG: volume group     vg*  vgdisplay/vgextend等命令
PV: physical volumn  pv*  pvdisplay/pvextend等命令
LV: logical volumn   lv*  lvdisplay/lvextend等命令
LV上扩展fs   resize2fs
空间分配时首先需要将物理分区添加到PV，然后将PV加到VG中，然后LV从VG中申请空
    间，之后在LV上创建文件系统，但PV一旦放到VG中，再更改大小是不会显现的，
    可以添加新的PV
PV必须时Linux LVM类型的文件系统，为主分区，使用fdisk设置t为8e
这种方式只能在已经使用LVM的文件系统上，如果一开始不是，只能新创建一个文件系统，然后
    mount到对应位置，当然如果磁盘上当前分区后面有连续空间，应该是能直接扩展的

### centos下设置static ip
ip,mask,类型：/etc/sysconfig/network-scripts/ifcfg-eth0
gateway：/etc/sysconfig/network
DNS: /etc/resolv.conf
修改后执行/etc/init.d/network restart

### PrivateTmp
httpd无法访问/tmp目录下的文件，提示找不到，但是文件是存在的
原因：由于安全问题，`systemd`可以为httpd配置PrivateTmp，即在/var/tmp下生成独立的/tmp文件夹
将/usr/lib/systemd/system中有关httpd的PrivateTmp设为false，然后systemctl daemon-reload
即可关闭该选项

### 时间与时区
/etc/localtime  centos下使用该文件控制时区，需要从/usr/share/zoneinfo/拷贝或ln过来以更改时区
/etc/sysconfig/clock
/etc/timezone
/usr/share/zoneinfo/
更新时间 ntpdate time.windows.com
查看主机时间是否存在误差timedatectl status（老的系统版本不自带）

### grub
在ubuntu15.04中使用text模式
- /etc/default/grub  `GRUB_CMDLINE_LINUX_DEFAULT="text"`
- sudo update-grub
- 对使用systemd（Ubuntu 15.04）的系统还要禁用graphical login manager:
    - sudo systemctl enable multi-user.target --force
    - sudo systemctl set-default multi-user.target

### 自启动服务
SystemV：update-rc.d(ubuntu)/chkconfig(centos)
- 在/etc/rc.d目录创建/etc/init.d的链接
- `[KS][number]xxxxxx`  K kill, S start, number为优先级

Upstart：使用initctl
- /etc/init/service.conf和/etc/init.service.override

systemd：使用systemctl
- /etc/systemd/system/multi-user.target.wants/service.service
- 然后enable一下：systemctl enable service.service

ubuntu从6.10启用upstart，15.04启用systemd
`service`脚本可用来控制SystemV（有些版本也支持upstart服务，但是`--status-all`只显示SystemV的）

### chroot
chroot时/etc/bashrc没被读取，但是~/.bashrc被读取了

chroot时提示找不到/bin/bash，实际为该程序的ld.so不存在
chroot环境下不会自动创建dev设备，如果某程序需要，可自行创建，或者使用mount bind宿主机的dev
- mknod -m 0666 dev/null c 1 3
- mknod -m 0666 dev/random c 1 8
- mknod -m 0444 dev/urandom c 1 9
- mount -bind /dev /mnt/newroot/dev

查看是否chroot：/proc/<pid>/root，值为/表示没有chroot
chroot为/a/b/c后的进程A，如果连接/etc/file.sock 进程B监听/a/b/c/etc/file.sock这样是可以正常连接的

### ssh
-f可以让ssh在执行命令前进入后台，但这样本地会多出一个ssh进程
`ssh  root@10.128.6.234 'sleep 300&'`会导致本地stuck，因为stdout还与远端的ssh保持连接中，使用nohup同样会保持stdout因此也不行
`ssh  root@10.128.6.234 'sleep 300 2>/dev/null &'`本地也会stuck
`ssh  root@10.128.6.234 'sleep 300 >/dev/null &'`可断开

远程运行locust（python脚本）时必须同时重定向stderr，否则程序起不来，原因未知

互信登陆只需要编写~/.ssh/authorized_keys就可以
