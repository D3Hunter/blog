`retrace`可以把混淆后的堆栈还原回来，也可以自定义，还原某些日志中的字段

`-outjars`用来保存前面的所有`-injars`（直到上个outjars为止）

可以在文件中使用java properties，如`<java.home>`会从`System.getProperty`获取

`-adaptresourcefilenames`只支持对相同目录下的resource文件做处理，因此不能用来处理SPI

目前proguard 6有bug，开启`-adaptclassstrings`后，就把`java.lang.String[]`变成`java.lang.String`，可通过`Class.getCanonicalName`规避

默认会对enum做清理，需要使用如下，保证字段被保留
```
-keepclassmembers enum * {
    <fields>;
    public static **[] values();
    public static ** valueOf(java.lang.String);
}
```

#### 如果使用反射或SPI，最好加上如下
- `-adaptclassstrings`
- `-adaptresourcefilecontents`

#### 如果使用Annotation，保留如下。
- `-keepattributes RuntimeVisible*Annotations`
- `-keepattributes Signature`

#### 保留行号并重命名SourceFile有助于使用retrace还原堆栈
- `-renamesourcefileattribute SourceFile`
- `-keepattributes SourceFile,LineNumberTable`

#### 如果需要保留内类，比如lombok生成的builder类
设置`-keepattributes InnerClasses`

### 其他配置项
- proguard保留类名同时会保留包名，除非`-applymapping mapping.txt`
- `-useuniqueclassmembernames`这个有可能不管用
- `-repackageclasses`把混淆的类放到同一个包下面, 配合`-classobfuscationdictionary windows.txt`可以为混淆类赋予不同的名字
    - 一下脚本可以生成随机名称
    - 需要在`spring``mybatis`等设置的Scan目录下
``` python
import string
element=list(string.ascii_lowercase)
def gen_alphabet_seq(length):
    if length == 1:
        return element
    result = []
    sub_result = gen_alphabet_seq(length-1)
    for ele in element:
        tmp_result = [ele + item for item in sub_result]
        result += tmp_result
    return result

for ele in gen_alphabet_seq(3):
    print ele
```
- `-keepparameternames`对于`keep`的`method`，同时保留`method`的`parameter`
- `-dontusemixedcaseclassnames`，如果要在mac／windows上混淆一个目录，加上因为文件系统不支持大小写导致类文件重复
