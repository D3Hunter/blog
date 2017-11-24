### Embedded Jetty
参考eclipse jetty embedded jetty部分文档
#### 设置handler
- extends AbstractHandler
- ServletHandler
- ServletContextHandler
#### 设置资源占用
以下设置线程数及`accept queue`大小（超了不再`accept`，客户端连接失败）
```
LinkedBlockingQueue<Runnable> queue = new LinkedBlockingQueue<>(acceptQueueSize);
QueuedThreadPool pool = new QueuedThreadPool(ThreadPoolMax(), ThreadPoolMin(), THREAD_IDLE_TIMEOUT, queue);
Server webServer = new Server(pool);

ServerConnector connector = new ServerConnector(webServer);
connector.setPort(ListenPort;
webServer.addConnector(connector);
```

jetty的threadpool有三块会使用
- acceptor 默认`Math.max(1, Math.min(4,cores/8))`
- selector 默认`Math.max(1,Math.min(4,cores/2))`
- request 线程池剩下的
