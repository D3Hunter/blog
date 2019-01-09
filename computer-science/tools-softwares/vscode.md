`Option + Enter`：选择所有满足查询条件的值。菜单栏看不到，只能在`Open Keyboard Shortcuts`查看

### Problems
`Can’t be updated when it’s running from a read-only`:
1. 退出
2. xattr -dr com.apple.quarantine /Applications/Your.app
3. 启动

去掉pylint: `"python.linting.pylintEnabled": false`

### plugins
`python.pythonPath`可以设置VirtualEnv设置的目录位置

如果`c/c++ goto defination`不可用可看下`browse.path`的设置是否包含了对应位置

### mac重启后vscode变成`?`:
- Use the macOS default unarchiving app, "Archive Utility" (when I was having this issue, I was extracting the VSCode app using a 3rd-party utility called "Dr. Unarchiver"
- Do not extract the app straight into the Applications directory; extract it into the Downloads folder, then drag and drop it into the Applications directory

### 命令行使用`code`
`Install code command to PATH`可在命令行使用`code`, `code -`可接收控制台输入，如`ls |code -`

