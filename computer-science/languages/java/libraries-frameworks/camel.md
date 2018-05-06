用来将Endpoint连起来
CamelContext
    camel包含一个CamelContext，它包含一组Component
Component
    A Component is essentially a factory of Endpoint instances.
    You can explicitly configure Component instances in Java code or an IoC container
    like Spring or Guice, or they can be auto-discovered using URIs.
Endpoint
    An Endpoint acts rather like a URI or URL in a web application or a
    Destination in a JMS system;
    camel支持很多种endpoint，甚至ssh、servicenow等

    VM/SEDA: 异步内存seda队列，可见性不同
        uri format: seda:someName[?options]
    Direct: 同步
    Spring event: 同步，payload需要在SpringApplicationEvent中
route中的多个bean/to会被当作pipeline
Component is essentially a factory of Endpoint instances.

Route中可访问的变量：
    ${header.<header_name>}: 可以使用setHeader，也可以通过sendBodyAndHeader
    ${body}

EventNotifier当消息送到endpoint后收到通知

从2.16开始支持dynamic to
