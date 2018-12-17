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

高级设置：Scroll wheel sends arrow keys when in alternate screen mode，避免滚动命令行历史

### 查看listen的端口
```
sudo lsof -iTCP -sTCP:LISTEN
sudo lsof -iTCP -sTCP:LISTEN -P
sudo lsof -iTCP -sTCP:LISTEN -P -n. -P -n prevents lsof from doing name resolution
sudo lsof -iTCP -sTCP:LISTEN -n
```

### commands

`osascript` -- execute OSA scripts (AppleScript, JavaScript, etc.)

命令行启动提示：`osascript -e 'display notification "check data center" with title "Time out"'`

- 进程线程数 `ps -M <pid> | wc -l`
- ldd: `otool -L`
- 使用对应的app打开某个文件:`open xxxx.xls`, 可通过`-a`指定应用

dtrace cannot control executables signed with restricted entitlements
- 在另一个窗口dtruss当前窗口pid：`sudo dtruss -p <pid> -f`
- 在当前窗口执行dtruss对应程序

networksetup用来管理网络相关
- networksetup -listallnetworkservices
- networksetup -getXXXXproxy Wi-Fi
- networksetup -setXXXXproxy Wi-Fi
- networksetup -setXXXXproxystate Wi-Fi on/off
- networksetup -getproxybypassdomains Wi-Fi
- networksetup -setproxybypassdomains Wi-Fi xxx
- 避免networksetup输入密码
    - `sudo visudo` to modify the file `/etc/sudoers`.
    - `your_username ALL=(ALL) NOPASSWD: /usr/sbin/networksetup`
    - Using `sudo networksetup ...` shouldn't require a password anymore.

系统配置文件位置
- /Library/Preferences/SystemConfiguration

- `sysctl` hw.physicalcpu hw.logicalcpu查看是否开启超线程
- `id` 可查看当前uid及所属gid
- `ps -j`可将uid转换成username，需要放在-f前面

更换sed为gnu-sed：`brew reinstall gnu-sed --with-default-names`，使用`/usr/local/bin/sed`


### 绑定keyboard short到某个shell script
- Open Automator
- New Document -> Service
- Add the 'Run Shell Script' module and insert your code killall -KILL Dock
- Set the 'Service receives no input', save and quit.
- Install your newly created service by opening it in Finder and choose 'Install'.
    - 看左上角应用菜单->服务
- Attach a keystroke to this service:
    - Open 'System preferences' -> 'Keyboard' -> 'Keyboard shortcuts' -> 'Services'
    - Find the service and attach a keystroke to it.


### finder
- finder显示隐藏文件`CMD + SHIFT + .`, 或者在terminal输入`defaults write com.apple.finder AppleShowAllFiles YES`,然后重启finder
- 底部显示path：`View->Show Path`
- title显示path：`defaults write com.apple.finder _FXShowPosixPathInTitle -bool true; killall Finder`
- 拷贝当前路径到剪切板：`Opt + Cmd + c`，选中文件时复制的是所选文件的路径，不选则是当前文件夹
### brew 没有特定软件
- `brew install coreutils`
- `sudo ln -s /usr/local/bin/gsha256sum /usr/local/bin/sha256sum`

### 截屏
Command + Shift + 3/4: 结果保存到桌面，分别为截取整个屏幕／选择截取
Ctrl + Command + Shift + 3/4: 结果保存到剪切板，分别为截取整个屏幕／选择截取

### 更改文件类型的默认application
1. From the Mac file system, select a file of the general format type you wish to change the default application for
2. Pull down the “File” menu and choose “Get Info” (or hit Command+i) to access the Get Info window
3. Click the “Open with:” sub menu, then click on the contextual menu and select the new application to associate all files of this format type with

### 去掉`[NAME] is an application downloaded from the internet. Are you sure you want to open it?`弹窗:
- `xattr -d -r com.apple.quarantine /Path/to/application/`

