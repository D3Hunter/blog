清除linux缓存echo 3 > /proc/sys/vm/drop_caches
DistroWatch可查看个linux/bsd发行版携带的软件版本情况，及其他各类信息
getenforce/setenforce控制SELinux，centos默认开启，ubuntu默认关闭
yum install lrzsz
atyle --style=kr --mode=c -H 格式化代码
`yum provides \*/Intrinsic.h` 查看哪个package提供了对应的头文件
ubuntu系统下使用如下：
- `apt-get install apt-file; apt-file update`
- `apt-file find Python.h`

DMI Desktop Management Interface; SMBIOS, System Management BIOS

grep和awk默认都是有缓冲的，要立即显示使用如下参数：
`top -bp $pid -d 5 | grep --line-buffered 'python' | awk -W interactive '{print $9}'`
top默认会接受来自stdin的指令，在脚本中将其输出到文件时会报错`failed tty get`, 添加`-b`切换到batch mode

awk计算sum有精度限制，此时可以使用`bc`（`paste`生成表达式）来计算：`cat numbers.txt | paste -sd+ | bc -l`

获取ip地址：`ifconfig | sed -En 's/127.0.0.1//;s/10\.//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'`

rsync - a fast, versatile, remote (and local) file-copying tool. rsync会对比src和dst之间的差别，并只拷贝变动的部分。

文件按行长度排序: `cat testfile | awk '{ print length, $0 }' | sort -n -s | cut -d" " -f2-`

### IUS
IUS repository：提供最新的package，yum内原有的包仍然可以安装

IUS的原则是不覆盖原stack的package，IUS的package命名规则为: `{name}{major_version}{minor_version}u`

centos 安装 git2.X 示例：
``` shell
$ sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
$ sudo yum erase git
$ sudo yum install epel-release 
$ sudo yum install git2u
```

### file read/import progress
pv -f xxx.sql 2> output.log | mysql -uroot -proot test

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

### 查看当前系统是否为虚拟机：
常用的虚拟机：VMWare、KEmu、KVM、Microsoft VirtualPC、Xen（HVM domU）、Virtuozzo
- dmidecode -t system / dmidecode -s system-product-name
- lshw -class system
- /sys/class/dmi/id/sys_vendor
- lspci
- dmesg |grep DMI  / dmesg |grep Hypervisor
### NFS有两种挂载方式：
硬挂载将模拟本地磁盘，在IO操作未完成前一直阻塞（这在NFS服务器出问题时会导致应用hang）
软挂载

### 创建新文件系统
非交互式创建`echo "n\np\n1\n\n\n\nw" | fdisk /dev/vdb; mkfs.ext4 /dev/vdb`

### linux
kill: If sig is 0, then no signal is sent, but error checking is still performed; this
can be used to check for the existence of a process ID or process group ID.

`auditd`  is  the userspace component to the Linux Auditing System
`inotify` inode notify
`/proc/sys/kernel/core_pattern`, `man core`配置coredump生成
配置内核参数 `/etc/sysctl.conf`

sed 换成回车
sed 's/,/\
/g'

`setuidgid` - runs another program under a specified account’s uid and gid.
Bochs 类似kvm／zen/QEMU
`pidof` -- find the process ID of a running program.
`/proc/pid/stat`中包含ppid
#### supervise
`svc` - controls services monitored by `supervise`(8)
`supervise` - starts and monitors a service.
`supervise s`
`supervise`  switches  to  the  directory named `s` and starts `./run`. It restarts `./run` if `./run` exits. It pauses for a second after starting `./run`, so that it does not loop too quickly if `./run` exits immediately.
`supervise` maintains status information in a binary format inside the directory `s/supervise`, which must be writable to `supervise`.  The status information can be read by  `svstat`
`auditd`  is  the userspace component to the Linux Auditing System. It’s responsible for writing audit records to the disk.
`audispd`  is  an  audit  event multiplexor(dispatcher). It has to be started by the audit daemon in order to get events. It takes audit events and distributes them to child programs that want to analyze events in realtime.

### creating swap file
- dd if=/dev/zero of=/swapfile bs=1024 count=65536
- mkswap /swapfile
- swapon /swapfile
- cat /proc/swaps

### audit
记录系统内的操作
- 添加audit：`auditctl -w /etc/shadow -k shadow-file -p rwxa`
    - 监控rwxa操作
    - `-w`监控的文件名
    - `-k`指定日志中显示的key
- 查看记录：`ausearch -f /etc/passwd`

