### linux
`/proc/pid/statm`,`/proc/pid/stat`,`/proc/pid/status`查看pid的内存、user、sys时间等信息；cpu利用率可通过`(user + sys) / clock`获得
`/proc/<pid>/cgroup`查看进程所在cgroup（里面的路径是相对于挂载点的
`/proc/<pid>/smaps`可获得进程内存占用的PSS指标
查看进程的线程个数，`ps -eo nlwp`或者`/proc/pid/task`或者`/proc/pid/status`
已打开的文件列表`/proc/<pid>/fd/`，进程限制`/proc/<pid>/limits`
`pctrl`可修改进程的`/proc/pid/comm|stat`中的名称，`/proc/pid/cmdline`需要修改argv[0]
`/proc/pid/fd`中socket中的数为inode，使用该inode可以在`/proc/net/[tcp|udp|unix]`中寻找该socket的详细信息,有些可能使用的ipv6

`/proc/diskstats` 2.6的内核可通过该文件获取磁盘利用情况（3以上的内核貌似沿用了2.6的设置）
`/prpc/net/dev` 网络信息
读取/proc中的数字目录数获取进程信息

`grep cgroup /proc/mounts`查看cgroup挂载点
`/proc/cgroups`列出cgroup子系统
每个container都会有一个cgroup，对LXC名称为`lxc/<container_name>`，老版本是
    <container_name>；对docker为`/docker/<longid>/`
cgroup的内存占用需要在内核中开启`cgroup_enable=memory swapaccount=1`
内存信息在`memory`，cpu在`cpuacct`，时间单位为`USER_HZ`，为当前已用

目前检测内核`thread`的方法：
- kthreadd (PID 2) has PPID 0 (on Linux 2.6+)
- `/proc/*/exe`为空
- `/proc/*/cmdline`空 ，used by ps and top to distinguish kernel threads.

磁盘信息可用`statvfs/statfs`获取
vmstat -Sn --stats查看memory,swap,io, etc..

free中的-+部分，对应实际占用
查看sector size：`sudo hdparm -I /dev/sda | grep -i physical`或`sudo fdisk -l`
df -T 查看文件系统类型
fdisk -l查看所有物理分区
fuser file_name  查看谁在使用某个文件

### windows
基本上Windows上所有可监控数据都可通过`Performance Counter`获取(具体看`perfmon`)

`GlobalMemoryStatusEx` 内存和交换分区（page file）使用
`GetDiskFreeSpaceEx` 获得磁盘信息
磁盘利用通过`RegQueryValueEx（HKEY_PERFORMANCE_DATA`获取，获得的数据为：`Performance Data Format`
使用`counter-index 200/202/204`来获取磁盘利用%也可以（地址是相连的部分，值相
    同），但该值有多个COUNTER（后一个为base-counter，辅助计算），还是
    使用1400/1402/1404来获取
`windows-performance-counter`是18-digit Active Directory timestamps, also named 'Windows NT time format' and 'Win32 FILETIME or SYSTEMTIME'. The timestamp is the number of 100-nanoseconds intervals since Jan 1, 1601 UTC.
Impersonation and Delegation
网络数据可通过`GetAdaptersInfo`和`GetIfEntry`获得，但`MIB_IFROW`为32需要处理溢出, 如果要更好的处理可以通过`Performance Counter`
使用`GetAdaptersInfo`获得的name为内部名称，`IP_ADAPTER_ADDRESSES`可得到`friendlyName`
