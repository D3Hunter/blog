`configure httpd`提示找不到libxml2，`--with-libxml2=/usr/`后成功

`httpd -l`显示内置module，MPM也是内置module之一
`apachectl -k graceful`  或者  `/etc/init.d/httpd reload`

AP_MPMQ_MAX_DAEMONS：最多能启动的daemons个数，prefork下等于MaxRequestWorkers
apr_table_setn(r->headers_out,
ap_set_content_type
ap_get_loadavg

hook的执行应该是循环跑的，需要hook自己去检查r->handler是否为自己

`ap_run_mpm`
`AP_IMPLEMENT_HOOK_RUN_FIRST(int, mpm,`

restart一次，generation就会递增。Apache里的restart应该等同于reload
这两个generation有什么区别, 后者初值为0
Parent Server Config. Generation: 2
Parent Server MPM Generation: 1

The per-server config is kept on the `server_rec`, of which there is one for each virtual host,
created at server startup. The per-directory config is kept on the `request_rec` and may be
computed using the merge function for every request.

设置request内的variable，类似于nginx中的ctx
```
my_request_vars* vars = apr_palloc(r->pool, sizeof(my_request_vars)) ;
/* store stuff in vars */
ap_set_module_config(r->request_config, &my_module, vars) ;
```

and retrieve what we set later in the request:
`my_request_vars* vars = ap_get_module_config(r->request_config, &my_module) ;`
The `conn_rec` has an analagous `conn_config` field. Apache provides other contexts that may be
useful for some applications: each filter and namespace has a context field for its own data.
These topics will be the subjects of separate articles.

the request pool, with the lifetime of an HTTP request.
the process pool, with the lifetime of an server process.
the connection pool, with the lifetime of a TCP connection.
the configuration pool

### hook
`ap_hook_fixups` Last chance to look at the request before content generation.该hook可以在存在proxy时对request进行修改，`ap_hook_handler`不行
#### ap_hooks.h ：一般的创建hook的方式
声明：`AP_DECLARE_HOOK`等，定义`ap_hook_*`和`ap_run_*`和`ap_hook_get_*`等函数
实现：`AP_IMPLEMENT_HOOK_VOID`等，实现上面的三个函数
#### `apr_optional_hooks.h` `mod_status`使用的该hook方式
这种方法不存在`ap_hook_*`式的hooking方法，需要使用`APR_OPTIONAL_HOOK`
mod_info里包含了内置的所有hook
`AP_DECLARE_HOOK`
`APR_DECLARE_EXTERNAL_HOOK`
`APR_IMPLEMENT_OPTIONAL_HOOK_RUN_ALL`
`ap_hook_handler`函数也是通过上面的的宏定义的
`AP_IMPLEMENT_HOOK_RUN_FIRST`

### filter
apache里的filter需要先`ap_register_output_filter`，然后在`insert_filter`里
`ap_add_output_filter`，这种方式filter会被执行多次，需要在filter函数里把自己去掉`ap_remove_output_filter`
为什么会执行多次？
每次都需要在insert_filter里添加才能执行？add跟request相关

apache程序内并不设置`NOFILE`，但可以在apachectl脚本里设置

httpd进行两段config
各MPM的 `*_pre_config`使用retain数据，只有`retained->module_loads`开始进行fork
    main.c调用了两边`ap_run_pre_config`只在第二次开始fork

`apr_pool_userdata_set`、`apr_pool_userdata_get`

`ap_hook_open_logs`阶段传入的`Server_rec`为最外层，即`process`级别的，并非每个`virtualhost`创建一个

`.htaccess`里可以添加httpd配置,在不修改`httpd.conf`的情况下更改应用配置，比如`RewriteRule`, 这样会影响效率
### 配置项
`ServerLimit/ThreadLimit`： `MaxRequestWorkers`的可配上限，需要完全stop才可更改
`StartServers`: 启动的进程数
`MaxRequestWorkers`: 同时处理的request数上限，不同MPM表达的含义略不同. apache 2.4可用，2.2中为MaxClients
`MaxClients`：同上
`MaxConnectionsPerChild`：每个process可处理的连接数上限，超过后退出

### Multi-Processing Module (MPM)
- worker
    a hybrid multi-threaded multi-process web server
    ThreadsPerChild/MinSpareThreads/MaxSpareThreads
- event
    A variant of the worker MPM with the goal of consuming threads only for
        connections with active processing
    --with-mpm=event来启用
    优化Keep-alive的情况
    这个有点类似多线程式的Nginx
- prefork
    non-threaded, pre-forking web server
    MinSpareServers/MaxSpareServers
- mpmt_os2
- mpm_winnt
### extension(mod)  
`apache`有`MMN`，多版本支持需要考虑  
更换模块文件，需要`stop/start`，不能`restart`，否则`httpd`会崩溃  
安装前停止`apache`，否则会有段错误  
多个`sethandler`会冲突，只会执行一个，最后配置的会生效，所以在`fixups`里判断模块名称的方法是不可行的  
每个`vhost`都有一个`server->module_config`，如果`vhost`没有配置，会使用最上层的`module_config`。即，只有一份，调用`merge`时可以创建，但是`merge`只在遇到模块的某个`command`时才会去调用  
  
使用`apr/apr-util`源码时，注意将其内的以往的build文件删除，否则可能会报找不到头文件的问题  
