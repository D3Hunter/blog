## Features
- Create stand-alone Spring applications
- Embed Tomcat, Jetty or Undertow directly (no need to deploy WAR files)
- Provide opinionated 'starter' POMs to simplify your Maven configuration
- Automatically configure Spring whenever possible
- Provide production-ready features such as metrics, health checks and externalized configuration
- Absolutely no code generation and no requirement for XML configuration

## misc
- `spring-boot`工程可通过[Spring Initializr](https://start.spring.io/)自动生成
- By default, spring-boot will not look for resources outside the jar file. 比如`logback`配置文件，可通过在`application.properties`设置`logging.config`
- `spring-boot`或者调用`getLocalHost`特别慢，将`hostname`放到`/etc/hosts`中的`127.0.0.1`和`::1`的映射中
- 如果要做一些`logback`的早期初始化操作（如`loggerContext.putProperty`），需要放到`SpringApplication.run()`后面，`SpringApplication.run()`之前也会做一些配置工作，可能会把之前的配置（`static`初始化或者`main`中）冲掉
- `Converter`可用来实现自定义类型转换，如在`application.properties`中`String`到`Date`转换
- `springboot`项目，其`parent`为`spring-boot-starter-parent`，并通过`spring-boot-maven-plugin`生成结果jar
    - `org.springframework.boot`、`org.springframework`和`org.springframework.data`分组下独立发版，版本号相互独立，因此最好使用这种方式以引入正确的依赖版本
- Spring Boot runs `schema-@@platform@@.sql` automatically during startup. `-all` is the default for all platforms.

## dependency tree
`springboot web`项目`package`依赖结构，默认使用`jsckson`
- org.springframework.boot:`spring-boot-starter-web`
    - org.springframework.boot:`spring-boot-starter`
        - org.springframework.boot:spring-boot
        - org.springframework.boot:spring-boot-autoconfigure
        - org.springframework.boot:spring-boot-starter-logging
        - jakarta.annotation:jakarta.annotation-api
        - org.yaml:snakeyaml
    - org.springframework.boot:`spring-boot-starter-json`
        - com.fasterxml.jackson.core:jackson-databind
        - com.fasterxml.jackson.datatype:jackson-datatype-jdk8
        - com.fasterxml.jackson.datatype:jackson-datatype-jsr310
        - com.fasterxml.jackson.module:jackson-module-parameter-names
    - org.springframework.boot:`spring-boot-starter-tomcat`
        - org.apache.tomcat.embed:tomcat-embed-core
        - org.glassfish:jakarta.el
    - org.springframework:`spring-web`
    - org.springframework:`spring-webmvc`
        - org.springframework:spring-aop
        - org.springframework:spring-context
        - org.springframework:spring-expression
- org.springframework.boot:`spring-boot-starter-data-jdbc`
    - org.springframework.boot:`spring-boot-starter-jdbc`
        - com.zaxxer:HikariCP
        - org.springframework:`spring-jdbc`
    - org.springframework.data:`spring-data-jdbc`
        - org.springframework.data:spring-data-relational
        - org.springframework.data:spring-data-commons
        - org.springframework:spring-tx
- org.springframework.boot:`spring-boot-starter-test`

## classes and annotations
- `@SpringBootApplication` shortcut for: `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`
- `@EnableAutoConfiguration`: attempting to guess and configure beans that you are likely to need. Auto-configuration classes are usually applied based on your classpath and what beans you have defined.
    - 该annotation所在类的所在包，会作为一些搜索的默认值，如搜索`@Entity`时
    - 如果有`spring-webmvc`，会自动加载`DispatcherServlet`，自动引入`@EnableWebMvc`
- `SpringApplication`: Class that can be used to bootstrap and launch a Spring application from a Java main method.
    - Create an appropriate `ApplicationContext` instance (depending on your classpath)
    - Register a `CommandLinePropertySource` to expose command line arguments as Spring properties
    - Refresh the application context, loading all singleton beans
    - Trigger any `CommandLineRunner` beans
- `CommandLineRunner`: Interface used to indicate that a bean should run when it is contained within a `SpringApplication`.
- `ApplicationRunner`: Interface used to indicate that a bean should run when it is contained within a `SpringApplication`. 跟前者的区别是，其`run`参数类型为`ApplicationArguments`，而前者为`String[]`
- `RestTemplateBuilder`: Builder that can be used to configure and create a `RestTemplate`. 在`typical auto-configured Spring Boot Application`下是一个可用的`bean`用来创建`RestTemplate`，默认自动选择恰当的`ClientHttpRequestFactory`
- `@ConfigurationProperties`: Annotation for externalized configuration.
    - `ConfigurationProperties`标记的类成员需要有对应的`setter`，否则不会根据`prefix`设置值
- `@EnableConfigurationProperties`: Enable support for `@ConfigurationProperties` annotated beans. 不添加时，对应类是不被当作bean的(也可以添加类似`Component`类的标签，不过不太规范)，对应类需要以参数形式传给`@EnableConfigurationProperties`

## Spring Boot features
### auto-configuration
Spring Boot checks for the presence of a `META-INF/spring.factories` file within your published jar. The file should list your configuration classes under the `EnableAutoConfiguration` key.

### database initialization
Spring-Boot loads SQL from the standard root classpath locations: `schema.sql` and `data.sql`, respectively. In addition, Spring Boot processes the `schema-${platform}.sql` and `data-${platform}.sql` files (if present), where platform is the value of `spring.datasource.platform`. `spring-boot-autoconfigure`的`DataSourceInitializerInvoker.afterPropertiesSet`会做初始化，该类通过`DataSourceAutoConfiguration`引入

