`ANSI escape sequences` are a standard for in-band signaling to control the cursor location, color, and other options on video text terminals. Certain sequences of bytes, most starting with `Esc` and `[`, are embedded into the text, which the terminal looks for and interprets as commands, not as character codes.

Sequences have different lengths. All sequences start with `ESC` (27 / hex 0x1B / octal 033 / bash里面可以\e来表示), followed by a second byte in the range 0x40–0x5F (ASCII @A–Z[\]^_).

CSI - `Control Sequence Introducer`:`ESC [`

`Select Graphic Rendition(SGR)` sets display attributes. Several attributes can be set in the same sequence, `separated by semicolons`. Each display attribute remains in effect until a following occurrence of SGR resets it. If no codes are given, `CSI m` is treated as `CSI 0 m`(reset / normal).

Examples: to get black letters on white background use `ESC[30;47m`, to get red use `ESC[31m`, to get bright red use `ESC[1;31m`.

The SGR parameters `30-37` selected the foreground color, while `40-47` selected the background. Quite a few terminals implemented "bold" (SGR code `1`) as a brighter color rather than a different font

bash针对非打印字符有特殊要求，from bash man page:
- `\e`, an ASCII escape character (033)
- `\[`, begin a sequence of non-printing characters, which could be used to embed a terminal control sequence intothe prompt
- `\]`, end a sequence of non-printing characters

