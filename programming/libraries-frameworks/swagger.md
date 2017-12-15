The goal of Swagger™ is to define a standard, language-agnostic interface to REST APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection.

Swagger Editor
Swagger Codegen：generate server or client implementation
Swagger UI: explore the API

### Problems
Swagger Editor生成的代码直接在Idea中运行回报`ClassNotFound javax.servlet.http.HttpServletRequest`，把`spring-boot-starter-tomcat`和`javax-validation`的`privided` scope去掉即可
### Swagger Editor
Swagger Editor lets you edit `Swagger API specifications` in `YAML` inside your browser and to preview documentations in real time. Valid Swagger JSON descriptions can then be generated and used with the full Swagger tooling (code generation, documentation, etc).
### Swagger CodeGen
The Swagger Codegen is an open source code-generator to build server stubs and client SDKs directly from a Swagger defined RESTful API.
### swagger and spring
JAX-RS: Java API for RESTful Web Services
	Representational State Transfer

Swagger is an open source software framework backed by a large ecosystem of tools that helps developers design, build, document, and consume RESTful Web services. While most users identify Swagger by the Swagger UI tool, the Swagger toolset includes support for automated documentation, code generation, and test case generation.

http://www.baeldung.com/swagger-2-documentation-for-spring-rest-api
http://eugeneyang.com/2015/12/18/Springmvc4%E9%9B%86%E6%88%90springfox,%20Swagger%20UI,%20springfox-staticdocs/
springfox implements Swagger specification
Swagger mainly centers around the Docket bean
After the Docket bean is defined, its select() method returns an instance of ApiSelectorBuilder, which provides a way to control the endpoints exposed by Swagger.

swagger Api开头的annotation为辅助生成文档用

默认Swagger-Core只包含Api标记的类
ApiIgnore可以忽略一些api
