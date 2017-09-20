`e(edit)` filename
`n` [filename]切换到某个文件
so ~/.vimrc加载配置，与前者同时使用可都加载
qall（qa)
u1|u rever-buffer到
`D`删除光标到行尾
`dw`删除字
`dt'`删除直到'，'可以换成任意字符
[n]<>可以增加减少缩进
注释多行 Shift I # Esc
选中文本，然后`u/U`进行case转换
使用`P`（insert粘贴）而不是`p`（append粘贴）来粘贴
`wa` 全部保存
redo `ctrl+r`/ undo `u`
Ctrl+O/I(TAB) to older/newer cursor position
lcd/pwd/grep
可以用V模式，替换一片区域，但是仍然不能选择
行号：set number/nonumber

### session
mksession ~/mysession.vim
source ~/mysession.vim
vim -S ~/mysession.vim
### 移动，滚屏
e/b/w按字移动
$/0/^/A/I
v：之后d/y，之后可以p
Ctrl-v: 之后I/A/r/d/c进行列编辑，按esc确认结果
zz/zb/zt将当前行作为中间、顶、底
`Ctrl-e/y` 滚动一行
`Ctrl-d/u` 滚动半页
`Ctrl-f/b` 滚动一页
gd/gD goto local/global declaration
g*/g# search word under cursor forward/backward
H/M/L屏幕内cursor移动
gg/G文件头尾

### tag：
- ctrl + ]  查找当前对象定义
- ctrl + o 回退

### convert case：
- gUiw/guiw 更改当前字
- gUU/guu 当前行
- U/u 在v模式下更改选中部分

### plugins:
- plug manager
    1. vim-plug
    2. vundle
- vim-easy-align
sudo apt-get install exuberant-ctags自带的tags不好用
### range
- 21     line 21                                     :21s/old/new/g
- 1      first line                                  :1s/old/new/g
- $      last line                                   :$s/old/new/g
- .      current line                                :.w single.txt
- %      all lines (same as 1,$)                     :%s/old/new/g
- 21,25  lines 21 to 25 inclusive                    :21,25s/old/new/g
- 21,$   lines 21 to end                             :21,$s/old/new/g
- .,$    current line to end                         :.,$s/old/new/g
- .+1,$  line after current line to end              :.+1,$s/old/new/g
- .,.+5  six lines (current to current+5 inclusive)  :.,.+5s/old/new/g
- .,.5   same (.5 is interpreted as .+5)             :.,.5s/old/new/g
### 行移动
- nnoremap <A-j> :m .+1<CR>==
- nnoremap <A-k> :m .-2<CR>==
- inoremap <A-j> <Esc>:m .+1<CR>==gi
- inoremap <A-k> <Esc>:m .-2<CR>==gi
- vnoremap <A-j> :m '>+1<CR>gv=gv
- vnoremap <A-k> :m '<-2<CR>gv=gv
## window
split/vsplit(sp/vs) file
hide/only/close
`bd` 关闭buffer
`ctrl-w` 上下左右
`ctrl-w ctrl-w`    - move cursor to another window (cycle)
`ctrl-w =`  让所有window等大小
`windo/bufdo` 所有window/buf做同样操作
ls(buffers)
- u   列表外缓冲区 |unlisted-buffer|。
- %   当前缓冲区。
- #   轮换缓冲区。
- a   激活缓冲区，缓冲区被加载且显示。
- h   隐藏缓冲区，缓冲区被加载但不显示。
- =   只读缓冲区。
- -   不可改缓冲区， 'modifiable' 选项不置位。
- +   已修改缓冲区。
- buffers! 显示列表外缓冲
### 缓冲命令
- buffer         编辑一个缓冲区
- bnext          编辑下一个缓冲区
- bprevious      编辑前一个缓冲区
- bfirst         编辑第一个缓冲区
- blast          编辑最后一个缓冲区
- bdelete        删除一个缓冲区
- sbuffer 3
