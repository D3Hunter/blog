打开以逗号分割的`csv`文件:
- `Data tab` -> `text to columns`
- 在`csv`文件开头添加`sep=,`
- `Excel`默认使用`system List separator`分割`csv`文件
    - `Windows`可以通过`Control Panel -> Region -> Additional settings`
    - `OSX`通过`System Preferences > Language & Region > Advanced > General.`
        - If your region uses commas (,) for decimal, then Excel will save using semi-colons (;)
        - If it uses a decimal point (.), then it will delimit with commas (,).
- `Excel`内部也可以通过`Options -> Advanced`来设置
