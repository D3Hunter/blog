### Concepts
- goals: aka Mojo - Maven plain Old Java Object
#### Usefull commands
plugin 帮助: `mvn help:describe -Dplugin=war -Dfull=true`

`parent-child`关系，`child`是依赖`parent`先执行完的，因此希望在`parent`中添加`assembly`，会先走`parent`的a`ssembly`再去处理`child`。可通过以下方式解决
- 将`assembly`放到最后一个child中，或新建一个child（最后一个child）
- 在parent中去掉assembly的`execute`部分，通过两阶段执行来处理`mvn package assembly:single`

`-DrepositoryId=antpool`决定了通过`settings.xml`中的哪个`server`获取credentials

### Questions
#### Create empty mvn project
`mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false`

#### Config mirror repository
`settings.xml`配置中，更改mirror，修改repository地址：
- `http://maven.oschina.net/content/groups/public/`
- `http://maven.aliyun.com/nexus/content/groups/public`
`<mirrorOf>*</mirrorOf>`

### Plugins
- maven-compiler-plugin: set `source` and `target`
- maven-resources-plugin
    - source file encoding
    - copy resources to build directory
- maven-jar-plugin
- maven-assembly-plugin
    - 去掉最后的id`<appendAssemblyId>false</appendAssemblyId>`
    - 文件名称`<finalName>`
    - 如果生成`dir`会警告`is not a regular file`, 在配置添加：`<attach>false</attach>`
    - Entry longer than 100 characters: `<tarLongFileMode>gnu</tarLongFileMode>`
- maven-antrun-plugin: 解压文件

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
