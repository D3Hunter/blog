## Mysql
- `docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=root -p 127.0.0.1:13306:3306 -d mysql:latest`
- root连接：`docker run -it --link test-mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'`
- 普通用户连接：`docker run -it --link test-mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -utest -ptest'`
    - ubuntu下localhost可能绑定到127.0.1.1导致mysql连接不上
- 使用data volume
    - 一旦使用volume，`docker run`时`MYSQL_ROOT_PASSWORD`就不需要指定了，即使用volume内的用户数据
    - `docker create --name test-data test-mysql-data:132412`
    - `docker run --name test-mysql-new --volumes-from=test-data -p 127.0.0.1:13306:3306 -d mysql:latest`
    - 创建数据image Dockerfile：
        FROM busybox
        WORKDIR /var/lib/mysql
        copy mysql /var/lib/mysql
        VOLUME /var/lib/mysql
        CMD ["true"]
