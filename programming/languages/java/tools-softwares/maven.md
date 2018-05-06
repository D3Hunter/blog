### Concepts
- goals: aka Mojo - Maven plain Old Java Object
#### Usefull commands
plugin 帮助: `mvn help:describe -Dplugin=war -Dfull=true`

`parent-child`关系，`child`是依赖`parent`先执行完的，因此希望在`parent`中添加`assembly`，会先走`parent`的a`ssembly`再去处理`child`。可通过以下方式解决
- 将`assembly`放到最后一个child中，或新建一个child（最后一个child）
- 在parent中去掉assembly的`execute`部分，通过两阶段执行来处理`mvn package assembly:single`

`-DrepositoryId=antpool`决定了通过`settings.xml`中的哪个`server`获取credentials

### Questions
Create empty mvn project
`mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false`

Config mirror repository
`settings.xml`配置中，更改mirror，修改repository地址：
- `http://maven.oschina.net/content/groups/public/`
- `http://maven.aliyun.com/nexus/content/groups/public`
`<mirrorOf>*</mirrorOf>`

dependency repositories和plugin epositories需要使用独立的tag来指定
- reposittories
- pluginRepositories

### Plugins
- maven-compiler-plugin: set `source` and `target`
- maven-resources-plugin
    - source file encoding
    - copy resources to build directory
- maven-jar-plugin
    - addMavenDescriptor设为false去掉jar中的pom
- maven-assembly-plugin
    - 去掉最后的id`<appendAssemblyId>false</appendAssemblyId>`
    - 文件名称`<finalName>`
    - 如果生成`dir`会警告`is not a regular file`, 在配置添加：`<attach>false</attach>`
    - Entry longer than 100 characters: `<tarLongFileMode>gnu</tarLongFileMode>`
    - attach = false, 避免assembly生成的文件被deploy
    - dependencySet allows inclusion and exclusion of project dependencies in the assembly
    - dependencySet 如果没有include默认是当前module的依赖
    - Transitive*, 传递依赖相关配置
    - outputFileNameMapping可设置dependency的最终名称，不仅对module有效，对三方依赖也有效
- maven-antrun-plugin: 解压文件
- maven-dependency-plugin
    - 拷贝依赖
    - unpack某个artifact，比如jre，如果是本地文件，使用maven-antrun-plugin
    - 有时模块间相互依赖，执行`dependency:tree`会提示下载不到依赖，可先去掉在执行，并不影响看到当前pom中的其它依赖
- maven-git-commit-id-plugin
    - 添加git相关信息

### Maven Default Lifecycle Phases
- validate
- generate-sources
- process-sources
- generate-resources
- process-resources
- compile
- process-classes
- generate-test-sources
- process-test-sources
- generate-test-resources
- process-test-resources
- test-compile
- test
- prepare-package (maven 2.1+)
- package
- pre-integration-test
- integration-test
- post-integration-test
- verify
- install
- deploy

### Nexus
Groups allow you to combine multiple repositories and other repository groups in a single URL.
Nexus ships with one group: `public`. The Public Repositories group combines the multiple important external proxy repositories like the Central Repository with the hosted repositories: `3rd Party`, `Releases`, and `Snapshots`.

`Return code is: 400`: 确认下地址使用的group还是某个具体的repository，
- repository: http://host:port/nexus/content/repositories/thirdparty/
- group: http://host:portnexus/content/groups/public/

upload example, `repositoryId`用户得到对应的`Server credentials`
- `mvn deploy:deploy-file  -Durl=http://host:port/nexus/content/repositories/thirdparty/ -DrepositoryId=repositoryId -Dfile="jre-1.8.151-linux-x64.zip"  -DgroupId=com.oracle  -DartifactId=jre  -Dversion=1.8.151  -Dpackaging=zip  -Dclassifier=linux-x64`

### Dependency Scope
Dependency scope is used to limit the transitivity of a dependency, and also to affect the classpath used for various build tasks.
- compile: This is the default scope, used if none is specified. Compile dependencies are available in all classpaths of a project.
- provided: This is much like compile, but indicates you expect the JDK or a container to provide the dependency at runtime. For example, when building a web application for the Java Enterprise Edition, you would set the dependency on the Servlet API and related Java EE APIs to scope provided because the web container provides those classes. This scope is only available on the compilation and test classpath, and is not transitive.
- runtime: It is in the runtime and test classpaths, but not the compile classpath.
- test: only available for the test compilation and execution phases. This scope is not transitive.
- system: The artifact is always available and is not looked up in a repository.
- import
