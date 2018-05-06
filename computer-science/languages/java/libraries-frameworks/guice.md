### Work with Jetty Servlet
```
ServletContextHandler servletContextHandler = new ServletContextHandler(server, "/", ServletContextHandler.SESSIONS);
servletContextHandler.addFilter(GuiceFilter.class, "/*", EnumSet.allOf(DispatcherType.class));

// You MUST add DefaultServlet or your server will always return 404s
servletContextHandler.addServlet(DefaultServlet.class, "/");
```
extends `ServletModule` and `serve` path with `servlet class`
- http://blog.timmattison.com/archives/2014/09/02/full-example-code-showing-how-to-use-guice-and-jetty/


### misc
支持AOP操作，使用AOP Alliance接口
