The `comm` utility reads `file1` and `file2`, which should be `sorted` lexically, and produces three text columns as output:
- lines only in file1;
- lines only in file2;
- lines in both files.

可以用来在文件级别做`A & B`,`A - B`和`B - A`操作

The `comm` utility assumes that the files are lexically sorted; all characters participate in line comparisons. 并受很多环境变量影响，比如`LC_COLLATE`，最好使用`sort`来排序（外部工具排序的结果可能不受这些环境变量影响），否则`comm`的结果可能不正确：
- `sort -o A.txt A.txt`
- `sort -o B.txt B.txt`
- `comm A.txt B.txt`
