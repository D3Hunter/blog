### Latex
Comprehensive TEX Archive Network (CTAN)

`TEX` is pronounced "Tech", while `LATEX` is pronounced “Lay-tech”(originally written by Leslie Lamport). LATEX 2" is pronounced “Lay-tech two e” and `typed LaTeX2e`

Several consecutive whitespace characters are treated as one “space”.

An empty line between two lines of text defines the end of a paragraph. Several empty lines are treated the same as one empty line.

reserved characters: `# $ % ^ & _ { } ~ \`, to input them uses:
    - `\#` `\$` `\%` `\^` `\&` `\_` `\{` `\}` `\~` `\textbackslash`

`LATEX` ignores whitespace after commands. If you want to get a space after a command, you have to put either an empty parameter `{}` and a blank or a special spacing command after the command name.

Command format: `\command[optional parameter]{parameter}`

When LATEX encounters a `%` character while processing an input file, it ignores the rest of the present line, the line break, and all whitespace at the beginning of the next line.

LATEX file structure:
```latex
\documentclass{article}
\begin{document}
Small is beautiful.
\end{document}
```

The area between `\documentclass` and `\begin{document}` is called the `preamble`.

`Page orientation` is the way in which a rectangular page is oriented for normal viewing. The two most common types of orientation are `portrait` and `landscape`. The term "`portrait orientation`" comes from visual art terminology and describes the dimensions used to capture a person's face and upper body in a picture; in such images, the height of the display area is greater than the width. The term "`landscape orientation`" also reflects visual art terminology, where pictures with more width than height are needed to fully capture the horizon within an artist's view.

In publishing there are special opening and closing quotation marks. In
LATEX, use two ` (grave accent) for opening quotation marks and two ' (vertical quote) for closing quotation marks.

In typography, a `serif` is a small line or stroke regularly attached to the end of a larger stroke in a letter or symbol within a particular font or family of fonts. A typeface or "font family" making use of `serifs` is called a `serif typeface`, and a typeface that does not include them is a `sans-serif` one.

right-hand page: 看书时右手所在页，或者说是订装页的正面页，left-hand page同理

As noted at the beginning of this chapter, it is dangerous to clutter your document with explicit commands like this, because they work in opposition to the basic idea of `LATEX`, which is to separate the `logical` and `visual markup` of your document. you should use `\newcommand` to define a “`logical wrapper command`” for the font changing command.

LATEX builds up its pages by pushing around boxes.

#### Mac上安装Latex
1. 安装`mactex`，可以用brew安装，`mactex`本身提供的UI工具不太好用。命令行工具在`/Library/TeX/texbin/`目录下（实际指向`/usr/local/texlive/2019/bin/x86_64-darwin`）
2. 安装`texstudio`，`texstudio`本身不包含`Tex`的核心工具，需要在`Preferences->Commands`里设置外部命令，在`/Library/TeX/texbin/`目录下找即可

#### 支持中文
1. 在`Preferences -> “Build -> Default compiler`种设置默认编译器为`XeLaTeX`
2. 文件以utf8编码，texstudio状态栏也设置为utf8
3. 在preamble中添加如下设置
```tex
\usepackage{ctex}
\setCJKmainfont{Kaiti TC Regular}
\setCJKsansfont{Songti TC Regular}
\setCJKmonofont{Heiti TC Regular}
```

