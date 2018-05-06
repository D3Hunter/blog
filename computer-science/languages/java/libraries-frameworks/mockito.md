Mock系统类(比如nio.file.Files)需要在@PrepareForTest中指定需要使用系统类的类，
    且添加@RunWith(PowerMockRunner.class)，普通的static类不需要
PowerMockito.mockStatic来mock static类
whenNew(Second.class).withNoArguments()可用mock constructor，但不推荐这么做
可以verify某函数调用次数

在when和verify部分，函数调用参数必须全部是matcher或全部是matcher，对于常量
    可以使用eq等函数将其转换成matcher
