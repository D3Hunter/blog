## SED
all commands `s/p/n/d/q//N/D/P/w/r/a/i/c/=/y/l/x/h/H/g/G/:/b/t/;/`

可在sed命令前指定范围
- Specifying a line by its number.
- Specifying a range of lines by number.
- All lines containing a pattern.
- All lines from the beginning of a file to a regular expression
- All lines from a regular expression to the end of the file.
- All lines between two regular expressions.
命令后可指定flags(也同名命令一样）
- /I - Ignore Case
- /w - filename Write to a file with
- /g - Global replacement
- /p - print

`&` as the matched string
```
% echo "123 abc" | sed 's/[0-9]*/& &/'
123 123 abc
```
The character after the `s` is the delimiter

命令前可加`!`将其语义去反（比如`p`为匹配时打印，`!p`为不匹配时打印）
the "!" command "inverts" the address range, operating on the other lines. 可用来做if else的逻辑
The curly braces, `{` and `}` are used to group the commands.
`{}`作为一个整体可取`!`，并可嵌套
```
sed -n '
	1,100 {
		/begin/,/end/ {
		     s/#.*//
		     s/[ ^I]*$//
		     /^$/ d
		     p
		}
	}
'
```
