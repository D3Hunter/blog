### Character Set
When computer systems process characters, they use numeric codes instead of the graphical representation of the character.

Character sets differ in the following ways:
- The number of characters available to be used in the set
- The characters that are available to be used in the set (also known as the `character repertoire`)
- The scripts used for writing and the languages that they represent
- The code points or values assigned to each character
- The encoding scheme used to represent a specific character

The characters that are encoded in a character set depend on the writing systems that are represented. A writing system can be used to represent a language or a group of languages. Writing systems can be classified into two categories:
- Phonetic Writing Systems
    - Phonetic writing systems consist of symbols that represent different sounds associated with a language.
    - Greek, Latin, Cyrillic, and Devanagari are all examples of phonetic writing systems based on alphabets. Note that alphabets can represent multiple languages. For example, the Latin alphabet can represent many Western European languages such as French, German, and English.
    - Characters associated with a phonetic writing system can typically be encoded in one byte because the character repertoire is usually smaller than 256 characters.
- Ideographic Writing Systems
    - Ideographic writing systems consist of ideographs or pictographs that represent the meaning of a word, not the sounds of a language.
    - Chinese and Japanese are examples of ideographic writing systems that are based on tens of thousands of ideographs. Languages that use ideographic writing systems may also use a syllabary. Syllabaries provide a mechanism for communicating additional phonetic information. For instance, Japanese has two syllabaries: Hiragana, normally used for grammatical elements, and Katakana, normally used for foreign and onomatopoeic words.
    - Characters associated with an ideographic writing system typically are encoded in more than one byte because the character repertoire has tens of thousands of characters.

The character set you choose uses one of the following types of encoding schemes:
- Single-Byte Encoding Schemes
    - 7-bit encoding schemes
    - 8-bit encoding schemes
- Multibyte Encoding Schemes
    - Fixed-width multibyte encoding schemes
    - Variable-width multibyte encoding schemes
    - Shift-sensitive variable-width multibyte encoding schemes
        - Shift-sensitive encoding schemes are used primarily on IBM platforms

UTF-8 character set.
- The ASCII characters requires one byte
- the Latin and Greek characters require two bytes
- the Asian character requires three bytes
- the supplementary character requires four bytes of storage.

#### UCS & Unicode
The `Universal Coded Character Set (UCS)` is a standard set of characters defined by the International Standard `ISO/IEC 10646`(plus amendments to that standard), which is the basis of many character encodings. The latest version contains over 136,000 abstract characters, each identified by an `unambiguous name` and an `integer number` called its `code point`. This `ISO/IEC 10646` standard is maintained in conjunction with The Unicode Standard (`Unicode`), and they are `code-for-code identical`.

The `UCS` has over 1.1 million possible code points available for use/allocation, but only the first 65,536 (the `Basic Multilingual Plane`, or `BMP`) had entered into common use before 2000. This situation began changing when the `People's Republic of China (PRC)` ruled in 2006 that all software sold in its jurisdiction would have to support `GB 18030`. This required software intended for sale in the PRC to move beyond the BMP.

##### Encoding forms
- `UCS-2`: use two bytes to represent a code point. Only support `BMP`
    - Occasionally, articles about Unicode will mistakenly refer to `UCS-2` as "`UCS-16`". `UCS-16` does not exist.
- `UTF-16`(Unicode Transformation Format)): amendment of `UCS-2`. Allows uses of code point other than `BMP` in pairs.
    - Unicode also adopted `UTF-16`, but in Unicode terminology, the high-half zone elements become "`high surrogates`" and the low-half zone elements become "`low surrogates`".
- `UCS-4`, uses four bytes (total 32 bits) to encode a code point.
- `UTF-8`, the dominant UCS encoding, is a variable-width encoding designed for backward compatibility with `ASCII`, and for avoiding the complications of `endianness` and `byte-order marks` in `UTF-16` and `UTF-32`
- `UTF-32`, Each 32-bit value in `UTF-32` represents one Unicode code point and is exactly equal to that code point's numerical value. `UTF-32` and `UCS-4` are identical.

##### Differences from Unicode
`ISO 10646` and `Unicode` have an identical repertoire and numbers—the same characters with the same numbers exist on both standards.

`ISO 10646` is a simple character map, an extension of previous standards like `ISO 8859`. In contrast, `Unicode` adds rules for `collation`, `normalization of forms`, and the `bidirectional algorithm for right-to-left scripts` such as Arabic and Hebrew.

To support these rules and algorithms, `Unicode` adds many properties to each character in the set such as properties determining a character’s default bidirectional class and properties to determine how the character combines with other characters.


### Character Reference
In `SGML`, `HTML` and `XML` documents, the logical constructs known as `character data` and `attribute values` consist of sequences of characters, in which each character can manifest directly (representing itself), or can be represented by a series of characters called a `character reference`, of which there are two types:
- `numeric character reference`
    - refers to a character by its `Universal Character Set`/`Unicode` code point, and uses the format:`&#nnnn;` or `&#xhhhh;`
    - `nnnn` is the code point in decimal form, and `hhhh` is the code point in hexadecimal form.
    - The `x` must be lowercase in XML documents.
- `character entity reference.`
    - refers to a character by the `name` of an entity which has the desired character as its replacement text.
    - with format: `&name;`, where `name` is the case-sensitive `name` of the entity. The semicolon is required, unless marked otherwise in the table below
    - An entity declaration is created by using the `<!ENTITY name "value">` syntax in a Document Type Definition (DTD).

#### Predefined entities in XML
The XML specification does not use the term "`character entity`" or "`character entity reference`". The XML specification defines five "`predefined entities`" representing special characters, and requires that all XML processors honor them.
- quot  "  U+0022 (34)  XML 1.0  quotation mark
- amp   &  U+0026 (38)  XML 1.0  ampersand
- apos  '  U+0027 (39)  XML 1.0  apostrophe (1.0: apostrophe-quote)
- lt    <  U+003C (60)  XML 1.0  less-than sign
- gt    >  U+003E (62)  XML 1.0  greater-than sign

