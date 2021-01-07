## latency and fault tolerance library
isolate points of access to remote systems, services and 3rd party libraries, stop cascading failure and enable resilience(适应力，快速恢复的能力) in complex distributed systems where failure is inevitable.

Circuit Breaker

- Netflix/Hystrix
- alibaba/Sentinel 流控防护：flow control, traffic shaping, circuit breaking and system adaptive protection
- Resilience4J
- Spring Retry

## Asciidoctor
A fast text processor & publishing toolchain for converting AsciiDoc to HTML5, DocBook & more.

## vault
`Vault` is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.

1. Static Infrastructure
Datacenters with inherently high-trust networks with clear network perimeters.

TRADITIONAL APPROACH
- High trust networks
- A clear network perimeter
- Security enforced by IP Address

2. Dynamic Infrastructure
Multiple clouds and private datacenters without a clear network perimeter.

VAULT APPROACH
- Low-trust networks in public clouds
- Unknown network perimeter across clouds
- Security enforced by Identity

## WireMock
WireMock is a simulator for HTTP-based APIs. Some might consider it a `service virtualization tool` or a `mock server`.

## httpbin
A simple HTTP Request & Response Service.

## service registry and discovery
`Eureka` is a REST (Representational State Transfer) based service that is primarily used in the AWS cloud for `locating services`(service discovery) for the purpose of load balancing and failover of middle-tier servers.

`Consul`/`Zookeeper`也能提供类似能力

## Thymeleaf template engine
`Thymeleaf` is a modern server-side Java template engine for both web and standalone environments.

The `Thymeleaf` configuration is also taken care of by `@SpringBootApplication`. By default, `templates` are located in the classpath under `templates/` and are resolved as `views` by stripping the `'.html'` suffix off the file name.

