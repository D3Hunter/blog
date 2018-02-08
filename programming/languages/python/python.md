### libraries:
pexpect: expect的python版本
virtualenv: create isolated Python environments

### Requirements files
pip install -r requirements.txt

use 'import modu' over 'from modu import sqrt' over 'from modu import *' to
    increase readalibity and understandability
Any directory with an `__init__.py` file is considered a Python package.
In Python, everything is an object, and can be handled as such.
Carefully isolating functions with context and side-effects from functions with logic (called pure functions)
A `decorator` is a function or a class that wraps (or decorates) a function or a method.
A `context manager` is a Python object that provides extra contextual information to an action.
Dynamic typing
Python has two kinds of built-in or user-defined types. Mutable and immutable types
    Typical mutables are lists and dictionaries. tuple and string is immutables
    字符串拼接用list的join更高效：list comprehensions，如果个数固定用‘+’也可以
We are all responsible users: no explicit `private`
PEP 8 is the de-facto code style guide for Python.
`list comprehensions` can be used to construct lists in a very natural, easy way, like a mathematician is used to do.

## Idioms
- Unpacking
    for index, item in enumerate(some_list):
    a, b = b, a
    a, (b, c) = 1, (2, 3)
- Create an ignored variable
    basename, __, ext = filename.rpartition('.')
- Create a length-N list of the same thing
    four_nones = [None] * 4
- Create a length-N list of lists
    Because lists are mutable, the * operator (as above) will create a list of N references to the same list
    four_lists = [[] for __ in xrange(4)]
- Create a string from a list
    letters = ['s', 'p', 'a', 'm']
    word = ''.join(letters)
- Searching for an item in a collection
    use set/directories which use hashtable for better performance
    'list''ll iterate whole list

### Conventions
- Check if variable equals a constant
    if attr:
    if not attr:
    if attr is None:
- Access a Dictionary Element
    Don’t use the `dict.has_key()` method. Instead, use `x in d` syntax,
    or pass a default argument to `dict.get()`.
- Short Ways to Manipulate Lists
    List comprehensions provide a powerful, concise way to work with lists.
    Also, the map() and filter() functions can perform operations on lists
    using a different, more concise syntax.
- Read From a File
    Use the `with open` syntax to read from files.
- Line Continuations
    A better solution is to use parentheses around your elements.

python -m site --user-site

### basic:
command line argument: import sys; len(sys.argv); sys.argv
[] list, () tuple, {} dict
str.split(strtok)
and or not
def functionname( parameters ):
for x in range(5): 或者xrange
time.sleep(t)
SimpleHTTPServer: This class serves files from the current directory and below
print '%d, %f' % (1, 2.3)
merged_list = list1 + list2

`*` unpacks the sequence/collection into positional arguments
    def sum(a, b):
        return a + b
    values = (1, 2)
    s = sum(*values)       ======      s = sum(1, 2)
    values = { 'a': 1, 'b': 2 }
    s = sum(**values)      ======      s = sum(1, 2)
需要f = staticmethod(f)才能成为static method，同理f = classmethod(f)
sys.argv 0为脚本
pip install virtualenvwrapper
访问全局变量，需要在方法中指定：global variable

Trailing comma is required for one-element tuples
删除某变量`del variable`

千位转换：`'{0:,}'.format(1000000)`,反向转换可以去掉`,`或使用locale
int转hexstr: `'0x{:02x}'.format(integer)`
hexstr转int: `int(str, 16)`

添加寻找路径`sys.path.append`,然后即可import
python默认会缓存某个已经加载过的module，使用`reload`强制重新加载

Enum类：`Python 3.4` as described in `PEP 435`,之前需要自己实现
`func_dict` 等同于 `__dict__`，但尽量用后者，python3去掉了前者

python中`/`是浮点除法，在大数处理时会有精度损失，可使用`decimal`，`//`为整形除法

python按位取反操作`~`，是按有符号的方式处理的

