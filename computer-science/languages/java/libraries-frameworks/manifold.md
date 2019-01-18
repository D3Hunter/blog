In object-oriented computer programming, an `extension method` is a method added to an object after the original object was compiled. The modified object is often a class, a prototype or a type. There is no syntactic difference between calling an extension method and calling a method declared in the type definition.

`lombok`通过`@ExtensionMethod`提供类似功能，目前属于实验接口

Extension methods are features of numerous languages including `C#`, `Java` via `Manifold`

`Manifold` is a unique framework to dynamically and seamlessly extend Java.
- `Type-safe Metaprogramming` – renders code generators obsolete, similar in concept to `F# type providers`
- `Extension Methods` – add methods to classes you don’t own, comparable to the same feature in `C#` and `Kotlin`
- `Structural Typing` – type-safe duck typing, much like interfaces in `TypeScript` and `Go`

At a high level each of these features is classified as either a `Type Manifold` or an Extension via the `Extension Manifold`.
- `Type Manifold` transforms a data source into a data type directly accessible in your Java code eliminating code generation build steps involved with conventional tools.

before

```
chocolate = Chocolate
chocolate.milk = Milk chocolate
chocolate.dark = Dark chocolate
```

and access with:

```java
Properties myProperties = new Properties();
myProperties.load(getClass().getResourceAsStream("/abc/MyProperties.properties"));
String myMessage = myProperties.getProperty("chocolate.milk");
```

using Type Manifold

```java
String myMessage = MyProperties.chocolate.milk;
```

- The `extension manifold` is a special kind of type manifold that lets you augment existing Java classes including Java’s own runtime classes such as String

before

``` java
public class MyStringUtil {
  public static void echo(String value) {
    System.out.println(value);
  }
}
```

and access with:

``` java
MyStringUtil.echo("Java");
```

using extension manifold:

```java
@Extension
public class MyStringExtension {
  public static void echo(@This String thiz) {
    System.out.println(thiz);
  }
}
```

and access with:

```java
"Java".echo();
```

