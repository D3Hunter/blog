DriverManager会通过`jdbc.drivers`获取driver class，从jdbc4.0还会通过SPI获取driver，如果驱动支持spi可不在需要`Class.forName`
DriverManager通过SPI读取driver是在`<clinit>`中做的，tomcat会在应用加载前加载该类，如果driver是在应用classpath，那么是加载不到的
每个driver在加载时需要创建一个自身的instance并注册到DriverManager，意味着可以通过`Class.forName("foo.bar.Driver")`来注册
无论Drivermanager还是DataSource，底层都是通过Driver来创建Connection

`ResultSet`列从1开始

### connection pooling
- HikariCP
- BoneCP
- Tomcat connection pooling
- DBCP
- c3p0
