`picocli` - a mighty tiny command line interface

### 多值枚举配置项
```java
// 逗号分隔的多值配置，如果是`Enum`，`${COMPLETION-CANDIDATES}`可用来输出可用的值
@Option(names = {"-o", "--option"}, paramLabel = "option", split = ",", description = "Valid values: ${COMPLETION-CANDIDATES}")
private SomeEnum[] someEnums;

private boolean parseArguments(String[] args) {
    CommandLine commandLine = new CommandLine(this);
    // 对于enum允许case incensitive
    commandLine.setCaseInsensitiveEnumValuesAllowed(true);

    try {
        commandLine.parse(args);
    } catch (MissingParameterException exception) {
        // skip
    } catch (ParameterException exception) {
        System.out.println(exception.getMessage());
    }

    commandLine.usage(System.out);

    return false;
}
```
