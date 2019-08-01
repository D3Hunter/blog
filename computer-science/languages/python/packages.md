操作clipboard：`import pyperclip`

pandas: Python Data Analysis Library. 支持很多数据源，如csv、excel文件等。也可以用来读取excel文件内容

##### Excel
1. Building Interactive Python tools with Excel as a front-end
    - PyXLL – The Python Excel Add-In
    - pywin32, win32com and comtypes
    - xlwings
    - DataNitro
2. Reading and writing Excel workbooks
    - OpenPyXL：易用，不支持图片和图表，大文件较慢
    - XlsxWriter：写入快
    - XLTable：处理formula方便
    - Pandas：只处理数据，不关心格式时，很方便
    - xlrd and xlwt：用来处理旧的xls file format

#### lxml
`python 3.7`的实现里，不在能通过`XMLTreeBuilder`来保持`attribute`顺序，但可修改`ElementTree.py`中的`_serialize_xml`，把输出`attribute`部分中的`sorted`去掉（有一行注释：`lexical order`）

