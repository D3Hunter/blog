查看servlet API版本：servlet-api.jar中META-INF/MANIFEST.MF
应用可以目录结构存在，也可以为Web ARchive, or WAR file
    WEB-INF中存放应用相关数据classes/lib/web.xml

$CATALINA_HOME/common/lib为应用与tomcat同享
$CATALINA_BASE/shared/lib应用间共享
/META-INF/context.xml: can be used to define Tomcat specific configuration options

设置线程池最大线程数：`server.xml`中的`maxThreads`
### 开启manager-ui，在`tomcat-users.xml`中添加
    <role rolename="manager-gui"/>
    <user username="admin" password="admin" roles="manager-gui"/>

### One or more listeners failed to start
1. In your `WEB-INF/classes` directory of the application, make a new file: `logging.properties`.
2. Add the following in that file:
```
org.apache.catalina.core.ContainerBase.[Catalina].level=INFO
org.apache.catalina.core.ContainerBase.[Catalina].handlers=java.util.logging.ConsoleHandler
```
3. Restart tomcat.

### 启动太慢：Creation of SecureRandom instance for session ID generation using [SHA1PRNG] took [5172] milliseconds.
- `-Djava.security.egd=file:/dev/./urandom`
- [reference][https://wiki.apache.org/tomcat/HowTo/FasterStartUp]