python如果有非`daemon thread`运行是不会退出的，`os._exit`会全部退出，但是不会执行相应的清理任务。

`dict`没有`contains`，需要用`xxx in dict`和`xxx not in dict`

`2to3`可以把python2的代码专程python3的代码

遍历文件的每一行：`for line in stream:`

### Problems
`TypeError: __call__() takes exactly 2 arguments (1 given)`: pip install setuptools==33.1.1

## method & function
- A method is on an object.
- A function is independent of an object.
- For Java, there are only methods.
- For C, there are only functions.
- For C++/python it would depend on whether or not you're in a class.

## descriptor
In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol. both `__get__()` and `__set__()`, it is considered a data descriptor
only define `__get__()` are called non-data descriptors
Data and non-data descriptors differ in how overrides are calculated, with respect to entries in an instance’s dictionary.

### BuiltIn Functions
- `__import__`: import a module whose name is only known at runtime
- `hasattr`: by calling getattr(object, name) and seeing whether it raises an exception or not.
- `isinstance`
- `str`: 字符串类型，Return a string containing a nicely printable representation of an object.
- `dict`: Create a new dictionary. The dict object is the dictionary class.
- `object`: Return a new featureless object. object is a base for all new style classes.
- map(function, iterable, ...) Apply function to every item of iterable and return a list of the results.
- `slice`: Extended Slices since python 1.4, Python's built-in list, tuple, and string sequence types have supported this feature since Python 2.3: `str[::-1]` reverse `str`

### String prefixs
The `b` prefix signifies a `bytes` string literal.
The `r` means that the string is to be treated as a raw string, which means all escape codes will be ignored.

### New-style and classic classes
Up to Python 2.1, old-style classes were the only flavour available to the user. The concept of (old-style) class is unrelated to the concept of type: if x is an instance of an old-style class, then `x.__class__` designates the class of x, but `type(x)` is always `<type 'instance'>.` This reflects the fact that all old-style instances, independently of their class, are implemented with a single built-in type, called `instance`.

New-style classes were introduced in Python 2.2 to unify classes and types.
If x is an instance of a new-style class, then type(x) is the same as `x.__class__`.

For compatibility reasons, classes are still `old-style by default`. New-style classes are created by specifying another new-style class (i.e. a type) as a parent class, or the "top-level type" `object` if no other parent is needed.

### `__getattr__` and `__getattribute__`
You can also tell a class how to deal with attributes which it doesn't explicitly manage and do that via `__getattr__` method.
If you need to catch every attribute regardless whether it exists or not, use `__getattribute__` instead.

### special attribute of object
`object.__dict__`: A dictionary or other mapping object used to store an object’s (writable) attributes.

By definition, if a module has a `__path__` attribute, it is a package, regardless of its value.

### Packages/Modules
- `asynchat` — Asynchronous socket command/response handler, simplifying asynchronous clients and servers and making it easier to handle protocols whose elements are terminated by arbitrary strings, or are of variable length.
- `SocketServer` module simplifies the task of writing network servers.
- `struct` — Interpret strings as packed binary data
### GIL
`The Global Interpreter Lock (GIL)` is used internally to ensure that only one thread runs in the Python VM at a time. In general, Python offers to switch among threads only between bytecode instructions; how frequently it switches can be set via sys.setcheckinterval. Each bytecode instruction and therefore all the C implementation code reached from each instruction is therefore atomic from the point of view of a Python program.

In theory, this means an exact accounting requires an exact understanding of the PVM bytecode implementation. In practice, it means that operations on shared variables of builtin data types (int, list, dict, etc) that “look atomic” really are.
这也意味着无论在python中起几个线程，最多只能用满一个cpu核，其他解释器实现可能不会使用GIL

### Virtual Environment
- sudo pip install virtualenv virtualenvwrapper
- source /usr/local/bin/virtualenvwrapper.sh
- mkvirtualenv xxx
    - export VIRTUALENV_PYTHON=/usr/bin/python3
    - mkvirtualenv -a myproject myenv
    - 或者使用`--python=python3` or `-p python3`
