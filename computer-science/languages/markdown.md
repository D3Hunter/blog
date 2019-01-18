一般的markdown实现都可以在其中直接内嵌html页面

### 命令行查看markdown／prettify工具
1. grip（支持github风格）
    - `pip install grip`
    - `grip README.md 80`
    - `grip README.md --export index.html`
    - `cat README.md | grip -`
    - `cat README.md | grip --export - | less`
2. pandoc
    - `brew install pandoc`
    - `pandoc README.md`
3. showdown
    - `npm install showdown -g`
    - `showdown makehtml -i README.md -o output.html --tables`
4. marked(速度很快)
    - `npm install -g marked`
    - `marked -i README.md -o output.html`
5. prettier(格式化，上面的会转成html)
    - `npm install --g prettier`
    - `prettier README.md | less`

