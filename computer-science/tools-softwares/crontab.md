EDITOR=vim crontab -e 编辑crontab, 可将job输出到文件

Crontab Environment
- `HOME=user’s-home-directory`
- `LOGNAME=user’s-login-id`
- `PATH=/usr/bin:/usr/sbin:.`
- `SHELL=/usr/bin/sh`

实现复杂逻辑最好使用脚本

### 格式
```
*     *     *   *    *        command(absolute path or relative to crontab HOME)
-     -     -   -    -
|     |     |   |    |
|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
|     |     |   +------- month (1 - 12)
|     |     +--------- day of        month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
```
- * in the value field above means all legal values as in braces for that column.
- The value column can have a * or a list of elements separated by commas.
- An element is either a number in the ranges shown above or two numbers in the range separated by a hyphen (meaning an inclusive range).
- Repeat pattern like `/2` for every 2 minutes is not supported by all operating systems.
- The specification of days can be made in two fields: month day and weekday. If both are specified in an entry, they are `cumulative` meaning both of the entries will get executed .


