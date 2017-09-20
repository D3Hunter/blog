加tag，类似rename：docker tag d583c3ac45fd myname/server:latest
如果从scratch创建docker image需要该程序静态链接或者自行安装依赖
sudo docker build -t myrepo:getcpu .  前面是repository后者为tag，需要当前目录下有Dockerfile
docker rm 删除container，-f
docker run -d -p 80:80 nginx-1.9.1:latest
`Registry` 存放一系列镜像
`repository` 存放某一类镜像的各个tag
`docker command`的执行由用户提交传递给`docker daemon`，而-H指定的就是这个命令提交地址, 使用`docker search [ip/host]/term`搜索时，实际链接的-H的地址，然后转给daemon
`docker ps -f "status=exited" | awk 'NR>1{print $1}' | xargs docker rm -f` 删除已经结束的container
`docker ps -a |tail -n +2 | awk '{print $1}'| xargs -I{} docker rm {}` 删除所有的container
`Ctrl+p+q`从attach的container中退出
`docker export adoring_kowalevski > contents.tar`对于不带sh/bash的可以这样查看文件.但一般都会带sh，或者sh的符号链接
docker ps -a仍然会显示exited的container，需要手动删除（为啥不直接删掉），`加上–rm可以自动删除`
`docker pull`未下载完的image无法删掉，重启docker
处于exit状态的container可以看logs
docker exec执行bash，就算以root登陆，仍然没有root权限，需要添加`--privileged`
docker cp <containerId>:/file/path/within/container /host/path/target

cpu/memory分别在`/proc`系统下的`cpuacct.stat/memory.stat`，dockerAPI也可用top获取

### docker and vagrant
Provisioner - is something doing provision - in docker installing, running, pulling containers.
Provider - is something that runs the VM. I.e. VBox runs the ubuntu OS image.
docker and vagrant, They are very much complimentary.

### 镜像相关
busybox
    busybox的find、sed功能都很弱
docker执行httpd报bad user name，但是这个user在passwd和group里面都有，为什么？？
    将/etc/nsswitch.conf中passwd和group配置为files，该配置依赖libnss_files.so.2
    这样就可以正确读取，配置为compat不行
docker container运行时，dev/proc/sys会自动创建，不需要包含在image中，如果使用chroot
    测试image的依赖，可以临时创建
ADD可以将压缩文件作为image的目录结构
ENV可以设置container的环境变量，如PATH
WORKDIR设置container工作目录
`CMD`会被覆盖，`ENTRYPOINT`不会
docker run需要`foreground进程`保持运行，否则整个container都会结束，可以使用supervisor
- 或者使用bash循环保持在foreground
- -e指定环境变量

### docker network
bridge 即docker0，不支持自动服务发现
none：无网络连接
host：跟host一样
docker run通过--net指定network，默认为bridge，每个container一个IP
network分为：
- bridge network:当前host可用，可通过expose与其他host通信
- overlay network：支持跨host
docker expose/publish, expose仅是标明我会监听，publish把这个端口绑定到host端
docker container中监听的端口如果不`polish`在host上看不到，在/proc中也看不到
### volumn
docker镜像为一系列`readonly`层，container启动后会在其上创建一个`rw`层
docker将这种ro层之上存在rw层的组合为`Union File System`
为了在container间共享数据，docker使用`volumn`的概念表示UFS之外存在于host的目录或文件
如果不指定--name，volumn在inspect是看不到的，但是可以在container看到volumn
`-v src:dest`可以指定某个host目录
使用docker rm删除exit的container不会自动删除volumn，需要加-v或者启动时使用--rm
### Docker Remote API
unix:///var/run/docker.sock
GET /containers/json?all=1&filters={"status":["running"]}&limit=100 HTTP/1.1
GET /containers/<id>/top?ps_args=-eopmem,pid,comm HTTP/1.1(必须有pid)
GET /containers/<id>/json
GET /images/json
GET /images/search?term=XXX
GET /info

### 添加registry
修改docker.service
ExecStart=添加 --registry-mirror=https://docker.mirrors.ustc.edu.cn
systemctl daemon-reload
systemctl restart docker
### 保持container运行
docker run -d centos tail -f /dev/null
docker run -t -d centos
docker run -td -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root docker.io/mysql:latest
