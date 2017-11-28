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

### Packages
asynchat — Asynchronous socket command/response handler, simplifying asynchronous clients and servers and making it easier to handle protocols whose elements are terminated by arbitrary strings, or are of variable length.