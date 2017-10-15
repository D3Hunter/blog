requires jdk `1.7+`

### gradle wrapper
it is not necessary for Gradle to be installed to use the `Gradle wrapper`. `gradlew` will download and cache `gradle`

#### files needed
- gradlew (Unix Shell script)
- gradlew.bat (Windows batch file)
- gradle/wrapper/gradle-wrapper.jar (Wrapper JAR)
- gradle/wrapper/gradle-wrapper.properties (Wrapper properties)

### 常用命令
创建wrapper：`gradle wrapper --gradle-version 2.0`
查看帮助 `gradle help --task xxx`
项目属性 `gradle properties`
显示所有task `gradle tasks --all`
去掉task `gradle -x xxxx`
包依赖 `gradle dependencies --configuration xxxxx`
task tree 使用`com.dorongold.task-tree`插件：`gradle help --task taskTree`

### gradle vs maven
Gradle is based on a graph of task dependencies, where the tasks do the work. Maven uses a model of fixed, linear phases to which you can attach goals (the things that do the work). 

### migrating from maven
根据`pom.xml`自动处理：`gradle init`

### Build phases
- Initialization
- Configuration
- Execution
```
println 'This is executed during the configuration phase.'

task configured {
    println 'This is also executed during the configuration phase.'
}

task test {
    doLast {
        println 'This is executed during the execution phase.'
    }
}
```

### plugins
`maven plugin`: The Maven plugin adds support for deploying artifacts to Maven repositories.
`maven publish`: publish build artifacts to an Apache Maven Repository. 
`nebula.os-package`: constructing linux packages, specifically RPM and DEBs.
`nebula.ospackage`: Provides a task similar to Tar and Zip for constructing RPM and DEB package files.
`com.jfrog.bintray`: A Gradle plugin for publishing to Bintray

### Gradle Build Language Reference (DSL)
A build script can contain any Groovy language element. [6] Gradle assumes that each build script is encoded using UTF-8
每个block都是一个`task`，要么来自`project/script`或者来自`plugin`，比如`compileTestJava`来自`java plugin`
`gradle.taskGraph`包含task的DAG
`plugins`与`apply plugin`区别在于？？前者较新

#### project API
Any method you call in your build script which is not defined in the build script, is delegated to the Project object.
Any property you access in your build script, which is not defined in the build script, is delegated to the Project object.
#### Extra properties
Extra properties can be added, read and set via the owning object's ext property. Alternatively, an ext block can be used to add multiple properties at once.


### multiple project
To define a multi-project build, you need to create a `settings` file.
Multi-project builds are always represented by a tree with a single root. Each element in the tree represents a project.

### dependencies
In Gradle dependencies are grouped into `configurations`. A `configuration` is simply a named set of dependencies. We will refer to them as `dependency configurations`
- compile
- runtime
- testCompile
- testRuntime
An `external dependency` is identified using group, name and version attributes. 
Dependency configurations are also used to publish files.[2] We call these files `publication artifacts`, or usually just `artifacts`.

If your build script needs to use external libraries, you can add them to the script's classpath in the build script itself. You do this using the `buildscript()`

### task
自定义的task需要手动`execute`
task依赖需要是一个DAG
`group`指定`task`所属的组（通过`gradle tasks --all`得到的分组）
