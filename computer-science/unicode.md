`Specials` is a short `Unicode block` allocated at the very end of the `Basic Multilingual Plane`, at `U+FFF0–FFFF`. Of these `16` code points, `five` are assigned as of `Unicode 12.0`:
- `U+FFFD` � `REPLACEMENT CHARACTER` used to replace an unknown, unrecognized or unrepresentable character
    - 在`UTF-8`里面是 `0xEF 0xBF 0xBD`
    - 该值可以用来判断是否存在乱码

`Mojibake` (文字化け) is the garbled text that is the result of text being decoded using an unintended character encoding. The result is a systematic replacement of symbols with completely unrelated ones, often from a different writing system. This display may include the generic `replacement character` ("�") in places where the binary representation is considered invalid.
- `Mojibake` means `"character transformation"` in Japanese. The word is composed of 文字, "character" and 化け "transform".
- In Chinese, the same phenomenon is called `Luàn mǎ` (乱码, meaning chaotic code)

The `Unicode collation algorithm (UCA)` is an algorithm defined in `Unicode Technical Report #10`, which is a customizable method to produce binary keys from strings representing text in any writing system and language that can be represented with `Unicode`. These keys can then be efficiently byte-by-byte compared in order to `collate` or `sort` them according to the rules of the language, with options for ignoring case, accents, etc.
- Default Unicode Collation Element Table (DUCET)
- International Components for Unicode, ICU

