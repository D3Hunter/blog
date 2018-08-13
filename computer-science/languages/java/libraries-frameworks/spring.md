spring-web的CommonsMultipartFile.transfer时，如果存储在磁盘，是rename过去的，rename失败才会copy

The Spring Framework provides a comprehensive programming and configuration model for modern Java-based enterprise applications - on any kind of deployment platform.
A key element of Spring is infrastructural support at the application level: Spring focuses on the "plumbing" of enterprise applications so that teams can focus on application-level business logic, without unnecessary ties to specific deployment environments.
### Features
- Dependency Injection
- Aspect-Oriented Programming including Spring's declarative transaction management
- Spring MVC and Spring WebFlux web frameworks
- Foundational support for JDBC, JPA, JMS


p-namespace/c-namespace

bean初始化的顺序可通过depends-on做

Core Container
    Core, Bean, Context, SpEL

Spring Configuration Metadata
    XML based configuration file.
    Annotation-based configuration
    Java-based configuration

dependency injection
    Constructor-based
    Setter-based
    but it is a good rule of thumb to use constructor arguments for mandatory dependencies and setters for optional dependencies.

AOP
    Aspect: an aspect is scattered or tangled as code, making it harder to understand and maintain
    Join point: This represents a point in your application where you can plug-in AOP aspect
    Advice: This is actual piece of code that is invoked during program execution by Spring AOP framework.
        Before/After/After-returning/After-throwing/Around
    PointCut: This is a set of one or more joinpoints where an advice should be executed.
    Introduction: An introduction allows you to add new methods or attributes to existing classes.
    Target object: The object being advised by one or more aspects, this object will always be a proxied object. Also referred to as the advised object.
    Weaving: Weaving is the process of linking aspects with other application types or objects to create an advised object. This can be done at compile time, load time, or at runtime.

The Spring Web model-view-controller (MVC) framework is designed around a DispatcherServlet that handles all the HTTP requests and responses.
    request-driven

+------------------------------------------------------------------+
| Annotation | Meaning                                             |
+------------+-----------------------------------------------------+
| @Component | generic stereotype for any Spring-managed component |
| @Repository| stereotype for persistence layer                    |
| @Service   | stereotype for service layer                        |
| @Controller| stereotype for presentation layer (spring-mvc)      |
+------------------------------------------------------------------+

@Component  – Indicates a auto scan component.
@Repository – Indicates DAO component in the persistence layer.
@Service    – Indicates a Service component in the business layer.
@Controller – Indicates a controller component in the presentation layer.
@RequestMapping处理什么样的请求

Autowired
    No qualifying bean of type […] found for dependency这种情况为对应的bean没注册
        如果是在Configuration中，需要添加对应方法返回该bean
    No qualifying bean of type […] is defined有多个Bean接口的实现
        异常为NoUniqueBeanDefinitionException
    No Bean Named […] is defined这种bean没定义

AnnotationConfigApplicationContext可以注册一系列标记的类，如@Configuration
    使用register必须refresh
WebApplicationContext: a spring container包含应用中的所有业务bean
    可以使用ContextLoaderListener 配置
    WebApplicationContext ctx = WebApplicationContextUtils.getWebApplicationContext(servletContext);
添加<context:property-placeholder .. />后，可以使用variable substitution
    这块底层是如何执行的，值从哪儿搜索，被搜索对象何时创建的
使用DispatcherServlet一般是将所有请求转到这个servlet，使用mvc:default-servlet-handler
    可将static resource转到default servlet上

@Configuration indicates that the class can be used by the Spring IoC container as a source of bean definitions.同样被@Component标记过，因此可被扫描
@Bean annotation tells Spring that a method annotated with @Bean will return an object that should be registered as a bean in the Spring application context.
@Import annotation allows for loading @Bean definitions from another configuration class.
@Scope 指定bean的scope，默认为singleton，prototype为每次都重新申请，其他的还有
    request，session，globalsession
    singleton为per ApplicationContext，application为per ServletContext
