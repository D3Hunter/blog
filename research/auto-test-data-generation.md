### Paper：
- Automated Test Data Generation for Coverage: Haven’t We Solved This Problem Yet? http://www0.cs.ucl.ac.uk/staff/M.Harman/taic09.pdf
- https://blog.csdn.net/wcventure/article/details/81946683


### jcute
安装
- 按照官网文档执行完后，需要执行`bash setup`
- 同时修改`jcutec`和`jcute`中的`CLASSPATH`，包含上`3rdparty`
- 提示找不到lp_solve库，使用`install_name_tool -change`更改
- `otool -l` 和 `otool -L`可查看dylib文件信息

查看报告使用`java -classpath jcute.jar cute.concolic.logging.BranchCoverageLog`

