`retrace`可以把混淆后的堆栈还原回来，也可以自定义，还原某些日志中的字段

`-outjars`用来保存前面的所有`-injars`（直到上个outjars为止）

可以在文件中使用java properties，如`<java.home>`会从`System.getProperty`获取

`-adaptresourcefilenames`只支持对相同目录下的resource文件做处理，因此不能用来处理SPI

目前proguard 6有bug，开启`-adaptclassstrings`后，就把`java.lang.String[]`变成`java.lang.String`，可通过`Class.getCanonicalName`规避

默认会对enum做清理，需要使用如下，保证字段被保留

    -keepclassmembers enum * {
        <fields>;
        public static **[] values();
        public static ** valueOf(java.lang.String);
    }

如果使用反射或SPI，最好加上如下
- `-adaptclassstrings`
- `-adaptresourcefilecontents`

如果使用Annotation，保留如下。
- `-keepattributes RuntimeVisible*Annotations`
- `-keepattributes Signature`

保留行号并重命名SourceFile有助于使用retrace还原堆栈
- `-renamesourcefileattribute SourceFile`
- `-keepattributes SourceFile,LineNumberTable`

