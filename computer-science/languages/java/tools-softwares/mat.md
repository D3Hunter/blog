mat在mac上运行报错，日志说需要设置-data参数,该参数一定要是绝对路径，否则仍然会拼接到错误的路径里。另外要以下面的形式写在-vmargs前面:
```
-data
/path/to/workspace
```
