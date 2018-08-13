### XML spec

[Definition: An XML document may consist of one or many storage units. These are called `entities`; they all have content and are all (except for the `document entity` and the external DTD subset) identified by `entity name`.] Each XML document has one entity called the `document entity`, which serves as the starting point for the XML processor and may contain the whole document.

[Definition: A `parsed entity` contains `text`, a sequence of characters, which may represent markup or character data.]

[Definition: An `unparsed entity` is a resource whose contents may or may not be `text`, and if `text`, may be other than XML. Each unparsed entity has an associated `notation`, identified by name. Beyond a requirement that an XML processor make the identifiers for the entity and notation available to the application, XML places no constraints on the contents of unparsed entities.]

If the `NDataDecl` is present, this is a general `unparsed entity`; otherwise it is a `parsed entity`.

`External parsed entities` should each begin with a `text declaration`(就是`<?xml ?>`的部分).

The `text declaration` must be provided literally, not by reference to a parsed entity. The `text declaration` must not appear at any position other than the beginning of an `external parsed entity`. The `text declaration` in an `external parsed entity` is not considered part of its `replacement text`.

[Definition: `Notations` identify by name the format of `unparsed entities`, the format of elements which bear a notation attribute, or the application to which a `processing instruction` is addressed.]

[Definition: `Notation declarations` provide a name for the notation, for use in entity and attribute-list declarations and in attribute specifications, and an external identifier for the notation which may allow an XML processor or its client application to locate a helper application capable of processing data in the given notation.]

[Definition: For an internal entity, the `replacement text` is the content of the entity, after replacement of character references and parameter-entity references.]

[Definition: For an external entity, the `replacement text` is the content of the entity, after stripping the text declaration (leaving any surrounding whitespace) if there is one but without any replacement of character references or parameter-entity references.]

### XML Schema
`XML Schemas` express shared vocabularies and allow machines to carry out rules made by people. They provide a means for defining the structure, content and semantics of XML documents. in more detail.

The `xsi:schemaLocation` and `xsi:noNamespaceSchemaLocation` attributes can be used in a document to provide hints as to the physical location of schema documents which may be used for ·assessment·. 后者用来指定无namespace的element的schema

`xmlns:xsi`声明要使用`xsi namespace`

参考https://www.w3.org/TR/REC-xml-names

### Simple API for XML (SAX)
`EntityResolver`: If a SAX application needs to implement customized handling for `external entities`, it must implement this interface and register an instance with the SAX driver using the `setEntityResolver` method. 默认行为是the system ID will be dereferenced as a URL，根据URL获取对应资源（可能需要访问网络）

The Java XML parser that spring uses will read the `schemaLocation` values and try to load them from the internet, in order to validate the XML file.

SAX 相比DOM类方法内存占用少，速度更快。使用visitor模式
