将文件当作表来读取，可使用
- Mysql的CSV engine，但是需要重命名文件
- calcite的file adapter https://calcite.apache.org/docs/file_adapter.html
- PostgreSQL实现了SQL/MED的特性，对应数据叫foreign data。使用foreign data wrapper操作，操作csv使用file_fdw扩展
    - 这个功能为SQL标准：SQL/MED("Management of External Data", defined by ISO/IEC 9075-9:2008 (originally defined for SQL:2003)) External data is data that is accessible to, but not managed by, an SQL-based DBMS.
- Oracle对应的功能叫external table

一些工具可直接使用sql查询csv文件
- https://superuser.com/questions/7169/querying-a-csv-file
- https://pythonhosted.org/querycsv/
- https://github.com/mithrandie/csvq
- sqlite 也可以操作csv，但需要先导入
- https://github.com/wireservice/csvkit 这个star较多 https://towardsdatascience.com/analyze-csvs-with-sql-in-command-line-233202dc1241
- https://github.com/dinedal/textql 这个也挺好
- https://github.com/harelba/q 这个也还行
- https://github.com/cube2222/octosql

