## Features
- Dependency Injection
- Aspect-Oriented Programming including Spring's declarative transaction management
- Spring MVC and Spring WebFlux web frameworks
- Foundational support for JDBC, JPA, JMS

## Spring Configuration Metadata
- XML based configuration file.
- Annotation-based configuration
- Java-based configuration

## dependency injection method
- Constructor-based
- Setter-based
- it is a good rule of thumb to use constructor arguments for mandatory dependencies and setters for optional dependencies.

## AOP
- `Aspect`: an aspect is scattered or tangled as code, making it harder to understand and maintain
- `Join point`: This represents a point in your application where you can plug-in AOP aspect
- `Advice`: This is actual piece of code that is invoked during program execution by Spring AOP framework.
    - Before/After/After-returning/After-throwing/Around
- `PointCut`: This is a set of one or more joinpoints where an advice should be executed.
- `Introduction`: An introduction allows you to add new methods or attributes to existing classes.
- `Target object`: The object being advised by one or more aspects, this object will always be a proxied object. Also referred to as the `advised object`.
- `Weaving`: Weaving is the process of linking aspects with other application types or objects to create an `advised object`. This can be done at `compile time`, `load time`, or at `runtime`.

## misc
- 如果使用`annotation`来注册`bean`，则默认会使用`class name`或`method name`做为`bean name`，如果两个类或方法同名，一般会提示bean name conflict。但遇到过以下情况，不会提示：@`SpringBootApplication`标记的`main`类名称为`Application`，扫描的包里有个`@Configuration`标记的类也叫`Application`。原因是`ClassPathBeanDefinitionScanner.checkCandidate`时，把这俩`bean`当成`compatible`的了，而被忽略，这个机制好像跟spring测试有关，暂不确定
- 基于classpath扫描bean的类`ClassPathScanningCandidateComponentProvider.scanCandidateComponents`
- bean defined later is the one which is finally instantiated by the Spring container. 但这两个bean需要用同样的方式定义，即都使用`xml`定义或都使用`@Configuration`定义
- controller方法返回`Callable`可以异步处理请求，`container-thread-A`返回callable后结束, 处理由另外的线程进行，最后由`container-thread-B`返回结果
    - use case: 请求要求结果且需要时间来计算结果，为避免用光container的线程池，提高吞吐, 内部使用`request.startAsync()`(`servlet 3`提供该功能)
    - 这种跟`@Async`是不同的
- 对于singleton的bean(默认都是), 且不是`lazy init`(默认为`eager init`)，那么当`context`启动后就会创建
    - 由于上面的一点，可以使用`@PostConstruct`来执行一些特定代码，也可以用属性`init-method`, 相比起来，前者更方便
- `Bean definition profiles`根据环境配置bean,嵌套的beans配置需要放到后面
    可通过context-param: `contextInitializerClasses`来配置profile功能的初始化
    系统属性`spring.profiles.active`可用来配置哪个profile为active，也可编程设置
- `PropertiesLoaderUtils`读取property配置文件
- `Velocity` and `FreeMarker` are two templating languages that can be used as view technologies within Spring MVC applications. 此外还有`Thymeleaf`
- bean生命周期管理方式：
    - `InitializingBean`/`DisposableBean`分别调用`afterPropertiesseSet`/`destroy`
    - `JSR250`提供了`PostConstruct`和`PreDestroy`，这种方式不依赖Spring, 这种方式比前者优先级更高

## classes and annotations
- `@Configuration`: Indicates that a class declares one or more `@Bean` methods and may be processed by the Spring container to generate bean definitions and service requests for those beans at runtime
- `@ComponentScan`: 默认扫描annotation所在类的所在包，递归搜索
    - search all classes having `@Component` or its sub types like `@Controller`
- `@RestController` shortcut for: `@Controller` and `@ResponseBody`
    - Types that carry this annotation are treated as controllers where `@RequestMapping` methods assume `@ResponseBody` semantics by default.
- `@ResponseBody` Annotation that indicates a method return value should be bound to the web response body
    - 如果是`ResponseEntity`则会将其转为对应的response body，此时如果是mvc的`@Controller`则该annotation多余
    - 默认`MappingJackson2HttpMessageConverter`将返回值转为HTTP response
- `@Controller`: Indicates that an annotated class is a "Controller" (e.g. a web controller).
    - This annotation serves as a specialization of `@Component`
- `@Service`:
    - Indicates that an annotated class is a "Service", originally defined by Domain-Driven Design (Evans, 2003) as "an operation offered as an interface that stands alone in the model, with no encapsulated state."
    - May also indicate that a class is a "Business Service Facade" (in the Core J2EE patterns sense), or something similar. This annotation is a general-purpose stereotype and individual teams may narrow their semantics and use as appropriate.
    - This annotation serves as a specialization of `@Component`
