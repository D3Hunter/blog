### VirtualBox
virtual box安装ubuntu花屏,重新切换图形显示
`sudo apt-get install virtualbox-guest-dkms`重启以支持更高分辨率
virtualbox用`nat`连接网络需要做端口转发以登陆进去，或使用`bridged network`，获得本地局域网的ip
`GRUB_CMDLINE_LINUX_DEFAULT=" quiet splash"`改成`“text”`就不再启动X，可以手动执行`startx`来启动图形化
VBoxManage list vms
VBoxHeadless -s <Guest-OS-Name>

获得桥接网卡且headless运行host的ip地址
1. for i in {1..254}; do ping -c 1 192.168.178.$i & done
2. VBoxManage list runningvms
3. VBoxManage showvminfo <vmname>
4. arp -a | grep <vmname-mac-addr>

VBoxManage modifyhd ".......vdi" --resize 81920 设置硬盘大小

### sublime：
"rulers": [80, 120]设置ruler

### 抓包
使用`tshark -q -r input.pcap -z follow,tcp,ascii,$stream > $stream.txt`
所得为ascii数据，所有非可见字符都使用'.'(0x2E)填充，并非原始数据，因此解压不
了，使用`tcpflow`获得的为二进制数据，可以正常解压。使用follow,tcp,hex或者
follow,tcp,raw获取的数据都是转成hex的，非原始二进制数据，因此都解压不了

`tcpdump -w xpackets.pcap -i eth0 dst 50.31.164.226 and port 80`
    这样只能抓发往50.31.164.226:80的数据，但是response收不到
    要抓response不要指定端口，但这样会把所有的流量都抓住
`tcpdump -tttt -r data.pcap`读取已经抓的包
`tcpflow`能把`.pcap`的http包分析出来
`tcpflow/tcpdump`都是使用`libpcap`，expression的格式是一样的：expression有一系列primitives组成，通常的primitive包含id和多个前缀qualifiers, qualifiers包含type/dir/proto，但也有复杂的primitive
- -l Make stdout line buffered
- -A Print each packet (minus its link level header) in ASCII
- -i 指定interface，默认使用‘lowest numbered’
- -n Don't convert host addresses to names
- -X 打印数据in hex and ASCII


### curl
`curl --unix-socket` 7.40以后支持
`curl: (48) An unknown option was passed in to libcurl`，curl正确，但libcurl版本不正确，使用ldd看看是否使用了正确的libcurl库
curl默认使用`strlen`计算`content-length`，如果想发送binary，需要使用`CURLOPT_POSTFIELDSIZE`
curl的`proxy username/password`仅需要对':'做encode。

编译带ssl的curl:
1. `./configure LIBS=-ldl --prefix=/root/code/curl64 --with-ssl=/root/code/openssl64/`
2. --disable-ldap --without-libidn --enable-shared=no
3. disable-ldap后configure报找不到ssl，其实是没有加-ldl，一定要使用disable-ldap
4. 使用without-ldap，在curl发现有系统库后仍会使用ldap

`ignore_expect_100` on不然带expect的报The requested URL could not be retrieved
这个不管用server_http11 on
这个问题应是由于curl默认使用HTTP/1.1导致的，下版改成HTTP/1.0

`CURLOPT_SSL_VERIFYPEER` 是否verify perr的certificate

### Automatic Bug Reporting Tool, commonly abbreviated as ABRT
abrt会收集bug crash，生成core文件，但仅收集yum安装的包，设置`/etc/abrt/*.conf`中的`ProcessUnpackaged = no`可以允许其他程序生成core（因为abrt会接管系统的core生成）abrt运行时，`sysctl -a|grep core_pattern`，以'|'开头

进程崩溃后会写core文件，并在`/var/log/messages`里写入信息
对于`“Package 'jdk' isn't signed with proper key“`，需要：
1. Edit the file /etc/abrt/abrt-action-save-package-data.conf
2. Set OpenGPGCheck = no
3. Reload abrtd with the command: service abrtd reload

### jenkins
使用windows部署jenkins，需要能通过PATH找到git，并能让git使用.ssh无密码访问代码库
git会在HOME目录下寻找.ssh，如果没有设置回事系统默认值（这个默认值在windows上未知）

jenkins中配置发送html邮件，主要有些子配置如果更改了默认邮件类型，需要单独配
