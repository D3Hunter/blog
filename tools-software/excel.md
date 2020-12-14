打开以逗号分割的`csv`文件:
- `Data tab` -> `text to columns`
- 在`csv`文件开头添加`sep=,`
- `Excel`默认使用`system List separator`分割`csv`文件
    - `Windows`可以通过`Control Panel -> Region -> Additional settings`
    - `OSX`通过`System Preferences > Language & Region > Advanced > General.`
        - If your region uses commas (,) for decimal, then Excel will save using semi-colons (;)
        - If it uses a decimal point (.), then it will delimit with commas (,).
- `Excel`内部也可以通过`Options -> Advanced`来设置

`CSV`文件中直接添加换行，可以将cell内容放到双引号内，然后直接使用换行即可
- mac下得使用`CRLF`作为换行符，不然Excel不识别
- 如果使用程序输出，mac下还可以把行换行符设置为LF，cell内为CR

mac下，Excel默认使用local字符集来打开`CSV`文件，所以需要将文件输出为`gb2312`等字符集

