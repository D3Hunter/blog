It is used to join files horizontally (parallel merging) by outputting lines consisting of lines from each file specified,

    $ cat state
    Arunachal Pradesh
    Assam
    Andhra Pradesh
    Bihar
    Chhattisgrah

    $ cat capital
    Itanagar
    Dispur
    Hyderabad
    Patna
    Raipur

    $ paste number state capital
    1       Arunachal Pradesh       Itanagar
    2       Assam   Dispur
    3       Andhra Pradesh  Hyderabad
    4       Bihar   Patna
    5       Chhattisgrah    Raipur

`-s (serial)`: We can merge the files in sequentially manner using the -s option. It reads all the lines from a single file and merges all these lines into a single line with each line separated by tab.

    $ paste -s number state capital
    1       2       3       4       5
    Arunachal Pradesh       Assam   Andhra Pradesh  Bihar   Chhattisgrah
    Itanagar        Dispur  Hyderabad       Patna   Raipur

可以用来跟生成表达式给`bc`: `cat numbers.txt | paste -sd+ | bc -l`

### Applications
这里的每个`-`都代表其数据来自于stdin
1. Combining N consecutive lines:

    With 2 hyphens
    $ cat capital | paste - -
    Itanagar        Dispur
    Hyderabad       Patna
    Raipur

    With 3 hyphens
    $ paste - - - < capital
    Itanagar        Dispur  Hyderabad
    Patna   Raipur

2. Combination with other commands:

    Without hypen
    $ cut -d " " -f 1 state | paste number
    1
    2
    3
    4
    5

    With hypen
    $ cut -d " " -f 1 state | paste number -
    1       Arunachal
    2       Assam
    3       Andhra
    4       Bihar
    5       Chhattisgrah
