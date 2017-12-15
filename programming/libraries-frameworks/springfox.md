The Springfox suite of java libraries are all about automating the generation of machine and human readable specifications for JSON APIs written using the spring family of projects.
Springfox works by examining an application, once, at runtime to infer API semantics based on spring configurations, class structure and various compile time java Annotations.

### Goals
- To extend support for a number of the evolving standards targeted at JSON API specification and documentation such as: `swagger`, `RAML` and `jsonapi`.
- To extend support for spring technologies other than `spring webmvc`
- Philosophically, we want to discourage using (swagger-core) annotations that are not material to the service description at runtime.
### Architecture
When we started work on 2.0 swagger specification we realized that we’re rewriting the logic to infer the `service models` and the `schema`. So we decided to take a step back and break it out into a two step process.
- First infer the `service model` into an internal representation.
- Second create a mapping layer that can map the `internal models` to different `specification formats`.
    - Out of the box we will support swagger 1.2 and swagger 2.0, but this leads us to the possibility of supporting other formats and other scenarios as well e.g. RAML, ALPS and hypermedia formats.
### Swagger
Springfox supports both version 1.2 and version 2.0 of the Swagger specification. Where possible, the Swagger 2.0 specification is preferable.

### Usage
加上`springfox-swagger-ui`包依赖，即可访问`swagger-ui.html`
通过`Docket` bean来定制具体信息
