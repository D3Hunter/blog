传统gnome桌面，可用`Super+Alt+RB`弹出任务条菜单
`gnome-session-fallback`
`dconf-editor`
卸载wine×后倒在Unity不可用，gnome界面也出不来，重装gnome
`xwininfo xprop`查看当前窗口信息

安装dep包 `sudo dpkg -i *.dep`
`apt-get download` 下载dep包，安装过程可参考man dpkg主要执行特定脚本，然后复制文件（和/目录结构类似）
`ar -x pakname.deb`解压deb包

`sudo`运行命令受`/etc/sudoers`影响，`Defaults secure_path`会重设`PATH`，导致`command not found`, 去掉即可
