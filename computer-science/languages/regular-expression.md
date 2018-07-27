不包括abcd的行，使用`negative lookahead assertion`实现：`^((?!abcd).)*$`

- positive lookahead assertion `(?=...)`
- negative lookahead assertion `(?!...)`
- positive lookbehind assertion `(?<=...)`
- negative lookbehind assertion `(?<!...)`
- .* .+ 默认是greedy的，后面跟?变成非greedy
- `\b` Matches the empty string, but only at the beginning or end of a word. 匹配字边界
- `\B` Matches the empty string, but only when it is not at the beginning or end of a word. 匹配非字边界
- `\s` When the UNICODE flag is not specified, it matches any whitespace character
- `\S` When the UNICODE flag is not specified, matches any non-whitespace character;
    - 如果无法指定DOTALL模式，可使用`[\s\S]`替代

