## 装机
install `brew`,`item2`,`oh my zsh`,`git`
隐私设置屏保立即需要密码`Ctrl-Shift-关机健`

### java多版本，需要重启
```
export JAVA_7_HOME="$(/usr/libexec/java_home -v 1.7)"
export JAVA_8_HOME="$(/usr/libexec/java_home -v 1.8)"
JAVA_HOME=$JAVA_7_HOME
alias jdk7="export JAVA_HOME=$JAVA_7_HOME"
alias jdk8="export JAVA_HOME=$JAVA_8_HOME"
```

### item2
profiles->keys->left options as ESC+

### 查看listen的端口
```
sudo lsof -iTCP -sTCP:LISTEN
sudo lsof -iTCP -sTCP:LISTEN -P 
sudo lsof -iTCP -sTCP:LISTEN -P -n. -P -n prevents lsof from doing name resolution
sudo lsof -iTCP -sTCP:LISTEN -n
```

### commands
进程线程数 `ps -M <pid> | wc -l`
ldd: `otool -L`

### brew 没有特定软件
- `brew install coreutils`
- `sudo ln -s /usr/local/bin/gsha256sum /usr/local/bin/sha256sum`

### 截屏
Command + Shift + 3/4: 结果保存到桌面，分别为截取整个屏幕／选择截取
Ctrl + Command + Shift + 3/4: 结果保存到剪切板，分别为截取整个屏幕／选择截取