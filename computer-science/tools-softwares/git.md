`git branch -d`
`push.default=simple` 仅提交当前branch
`git checkout unittest`切换分支
`git checkout file/to/restore` 指定文件checkout
`git tag -a` 创建annotated tags，不加参数为lightweight tag
`git show v1.0.0`显示tag详细信息
`git push --tags` 或 `git push v1.0.0`提交tags
`git checkout -b version2 v2.0.0`这么做，如果再commit tag会被改变，所以尽量避免这样做，可以找到hash，手动checkout
`git reset --soft HEAD~1`取消上次的commit
`git push -u origin feature_branch_name`将本地branch push到origin
`git push origin --delete <branchName>`删除远端branch，tag可以用类似方法删除
`git push origin :<branchName>`删除远端branch，tag可以用类似方法删除
`git checkout master`之后执行git merge feature2，将feature2中新增内容merge到master上，如果master没动过就是fastforward
`git remote -v`
`git remote set-url origin <url>`
`git pull --rebase` 避免多余的merge commit
`git pull --prune` 删掉remote不存在的本地branch
`git commit --amend`
`git log --graph --oneline --all`
`git log --follow -p -- file`查看某文件的历史记录
`gitk [filename]`
`gitk --all`显示所有branch
`git reset --merge <>`将当前branch回归到某个点
`git diff`、diff都是得到的是new相对于old的变化diff old new

`git rebase --interactive` <要修改commit message的地方>
`git rebase master`，rebase到master上，同上，这样做后可能需要force push到origin
`git rebase -i --root`合并前两个commit
`git rebase --onto commit-id^ commit-id`去掉某个commit
`git rebase --onto master next topic`
`git rebase --root`可用来处理init commit

`git config --global --unset <config>`
`git reset --hard origin/master` 将本地branch设置成origin的HEAD
`git config --global core.pager 'less -x1,5'` 4个空格显示
`git config --global core.editor emacs`
`git apply`可用来`apply patch`，但会根据patch中的label自动匹配需要修改的文件

`git difftool`
- 默认使用diff.tool的配置
- 每个difftool可以设置 `difftool.<toolname>.path`和`difftool.<toolname>.cmd`,但标准支持的difftool只设置path即可或者放到PATH环境变量里
- `difftool`默认支持`meld`和`bc3`，这两个很好用
- 使用时加上`-d`可一次性比较所有文件，否则是线性比较

让centos自动补齐git
```
    for file in /etc/bash_completion.d/* ; do
        source "$file"
    done
```
`git rev-parse --abbrev-ref HEAD` 获得当前branch
`git show a2c25061` 显示某hash的内容

删掉branch中有关某些文件的历史
- git filter-branch --commit-filter 'if [ z$1 = z`git rev-parse $3^{tree}` ]; then skip_commit "$@"; else git commit-tree "$@"; fi' "$@"
- git filter-branch --tree-filter 'rm -rf my_folder' --prune-empty -f HEAD
- git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch Rakefile' HEAD
- git filter-branch --index-filter "git rm -r --cached --ignore-unmatch <file/dir>" HEAD

git log --all -- <path-to-file>
git show <SHA> -- <path-to-file>

清掉所有修改
- git clean -df
- git checkout -- .

设置git自动根据系统checkout特定的换行符
- find . -type f -not -path "./.git/*" -exec dos2unix {} \;
- git commit -a -m 'dos2unix conversion'
- echo "* text=auto" > .gitattributes
