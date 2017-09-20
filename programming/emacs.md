格式化代码：`indent-region`
没有`redo`的概念，可以按任意建使`undo`也可以`undo`，即`redo`
输入特殊字符 : `ctrl-q` 加`tab`就可以输入`tab`,`C-q C-j` `C-q C-m`输入`^J` `^M`
列出可用字符`M-x list-charset-chars`
yank到剪切板 : `(setq x-select-enable-clipboard t)`同时yank到剪切板，console无效
正则替换 : `replace-regexp` 类似于M-%，支持正则
设置没有line wrap : `M-x toggle-truncate-lines` 或 `(setq-default truncate-lines 1)`
显示列号 `M-x column-number-mode` 或 `(setq column-number-mode t)`
`M-x imenu` 可定位函数(仅当前buf)，可自动补齐
`M-/`自动补齐,可使用tags文件
align对齐 `align-regex`
`M-u/l/c` 大小写
`M-|`在区域上执行命令,比如python -m json.tool将json字符串格式化
`nhexl-mode`去掉overwrite即可插入
`M-& async shell`
`C-x s`保存所有buffer
`C-x C-w` save as
`dired`使用`m/u`标记文件，`dired-do-query-replace-regexp`可在标记的文件内查找替换
`revert-buffer`
`imenu-add-to-menubar`查看文件中的函数列表
emacs按字搜索：`M-s w`
默认emacs会自动添加最后的换行`(setq mode-require-final-newline nil)`
`C-x RET r dos RET` 避免显示`^M`
`C-x r M-w/C-x r y`  拷贝粘贴
`C-x r N`插入数字
重复上一条命令`C-x z`或`C-x ESC ESC`
`clipboard-yank`

列操作
- `C-x r k` Kill 
- `C-x r M-w` Copy 
- `C-x r d` Delete
- `C-x r y` Yank
- `C-x r o` Insert blank space
- `C-x r N` Insert line numbers
- `C-x r c` Clear with spaces
- `C-x r t` string <RET> Replace 
- `M-x string-insert-rectangle <RET> string <RET>` Insert string on each line of the rectangle. 

tags相关
- `etags *.c` 写入TAGS for emacs
- `M-.` 查找first tag  `M-*`返回
- `C-u M-.` 下一个符合的tag
- `C-u - M-.` 返回上一个符合的tag
