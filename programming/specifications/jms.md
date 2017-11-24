### Message Acknowledgments 
With this knowledge the JMS provider can manage the distribution of messages and guarantee their delivery.
- `AUTO_ACKNOWLEDGE`: With `AUTO_ACKNOWLEDGE` mode the acknowledgment is always the last thing to happen implicitly after the onMessage() handler returns.
- `DUPS_OK_ACKNOWLEDGE`: This acknowledgment mode instructs the session to lazily acknowledge the delivery of messages. This is likely to result in the delivery of some duplicate messages if the JMS provider fails, so it should only be used by consumers that can tolerate duplicate messages.
- `CLIENT_ACKNOWLEDGE`: The use of `CLIENT_ACKNOWLEDGE` allows the application to control when the acknowledgment is sent.

### Destination
A Destination object encapsulates a `provider-specific` address. The JMS API does not define a standard address syntax.
A Destination object is a JMS administered object.
It is expected that JMS providers will provide the tools an administrator needs to create and configure administered objects in a `JNDI` namespace. JMS provider implementations of administered objects should implement the `javax.naming.Referenceable` and `java.io.Serializable` interfaces so that they can be stored in all `JNDI` naming contexts. In addition, it is recommended that these implementations follow the JavaBeansTM design patterns.
- Queue
- TemporaryQueue
- TemporaryTopic
- Topic
