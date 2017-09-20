### extension(mod)  
`apache`有`MMN`，多版本支持需要考虑  
更换模块文件，需要`stop/start`，不能`restart`，否则`httpd`会崩溃  
安装前停止`apache`，否则会有段错误  
多个`sethandler`会冲突，只会执行一个，最后配置的会生效，所以在`fixups`里判断模块名称的方法是不可行的  
每个`vhost`都有一个`server->module_config`，如果`vhost`没有配置，会使用最上层的`module_config`。即，只有一份，调用`merge`时可以创建，但是`merge`只在遇到模块的某个`command`时才会去调用  
  
使用`apr/apr-util`源码时，注意将其内的以往的build文件删除，否则可能会报找不到头文件的问题  