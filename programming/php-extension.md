编译php报undefined错误，可能是上次make导致，make clean可解决
`php-fpm -t`查看php-fpm.conf位置
`php -i | grep ini`
php-fpm.conf中`pm*`对应管理多少个worker
`php-fpm -R`运行root运行

抽取php-ext的编译依赖，需要修改phpize/php-config中的prefix获取方法（dirname）
`php-ext debug`编译时不带"-g"（可能时设置CFLAGS覆盖掉了）
`Primary script unknown`可能是找不到php脚本，看看nginx中`SCRIPT_FILENAME`是否配置正确
### yii framework
apt-get install libssl-dev
yii2需要mcrypt支持
    安装libmcrypt, libmcrypt-devel
    在php源码目录编译mcrypt：phpize;aclocal;./configure;make
    在php.ini中添加extension=mcrypt.so
yii2 migrate需要使用pdo_mysql，否者报could not find driver
    php编译时的--with-mysql编译的是mysql，两者是不同的
    如果还不行可试试将localhost换成127.0.0.1

### 编译php5.5.34，make install时出现以下问题：
cp: cannot stat `sapi/cli/php.1′: No such file or directory
原因为`configure`生成的php.1在之后的make clean中被删除掉了
因为要在同目录下编译zts和nzts，应在configure前进行make clean
`install-pear-installer] Error 255`原因为上次下载pear包中途中断，导致失败
    删掉重新下载即可

### PHP 源码
`#define APM_G(v) TSRMG(apm_globals_id, zend_apm_globals *, v)`展开后的结果`((zend_apm_globals *) (*tsrm_ls)[apm_globals_id-1])->v`
非zts下的`TSRMLS_C`为空（不需要TSRM），编译时就会出错，所以使用TSRMLS_CC为比较好的选择
TSRM thread-safe-resource-mamagenent; ls local storage
`PHP_` `php_`开头的宏都被设置为对应`ZEND_ zend_`开头的宏
`TSRMLS_*`系列的宏方便同时支持zts和非zts
`zend_execute_data->function_state.arguments`返回的值为参数个数，参数在前面存储
`add_next_index_string`往数组里append
`add_assoc_zval*`类接口调用`zend_symtable_update`，该函数会检查key是否为数字index
`ZEND_DECLARE_MODULE_GLOBALS`声明global变量
- zts  下为： `ts_rsrc_id module_name##_globals_id;`
- 非zts下为： `zend_##module_name##_globals module_name##_globals;`
`ZEND_GET_MODULE`展开后为：
    `ZEND_DLEXPORT zend_module_entry *get_module(void) { return &name##_module_entry; }`
`ZEND_INI_BEGIN()        static const zend_ini_entry ini_entries[] = {`
`REGISTER_INI_ENTRIES() zend_register_ini_entries(ini_entries, module_number`, module_number为startup函数的参数
`sapi_module`、`SG(sapi_headers)`
`AG` alloc global
### PHP/zend下的一些缩写
- SAPI Globals (SG)
- Executor Globals (EG)
- Internal Extension Globals APM_G
- php_core_globals PG
- output globals OG
- BG为扩展basic_functions的全局
- EX execute data
- CG(function_table) compile global
显示某个模块的`PHP_MINFO_FUNCTION`中的内容：`php -$'\x0e' <extension-name>`，这个好像是内部使用的，其参数为不可打印字符14
`SG(request_info).request_method`
