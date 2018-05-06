设计上概念的正交性
- 比如埋点概念，静态下只是target、advice和其他一些静态信息
- 但在运行时经过的埋点变成了SpanEvent，包含各种运行时数据，参数、duration、关联信息和返回值等。当然静态信息也可以包含进来。
- scope(作用域、范围、组）: interceptor scope, trace scope

涉及到的概念
- 时态
    - 静态
        - 静态埋点Interceptor
        - 静态埋点组InterceptorScope
    - 运行态
        - 运行时组InterceptorScopeInvocation
            - 存放运行时组内共享信息Attachment
            - 限定买点进入时机：Always、Boundary（不可嵌套）、Internal（可嵌套）。可用来限制不必要的埋点进入。
            - 也可以称为InterceptorScopeRuntimeContext
        - Trace 某请求上下文
        - Span 表示整个Trace内的信息
        - SpanEvent运行时经过的某个埋点
- scope：范围、分组，如interceptor scope（一组关联的interceptor）、trace scope（如存在async或者sub trace的情况）
    - 参考InterceptorScope和InterceptorScopeInvocation
- context，跟时态组合成为两种概念
