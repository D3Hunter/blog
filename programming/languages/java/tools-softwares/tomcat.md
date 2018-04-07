查看servlet API版本：servlet-api.jar中META-INF/MANIFEST.MF
应用可以目录结构存在，也可以为Web ARchive, or WAR file
    WEB-INF中存放应用相关数据classes/lib/web.xml

$CATALINA_HOME/common/lib为应用与tomcat同享
$CATALINA_BASE/shared/lib应用间共享
/META-INF/context.xml: can be used to define Tomcat specific configuration options

开启manager-ui，在`tomcat-users.xml`中添加
    <role rolename="manager-gui"/>
    <user username="admin" password="admin" roles="manager-gui"/>
