- 在`Before Launch`中添加External tools，可在debug前执行脚本，用来实现`一键编译部署启动调试`
- 设置默认maven：`File->Others Settings->Default Preferences`
- 如果使用了`Scanner.java`，`mac`上需要用`⌘-D`来输入`EOF`
- IDEA DEBUG时默认是用idea自己的编译系统，如果对maven有依赖可以使用maven来编译`Maven -> Runner -> Delegate build and run actions to Maven`
- IDEA Debug asynchronous code：在`worker thread`断点触发时，自动关联对应`schedule thread`调度时的stack，默认对`Swing`和`Java Concurrency API`都有效，也可通过`@Async.Schedule`和`@Async.Execute`来定义相关触发点，或添加自定义触发点。该功能通过`instrumenting agent`实现（也支持完全由`Debugger`处理，但性能较差），远程调试需要添加对应`javaagent`。IDEA 2020版本默认开启


### 超大文件IDEA不做语法标记：
idea.properties
```
#---------------------------------------------------------------------
# Maximum file size (kilobytes) IDE should provide code assistance for.
# The larger file is the slower its editor works and higher overall system memory requirements are
# if code assistance is enabled. Remove this property or set to very large number if you need
# code assistance for any files available regardless their size.
#---------------------------------------------------------------------
idea.max.intellisense.filesize=2500
```

如果该值小于代码文件大小，可能会导致代码里显示语法错误。更好的做法是将该值设置足够大，然后打开大文件，`Analyse->Configure current file analyse`来关闭analyse，避免CPU飙升。

### live templates
只支持有限的函数，substring支持较弱（只有`substringBefore`），但可以使用`regularExpression`替代

- `regularExpression()`中的`pattern`使用java的字符串解析方式，即如果要使用pattern中使用`\`，则要先使用java的方式转义一次
- `clipboard()`获取剪切板内容

参考[predefined_functions](https://www.jetbrains.com/help/idea/2018.3/edit-template-variables-dialog.html#predefined_functions)

### 文本替换更改captured group的case：
- `\l` changes a character to lowercase until the next character in the string.
- `\u` changes a character to uppercase until the next character in the string.
- `\L` changes characters to lowercase until the end of the literal string `\E`.
- `\U` changes characters to uppercase until the end of the literal string `\E`.

