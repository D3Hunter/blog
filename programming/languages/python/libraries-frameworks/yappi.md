### example
```python
import yappi
def foo():
    for i in range(10000000):
        pass
yappi.start()
foo()
yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
```
结果如下：
tsub：shallow time
scnt：scheduled count

    Clock type: CPU
    Ordered by: totaltime, desc

    name                                  ncall  tsub      ttot      tavg
    test.py:2 foo                         1      0.290882  0.290882  0.290882

    name           id     tid              ttot      scnt
    _MainThread    0      140663324436224  0.291468  1

### API
默认`yappi`记录`cputime`（可以用来profile cpu使用情况），可通过`yappi.set_clock_type("wall")`设置时间记录类型为walltime（profile响应时间构成）
