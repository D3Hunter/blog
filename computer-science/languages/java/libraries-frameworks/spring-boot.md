Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run".

By default, `Spring` will not look for resources outside the jar file. If you want to use an external logback configuration file, you must pass it's location when starting the jar: `-Dlogging.config=logback-spring.xml`

spring-boot或者调用`getLocalHost`特别慢，将`hostname`放到`/etc/hosts`中的`127.0.0.1`和`::1`的映射中

如果要做一些`logback`的早期初始化操作（如`loggerContext.putProperty`），需要放到`SpringApplication.run()`后面，`SpringApplication.run()`之前也会做一些配置工作，可能会把之前的配置（static初始化或者main中）冲掉

`ConfigurationProperties`标记的类成员需要有对应的`setter`，否则不会根据`prefix`设置值

### Features
- Create stand-alone Spring applications
- Embed Tomcat, Jetty or Undertow directly (no need to deploy WAR files)
- Provide opinionated 'starter' POMs to simplify your Maven configuration
- Automatically configure Spring whenever possible
- Provide production-ready features such as metrics, health checks and externalized configuration
- Absolutely no code generation and no requirement for XML configuration
