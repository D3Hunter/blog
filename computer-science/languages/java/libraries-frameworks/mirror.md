`Mirror` was created to bring light to a simple problem, usually named `ReflectionUtil`, which is on almost all projects that rely on reflection to do advanced tasks.

before

``` java
//Let's just set a field value. Should be a simple task, right?

//"target" is the object containing the field whose value you want to set.
Field toSet = null;
for (Field f : target.getClass().getDeclaredFields()) {
    //Get all fields DECLARED inside the target object class
    if (f.getName().equals("field")) {
        toSet = f;
    }
}
if (toSet != null && (toSet.getModifiers() & Modifier.STATIC) == 0) {
    toSet.setAccessible(true);
    toSet.set(target, value);
}
```

or in a `procedural` way:

```java
ReflectionUtil.setField(target, fielName, value);
```

with mirror

``` java
new Mirror().on(target).set().field(fieldName).withValue(value);
```

