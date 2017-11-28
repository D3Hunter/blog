You can run `go install` to install the binary into your workspace's bin directory or `go clean` to remove it.
The Go binary distributions assume they will be installed in `/usr/local/go`, to install the Go tools to a different location, you must set the `GOROOT` environment variable to point to the directory in which it was installed.

### GOPATH
The `GOPATH` environment variable specifies the location of your workspace. It defaults to a directory named `go` inside your home directory
If you would like to work in a different location, you will need to set `GOPATH` to the path to that directory. Note that `GOPATH` must not be the same path as your `Go installation`.
The command `go env GOPATH` prints the effective current `GOPATH`; it prints the default location if the environment variable is unset. 
如果是默认的，没必要显示设置这个环境变量
### Code organization
- Go programmers typically keep all their Go code in a single `workspace`.
- A `workspace` contains many version control `repositories` (managed by Git, for example).
- Each `repository` contains one or more `packages`.
- Each `package` consists of one or more `Go source` files in a single directory.
- The path to a `package`'s directory determines its `import path`.
Note that this differs from other programming environments in which every project has a separate workspace and workspaces are closely tied to version control repositories.
### Workspaces
A workspace is a directory hierarchy with three directories at its root:
- src contains Go source files,
- pkg contains package objects, and
- bin contains executable commands.

### import paths
An `import path` is a string that uniquely identifies a `package`. A package's import path corresponds to its location inside a `workspace` or in a `remote repository` (explained below).
