在`Before Launch`中添加External tools，可在debug前执行脚本，用来实现`一键编译部署启动调试`
设置默认maven：`File->Others Settings->Default Preferences`

ctrl-W: expand selection
Cmd-shift-m: move to matching brace

如果使用了`Scanner.java`，`mac`上需要用`⌘-D`来输入`EOF`

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
### live templates
只支持有限的函数，substring支持较弱（只有`substringBefore`），但可以使用`regularExpression`替代

- `regularExpression()`中的`pattern`使用java的字符串解析方式，即如果要使用pattern中使用`\`，则要先使用java的方式转义一次
- `clipboard()`获取剪切板内容

参考[predefined_functions](https://www.jetbrains.com/help/idea/2018.3/edit-template-variables-dialog.html#predefined_functions)