- workon xxx

### 问题
osx上pip有时会卸载`Uninstalling six-1.4.1`失败，可以先忽略掉`--ignore-installed six`，这样有可能出现其他问题
- 参考https://github.com/pypa/pip/issues/3165

### json
json.dumps/loads

### Servers using Web Server Gateway Interface v1.0 (WSGI)
WSGI in a nutshell is an interface between a web server and the application itself.
1. CherryPy WSGI Server. CherryPy is actually a web framework. Yet it is a fully self-contained one
2. Gunicorn is a stand-alone web server which offers quite a bit of functionality in a significantly easy to operate fashion.
3. Tornado is an application development framework and a networking library designed for handling asynchrnous operations,
4. Twisted Web is the web server that comes with the Twisted networking library. Whereas Twisted itself is "an event-driven networking engine", the Twisted Web server runs on WSGI and it is capable of powering other Python web applications.
5. uWSGI itself is a vast project with many components, aiming to provide a full [software] stack for building hosting services
6. Waitress is a pure-Python WSGI server.
7. mod_python is an Apache module that embeds Python within the server itself.(dead?)

### PEP
`Benevolent Dictator For Life (BDFL)` is a title given to a small number of open-source software development leaders, typically project founders who retain the final say in disputes or arguments within the community.

`Top level module` is the topmost one

    top_module(这一层目录上面没有__init__.py)
        __init__.py
        moduleX.py

### PEP 8
David Goodger describes the PEP 8 recommendations as follows:
- `joined_lower` for functions, methods, attributes, variables
- `joined_lower` or ALL_CAPS for constants
- `StudlyCaps` for classes
- `camelCase` only to conform to pre-existing conventions

#### PEP 328 Imports: Multi-Line and Absolute/Relative
since `python 2.4` `21-Dec-2003`
解决import过长及多个相同名称的package的问题
it is proposed that all `import` statements be `absolute` by default (searching sys.path only) with special syntax `(leading dots)` for accessing package-relative imports.
Relative imports must always use `from <> import`; `import <>` is always absolute.

Relative imports use a module's `__name__` attribute to determine that module's position in the package hierarchy. If the module's name does not contain any package information (e.g. it is set to '`__main__`') then relative imports are resolved as if the module were a top level module, regardless of where the module is actually located on the file system.
- 这意味着使用 relative import，需要以package（`python -m foo.bar`）形式运行，否则容易报错`ValueError: Attempted relative import beyond toplevel package`
- 参考`PEP 366`和`PEP 338`

### PEP 366 -- Main module explicit relative imports
since `python 2.6` `1-May-2007`
By adding a new module level attribute, this PEP allows relative imports to work automatically if the module is `executed using the -m switch`. A small amount of boilerplate in the module itself will allow the relative imports to work when the file is `executed by name`.
The major proposed change is the introduction of a new module level attribute, `__package__`. When it is present, relative imports will be based on this attribute rather than the module `__name__` attribute.

Note that it is `not enough` to simply have the directory containing the module in `sys.path`, the corresponding package needs to be `explicitly imported`.

    if __name__ == "__main__" and __package__ is None:
        import sys, os
        # 这里假设当前脚本位于top level module目录内
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(1, parent_dir) # 需要放到前面，免得被系统的package覆盖导致找不到
        import xxxxxx
        __package__ = str("xxxxxx")
        del sys, os
这个relative import是个大坑，使用时注意
### PEP 338 -- Executing modules as scripts
The -m switch provides a benefit here, as it `inserts the current directory into sys.path`, instead of the directory contain the main module. 
the main goal of the `-m` switch -- to allow the full Python namespace to be used to locate modules for execution from the command line.
### PEP 263 -- Defining Python Source Code Encodings
This PEP proposes to introduce a syntax to declare the encoding of a Python source file. 
To define a source code encoding, `a magic comment` must be placed into the source files either as `first or second line` in the file.
More precisely, the first or second line must match the following regular expression:

    ^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)