- `@Scheduled`: Annotation that marks a method to be scheduled.
    - Processing of `@Scheduled` annotations is performed by registering a `ScheduledAnnotationBeanPostProcessor`. This can be done manually or, more conveniently, through the `<task:annotation-driven/>` element or `@EnableScheduling` annotation.
- `@EnableScheduling`: Enables Spring's scheduled task execution capability, similar to functionality found in Spring's `<task:*>` XML namespace.
- `RestTemplate`: Synchronous client to perform HTTP requests, 目前推荐使用`WebClient`。springboot下可用`RestTemplateBuilder`创建
    - 底层HTTP client libraries支持`JDK HttpURLConnection`, `Apache HttpComponents`, and `others`. 通过`ClientHttpRequestFactory`
- `JdbcTemplate`: `This is the central class in the JDBC core package`. It simplifies the use of JDBC and helps to avoid common errors. It executes core JDBC workflow, leaving application code to provide SQL and extract results.
    - spring支持嵌入式数据库H2，并自动创建连接
- `@ExceptionHandler`: Annotation for handling exceptions in specific `handler classes` and/or `handler methods`. 支持的参数和返回方法参考javadoc
- `@Bean`: Indicates that a method produces a bean to be managed by the Spring container.
- `ResponseEntity`: Extension of HttpEntity that adds a `HttpStatus` status code. Used in `RestTemplate` as well `@Controller` methods.
- `MvcUriComponentsBuilder`: Creates instances of `UriComponentsBuilder` by pointing to `@RequestMapping` methods on Spring MVC controllers. 可基于mvc的handler元信息构建uri
- `RedirectAttributes`: controllers can use to select attributes for a redirect scenario.
    - `Attribute`可在URI中使用，`FlashAttribute`可在view中使用
- `@RequestParam`: Annotation which indicates that a method parameter should be bound to a `web request parameter`.（spring-mvc下包括`query parameters`, `form data`, and `parts in multipart requests`）
- `@PathVariable`: Annotation which indicates that a `method parameter` should be bound to a `URI template variable`. Supported for `@RequestMapping` annotated handler methods.
- `MultipartFile`: A representation of an uploaded file received in a multipart request.
    - The file contents are either stored in memory or temporarily on disk.
    - The temporary storage will be cleared at the end of request processing.
- `@EnableWebMvc`: Adding this annotation to an `@Configuration` class imports the Spring MVC configuration from `WebMvcConfigurationSupport`
- `@EnableJms`: enables detection of `@JmsListener` annotations on any `Spring-managed bean` in the container.
- `@Transactional`: Describes a transaction attribute on an individual method or on a class.
    - At the class level, this annotation applies as a default to all methods of the declaring class and its subclasses.
- `@Async`: Annotation that marks a method as a candidate for `asynchronous` execution. 跟scheduled task类似在单独的线程内执行
- `@EnableAsync`: Enables Spring's asynchronous method execution capability, similar to functionality found in Spring's `<task:*>` XML namespace.
- `@ModelAttribute`: Annotation that binds a method parameter or method return value to a named model attribute, exposed to a web view.
- `@EnableCaching`: Enables Spring's annotation-driven cache management capability
- `@Cacheable`: Annotation indicating that the result of invoking a method (or all methods in a class) can be cached.
- `@Scope` 指定bean的scope，默认为singleton，prototype为每次都重新申请，其他的还有request，session，globalsession, singleton为per `ApplicationContext`，application为per `ServletContext`
- `ApplicationContext`本身可作为`ResourceLoader`
    - 传给它的参数默认会按照context的类型创建对应的`Resource`，但可以指定prefix来覆盖默认行为，如：`classpath:/file:/http:`
- `Environment`负责profiles和properties
    - 对于Properties通过一系列的`PropertySource`来进行
    - 默认的`StandardEnvironment`包含两个PropertySource，一个是JVM系统属性(`System.getProperties(`))，一个是系统环境变量(`System.getEnv()`), 前者优先级更高
    - 配置中${xxx}都是从`Environment`中获取的


## XML Schema-based configuration
XML Schema-based configuration支持使用namespace的格式, 支持对配置文件扩展：Extensible XML authoring，用户自定义schema
- Authoring an XML schema to describe your custom element(s).
- Coding a custom `NamespaceHandler` implementation (this is an easy step, don’t worry).
- Coding one or more `BeanDefinitionParser` implementations (this is where the real work is done).
- Registering the above artifacts with Spring (this too is an easy step).
    - `META-INF/spring.handlers`
    - `META-INF/spring.schemas`

When using XML-based configuration metadata, you use the `'id'` or `'name'` attributes to specify the bean identifier(s).

## spring-context
- `@Import`: Indicates one or more component classes to import — typically `@Configuration` classes.
    - `mybatis-spring`的`@MapperScan` import 了`ImportBeanDefinitionRegistrar`