@Autowired annotation can apply to bean property setter methods, non-setter methods, constructor and properties.
@Async标记某个方法异步执行，会有线程数控制么？
@Qualifier当有多个想同类型的bean，要想使用autowire可配置该标记，值为beanid

@Bean跟@Configuration在一块用表示某函数会返回一个让Spring管理的bean
    而跟@Component在一块时？？
    full mode VS lite mode
@Configuration在启动时通过CGLIB被sub-class

meta-annotation可以标记其他标记的标记，比如@Service实际上被标记了@Component
    因此可以说@Component为meta-annotation

Spring Integration

ApplicationContext本身可作为ResourceLoader
    传给它的参数默认会按照context的类型创建对应的Resource，但可以指定prefix
    来覆盖默认行为，如：classpath:/file:/http:

Environment负责profiles和properties
    对于Properties通过一系列的PropertySource来进行
    默认的StandardEnvironment包含两个PropertySource，一个是JVM系统属性(
        System.getProperties())，一个是系统环境变量(System.getEnv())
        前者优先级更高
    配置中${xxx}都是从Environment中获取的

Extensible XML authoring
    Authoring an XML schema
    NamespaceHandler
    BeanDefinitionParser
    Registering the above artifacts with Spring
        META-INF/spring.handlers
        META-INF/spring.schemas
    spring会搜索classpath自动发现新的扩展:DefaultNamespaceHandlerResolver

controller方法返回callable可以异步处理请求，container-thread-A返回callable后结束
    处理由另外的线程进行，之后由container-thread-B返回结果
    use case: 请求要求结果且需要时间来计算结果，为避免用光container的线程池，提高吞吐
    内部使用request.startAsync()(servlet 3提供该功能)

对于singleton的bean(默认都是), 且不是lazy init(默认)，那么当context启动后就会创建
由于上面的一点，可以使用@PostConstruct来执行一些特定代码，也可以用属性init-method
    相比起来，前者更方便

Bean definition profiles根据环境配置bean,嵌套的beans配置需要放到后面
    可通过context-param: contextInitializerClasses来配置profile功能的初始化
    系统属性spring.profiles.active可用来配置哪个profile为active，也可编程设置

Annotation injection is performed before XML injection, so it can be overrided.
Annotation wiring需要在配置中开启

PropertiesLoaderUtils读取property配置文件

没有id/name的bean可以通过类型来获取/autowire，这时不能有多个class相同但都没id/name，会报错

annotation本身并不会做什么，再XML中需要<context:annotation-config />才能让其起作用
annotation标记的bean并不会自动成为bean，需要用上面描述的几种方法来生效
context:component-scan从包里扫描bean
mvc:message-converters似乎能将HTTP payload按配置转成特定对象，这需要主动调用
    HTTP Message Conversion
Velocity and FreeMarker are two templating languages that can be used as view technologies within Spring MVC applications.
spring的Interceptor跟servlet filter类似，但跟spring结合更好，一些操作可能更易完成

BeanFactoryPostProcessor/BeanDefinitionRegistryPostProcessor注册后的Listener

bean生命周期管理方式：
    InitializingBean/DisposableBean分别调用afterPropertiesseSet/destroy
    JSR250提供了PostConstruct和PreDestroy，这种方式不依赖Spring
        这种方式比前者优先级更高

### XML Schema-based configuration
XML Schema-based configuration支持使用namespace的格式
支持对配置文件扩展：Extensible XML authoring，用户自定义schema
- Authoring an XML schema to describe your custom element(s).
- Coding a custom `NamespaceHandler` implementation (this is an easy step, don’t worry).
- Coding one or more `BeanDefinitionParser` implementations (this is where the real work is done).
- Registering the above artifacts with Spring (this too is an easy step).
    - `META-INF/spring.handlers`
    - `META-INF/spring.schemas`

When using XML-based configuration metadata, you use the `'id'` or `'name'` attributes to specify the bean identifier(s).

