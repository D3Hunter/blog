对于小数据量，短期存在的数据做序列化还行，长期数据，如果类结构变更较大，可能导致旧的数据无法反序列化。

大数据量下性能不好，且占内存，不建议使用。同样的对象，跟GSON相比，反序列化效率差了10几倍。

### System Architecture
The key to storing and retrieving objects in a serialized form is representing the state of objects sufficient to reconstruct the object(s). Objects to be saved in the stream may support either the Serializable or the Externalizable interface.

For `serializable objects`, the stream includes sufficient information to restore the fields in the stream to a compatible version of the class. For `Externalizable objects`, the class is solely responsible for the external format of its contents. For `Externalizable` objects, only the identity of the class of the object is saved by the container; the class must save and restore the contents.

Objects to be stored and retrieved frequently refer to other objects. Those other objects must be stored and retrieved at the same time to maintain the `relationships` between the objects. When an object is stored, all of the objects that are reachable from that object are stored as well.

The goals for serializing JavaTM objects are to:
- Have a simple yet extensible mechanism.
- Maintain the JavaTM object type and safety properties in the serialized form.
- Be extensible to support marshaling and unmarshaling as needed for remote objects.
- Be extensible to support simple persistence of JavaTM objects.
- Require per class implementation only for customization.
- Allow the object to define its external format.

Within a stream, the first reference to any object results in the object being serialized or externalized and the assignment of a handle for that object. Subsequent references to that object are encoded as the handle. Using object handles preserves sharing and circular references that occur naturally in object graphs. Subsequent references to an object use only the handle allowing a very compact representation.

Except for serializable fields, primitive data is written to the stream in block-data records, with each record prefixed by a marker and an indication of the number of bytes in the record.

ObjectOutputStream can be extended to customize the information about classes in the stream or to replace objects to be serialized. Refer to the `annotateClass` and `replaceObject` method descriptions for details. Refer to the `resolveClass` and `resolveObject` method for deserializing.

Default serializable fields of a class are defined to be the `non-transient` and `non-static` fields. This default computation can be overridden by declaring a special field in the Serializable class, `serialPersistentFields`. This field must be initialized with an array of `ObjectStreamField` objects that list the names and types of the serializable fields.
```java
class List implements Serializable {
    List next;

    private static final ObjectStreamField[] serialPersistentFields
                 = {new ObjectStreamField("next", List.class)};
}
```

The process by which `enum` constants are serialized cannot be customized.
