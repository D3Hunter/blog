Lombok字节码自动插入，设置getter/setter/constructor等
inject code into a class at compile time

Java Compilation:
    .java --> Parse and Enter <--> Annotation Processing --> Analyse and Generate
        --> .class

hooks itself into the compilation process as an annotation processor
Normally, annotation processors only generate new source files whereas Lombok modifies existing classes.
The annotation processing API doesn't provide a mechanism for changing the AST of a class. The clever people at Project Lombok got around this through some unpublished APIs of javac.
using back-door APIs

@Data: All together now: A shortcut for @ToString, @EqualsAndHashCode, @Getter on all fields, and @Setter on all non-final fields, and @RequiredArgsConstructor!
@Builder can generate so-called 'singular' methods for collection parameters/fields. These take 1 element instead of an entire list, and add the element to the list.
    比如Person.builder().name("Savage x").city("San Francisco").job("Mythbusters").job("Unchained Reaction").build();
