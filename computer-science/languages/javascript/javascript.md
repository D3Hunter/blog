document.getElementById('login').getElementsByTagName('input')[1].value
jQuery中可以按id class 和标签类型获取对象，分别为$('#id') $('.class') $('input:text')之类的

### Execution Context
Just like `functions/modules/packages` allow you to manage the complexity of writing code, `Execution Contexts` allow the JavaScript engine to manage the complexity of interpreting and running your code.

The first `Execution Context` that gets created when the JavaScript engine runs your code is called the “`Global Execution Context`”. Initially this `Execution Context` will consist of two things - a `global object` and a variable called `this`. `this` will reference the `global object` which will be `window` if you’re running JavaScript in the browser or `global` if you’re running it in a Node environment.

Each `Execution Context` has two separate phases, a `Creation` phase and an `Execution` phase and each phase has its own unique responsibilities. In the Global `Creation` phase, the JavaScript engine will:
- Create a `global object`.
- Create an object called `“this”`.
- Set up memory space for variables and functions.
- Assign variable declarations a default value of `“undefined”` while placing any function declarations in memory.

The only time an `Execution Context` is created is when the JavaScript engine first starts interpreting your code (Global Execution Context) and whenever a function is invoked.

In both the `browser` and in `Node`, if you create a variable without a declaration (ie without `var`, `let`, or `const`), that variable will also be added as a `property` on the `global object`. 如果是在function内，则只在function执行后才会获得值


### libraries
- Chart.js 绘制图表
