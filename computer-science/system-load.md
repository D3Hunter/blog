## system load average
The load average tries to measure the number of active processes(running, runnable, task uninterruptible) at any time.

`System load average`: Zero means there is no load. If you have a system with four CPU cores, a value of four would mean to system is fully loaded, a value of eight would mean the system is overloaded.

`System load` is a better metric than computing CPU utilization because the latter doesn't distinguish between the case a system is `fully loaded` and a system is `overloaded`.

[UNIX Load Average Part 1: How It Works - Neil J. Gunther](http://www.perfdynamics.com/Papers/la1.pdf)

- 1 HZ = 100 ticks
- 5 HZ = 500 ticks
- 1 tick = 10 miliseconds
- 500 ticks = 5000 miliseconds (or 5 seconds)
So, `5 HZ` means that CALC_LOAD=5HZ is called every 5 seconds.

基于5s一次的采样结果（active processes)，使用`EMA`计算`load average`，但`α`的取值使用的exp函数，1min的load average的`α`仅为wiki上推荐的`2/(N + 1)`的一半左右，所以历史数据的权重更高