- `ImportBeanDefinitionRegistrar`: Interface to be implemented by types that register additional bean definitions when processing `@Configuration` classes....classes of this type may be provided to the `@Import` annotation.
    - `mybatis-spring`的`MapperScannerRegistrar`实现了该接口，并注册了`MapperScannerConfigurer`，该类会做实际的scan，由于`Mapper`类没有什么特殊的标记，该类实际上会把所有的`interface`都加进来

## spring-data
`Spring Data`’s mission is to provide a familiar and consistent, Spring-based programming model for data access while still retaining the special traits of the underlying data store. 常见的data store都有

- `JdbcTemplate`
- `RedisTemplate`: Helper class that simplifies Redis data access code.
- `StringRedisTemplate`: String-focused extension of `RedisTemplate`.

## spring-hateoas
- Hypermedia as the Engine of Application State (`HATEOAS`)
    - With `HATEOAS`, a client interacts with a network application whose application servers provide information dynamically through `hypermedia`.
- `WebMvcLinkBuilder`: Builder to ease building `Link` instances pointing to Spring MVC controllers. 使用`linkTo`/`methodOn`可很方便的获取对应某个`XXXMapping`方法所在的`url`

The word "`hypermedia`" was coined by Ted Nelson in 1962 as a generalization of "`hypertext`", an invention of his. Whereas `hypertext` entailed interlinked textual documents, `hypermedia` expanded the scope to any form of media. The key with both, of course, is the `embedding of links in the content we use`.

`HAL`(Hypertext Application Language) is a simple format that gives a consistent and easy way to hyperlink between resources in your API.

## spring-integration
Extends the Spring programming model to support the well-known `Enterprise Integration Patterns`.

## Spring Tool Suite
`Spring Tools` 4 is the next generation of Spring tooling for your favorite coding environment. Largely rebuilt from scratch, it provides world-class support for developing Spring-based enterprise applications, whether you prefer Eclipse, Visual Studio Code, or Theia IDE. 能识别spring/springboot应用特有的内容

## spring cloud
在pom中引入如下内容，这样设置properties属性`<spring-cloud.version>`，再引入spring-cloud相关包时就不需要添加版本号
```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>${spring-cloud.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
```

- `spring-cloud.version`的取值并不是实际的版本号，而是`Release Train`号，[参考](https://spring.io/projects/spring-cloud#getting-started)
- `@EnableConfigServer`
- `@RefreshScope`: A Scope implementation that allows for beans to be refreshed dynamically at runtime (see refresh(String) and refreshAll()). If a bean is refreshed then the next time the bean is accessed (i.e. a method is executed) a new instance is created.
    - `@RefreshScope`标记的bean是一个CGLib增强的原bean的子类，并实现如下接口: `ScopedObject`, `AopInfrastructureBean`, `SpringProxy`, `Advised`, `Factory`，具体操作会通过`TargetSource`delegate到原bean. 如果其被其他bean通过`@Autowired`依赖，通过这种方式，被依赖侧也是会更新的（更新期间可能会有时间差？）
- client端引入`spring-cloud-config-server`会导致`ConfigServicePropertySourceLocator`不被启用，无法获取配置，原因未知
- `bootstrap.properties`， 比如用到spring-cloud-config时(用到`spring.application.name`)，会用到，`spring-cloud-context`的`BootstrapApplicationListener`中被导入

## spring security
Application security boils down to two more or less independent problems: `authentication` (who are you?) and `authorization` (what are you allowed to do?). 后者在有些地方称为`access control`

The main strategy interface for authentication is `AuthenticationManager`. The most commonly used implementation of `AuthenticationManager` is `ProviderManager`, which delegates to a chain of `AuthenticationProvider` instances.

the core strategy of authorization is `AccessDecisionManager`. There are three implementations provided by the framework and all three delegate to a chain of `AccessDecisionVoter` instances.... Most people use the default `AccessDecisionManager`, which is `AffirmativeBased` (if any voters return affirmatively, access is granted).

`Spring Security` in the web tier (for UIs and HTTP back ends) is based on `Servlet Filters`(which are `ordered`). Spring Security is installed as a single Filter(inside of it, there are additional filters) in the chain, and its concrete type is `FilterChainProxy`.

The fact that all filters internal to Spring Security are unknown to the container is important

- `cookie-based authentication` with a redirect to a login page for the UI parts
- `token-based authentication` with a 401 response to unauthenticated requests for the API parts.

As well as support for securing web applications, Spring Security offers support for applying access rules to Java method executions.

- `@AuthenticationPrincipal`(可放在Mapping method参数上): This annotation pulls the current `Authentication` out of the `SecurityContext` and calls the `getPrincipal()` method on it to yield the method parameter.

`token`本身有两种，一种是一个key或reference，通过该key可获取token对应的；另一种直接把数据保存到token中。token可存储在cookie中，由于cookie有大小限制，token的第一种方式就很适合

## spring-web
- `spring-web`的`CommonsMultipartFile.transfer`时，如果存储在磁盘，是rename过去的，rename失败才会copy

