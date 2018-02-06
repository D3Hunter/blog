设置断点：`import pdb; pdb.set_trace()`
获得当前运行线程：`p threading._active`

获取某个线程的调用栈,参考以下python代码
`p traceback.extract_stack(sys._current_frames()[139778270615296])`
```python
print >> sys.stderr, "\n*** STACKTRACE - START ***\n"
code = []
for threadId, stack in sys._current_frames().items():
    code.append("\n# ThreadID: %s" % threadId)
    for filename, lineno, name, line in traceback.extract_stack(stack):
        code.append('File: "%s", line %d, in %s' % (filename,
                                                    lineno, name))
        if line:
            code.append("  %s" % (line.strip()))

for line in code:
    print >> sys.stderr, line
print >> sys.stderr, "\n*** STACKTRACE - END ***\n"
```
