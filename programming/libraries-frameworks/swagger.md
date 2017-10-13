### swagger and spring
JAX-RS: Java API for RESTful Web Services
	Representational State Transfer

Swagger is an open source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful Web services. While most users identify Swagger by the Swagger UI tool, the Swagger toolset includes support for automated documentation, code generation, and test case generation.

http://www.baeldung.com/swagger-2-documentation-for-spring-rest-api
http://eugeneyang.com/2015/12/18/Springmvc4%E9%9B%86%E6%88%90springfox,%20Swagger%20UI,%20springfox-staticdocs/
springfox implements Swagger specification
Swagger mainly centers around the Docket bean
Swagger 2 is enabled through the @EnableSwagger2 annotation.
After the Docket bean is defined, its select() method returns an instance of ApiSelectorBuilder, which provides a way to control the endpoints exposed by Swagger.

启用`springfox-swagger-ui`后`http://localhost:8080/swagger-ui.html` 查看api信息

swagger Api开头的annotation为辅助生成文档用

默认Swagger-Core只包含Api标记的类
ApiIgnore可以忽略一些api