使用`deflateInit`压缩的，需要使用`inflateInit`，或者使用`inflateInit2`，`wbit`为`15`或者
- `MAX_WBITS+17`,文档上写15可以，但32(MAX_WBITS+17)为什么也可以？另外
- MAX_WBITS+32可自动判断zlib/gzip，+16只能是gzip

`zlib/gzip/zip`通常都是使用`DEFLATE`压缩数据格式，但`wrapper（header和trailer）`不同，
- <None>/.gz/.zip是上面数据格式对应的文件后缀，其中zlib wrapper一般在png文件中使用
- `.gz`仅针对单个文件，因此常与`.tar`一起使用；`.zip`是归档。
### `gzip/zip`命令
- 前者和zlib的gzip wrapping一样，只是gzip wrapping的header中name等字段为空
- `zip`等同于tar后执行compress，但一般的压缩算法为`deflate`
### `zlib`是一个库，支持三种在DEFLATE格式上的`Wrapping`：
- raw deflate(no wrapping)，
- zlib wrapping(png格式使用)
    header一般只有两个字节，标明method和windowbits；trailing为4字节,adler-32校验和
- gzip wrapping
- zlib/gzip warpping的区别在于前者更紧凑，adler-32校验速度快于后者使用crc32校验
### window bits:
- -15 ~ -8 raw deflate
- 8 ~ 15 zlib wrapping
- 24 ~ 31 gzip wrapping (header和trailing基本为空), (可以使用gunzip工具解压)