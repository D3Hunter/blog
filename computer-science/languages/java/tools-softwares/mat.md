`mat`: Eclipse Memory Analyzer Tool

`mat`在`mac`上运行报错，日志说需要设置`-data`参数,该参数一定要是绝对路径，否则仍然会拼接到错误的路径里。另外要以下面的形式写在`-vmargs`前面:
```
-data
/path/to/workspace
```

命令行分析可以使用`ParseHeapDump.sh`
- The `org.eclipse.mat.api:suspects` argument creates a ZIP file containing the leak suspect report. This argument is optional.
- The `org.eclipse.mat.api:overview` argument creates a ZIP file containing the overview report. This argument is optional.
- The `org.eclipse.mat.api:top_components` argument creates a ZIP file containing the top components report. This argument is optional.

