每个logger都有自己的level，未设置就取parent的level，root的默认level为debug
继承hierarchy通过'.'区分
LoggerFactory.getLogger对同一个名称（类）始终返回同一个logger
log过程是参数构建在前，判断在后，可用isXXXEnabled提高效率

MDC(Mapped Diagnostic Context), 对于分布式系统，日志系统用来输出跟特定client/request相关的标记内容
