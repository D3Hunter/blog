### Problems
`Can’t be updated when it’s running from a read-only`:
1. 退出
2. xattr -dr com.apple.quarantine /Applications/Your.app
3. 启动

去掉pylint: `"python.linting.pylintEnabled": false`

### plugins
`python.pythonPath`可以设置VirtualEnv设置的目录位置

如果`c/c++ goto defination`不可用可看下`browse.path`的设置是否包含了对应位置

