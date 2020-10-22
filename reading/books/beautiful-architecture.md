## beautiful architecture
Yet beautiful architectures exhibit a few universal principles, some of which I outline here:
- One fact in one place
    - normalization
    - factoring
    - layering
- Automatic propagation
- Architecture includes construction
- Minimize mechanisms
- Construct engines
- O(G), the order of growth
- Resist entropy

### Chapter 1 What is Architecture
Central to beauty is `conceptual integrity` — that is, a set of abstractions and the rules for using them throughout the system as simply as possible.

In our discussion we will use “architecture” as a noun to denote a set of artifacts, including documentation such as blueprints and building specifications that describe the object to be built, wherein the object is viewed as a set of structures.

Architecture is a game of trade-offs — a decision that improves one of these characteristics often diminishes another.

The first concern of a software architect is not the functionality of the system.
You did this by focusing on `quality concerns` that needed to be satisfied.

It is this `conceptual integrity` that allows a developer who already knows about one part of a system to quickly understand another part.

The challenge for an architecture team is to maintain a `single-mindedness` and a `single philosophy` as they go about creating the architecture. Keep the team as small as possible, work in a highly collaborative environment with frequent communication, and have one or two “chiefs” act as benevolent dictators with the final say on all decisions. This organizational pattern is commonly seen in successful systems, whether corporate or open source, and results in the conceptual integrity that is one of the attributes of a beautiful architecture.

Conway noted that the structure of a system reflects the structure of the organization that built it (1968).

We know from experience that we should evaluate an architecture to determine whether it will meet its requirements before spending money to build, test, and deploy the system.
- The first class of evaluation methods determines properties of the architecture, often by modeling or simulation of one or more aspects of the system.
- The second, and broadest, class of evaluation methods is based on questioning the architects to assess the architecture. There are many structured questioning methods.
    - Software Architecture Review Board (SARB)
    - Architecture Trade-off Analysis Method (ATAM)
    - Active reviews are another type of questioning approach that turns the process on its head, requiring the architects to provide the reviewers with the questions that the architects think are important to answer
    - software architecture review checklist

What criteria would we add to these for nominees for a more general “Architecture Hall of Fame,” or perhaps a “Gallery of Beautiful Architectures”?
- First, ... our systems are built to be used. ... begin by looking at the `Utility of the architecture` ... But before an architecture can be used, it must be built, and so we should look at the `Buildability of the architecture`.
- Next, we want architectures that demonstrate Persistence—that is, architectures that have stood the test of time...We want to find architectures that have avoided the “aging horizon” (Klein 2005) beyond which maintenance becomes prohibitively expensive.
- Finally, we would want to include architectures that have features that delight the developers and testers who use the architecture and build it and maintain it, as well as the users of the system(s) built from it.

### Chapter 2
Poor company structure and unhealthy development processes will be reflected in a poor software architecture.

- Incomprehensibility(Difficult or impossible to understand or comprehend)
- Lack of cohesion

- It’s important to maintain the quality of a software design. Bad architectural design leads to further bad architectural design.
- The consequence of a bad architecture is not constrained within the code. It spills outside to affect people, teams, processes, and timescales.

Key qualities of software design are cohesion and coupling.
- Strong cohesion
    - Cohesion is a measure of how related functionality is gathered together and how well the parts inside a module work as a whole.
- Low coupling
    - Coupling is a measure of the interdependency between modules—the amount of wiring to and from them.
    - Tight coupling leads to untestable code.

It’s important to know what you’re designing before you start designing it. If you don’t know what it is and what it’s supposed to do, don’t design it yet. Only design what you know you need.

The lack of foresight and architectural design in the led to:
- A low-quality product with infrequent releases
- An inflexible system that couldn’t accommodate change or the addition of new functionality
- Pervasive code problems
- Staffing problems (stress, low morale, turnover, etc.)
- A lot of messy internal company politics
- Lack of success for the company
- Many painful headaches and late nights working on the code

Decisions about some of the basic concerns were made at this point to ensure that the code would grow easily and cohesively, including:
- choice of supporting libraries the project would employ
- The top-level file structure
- How we would name things
- A “house” presentation style
- Common coding idioms
- The choice of unit test framework
- The supporting infrastructure (e.g., source control, a suitable build system, and continuous integration)

The Story Unfolds
- Locating functionality
    - An architecture helps you to locate functionality: to add it, to modify it, or to fix it. It provides a template for you to slot work into and a map to navigate the system.
- Consistency
    - A clear architectural design leads to a consistent system. All decisions should be made in the context of the architectural design.
    - Clear architecture helps reduce duplication of functionality.
- Growing the architecture
    - Software architecture is not set in stone. Change it if you need to. To be changeable, the architecture must remain simple. Resist changes that compromise simplicity.
- Deferring design decisions
    - YAGNI (don’t do anything if you aren’t going to need it.)
    - Defer design decisions until you have to make them. Don’t make architectural decisions when you don’t know the requirements yet. Don’t guess.
- Maintaining quality
    - Pair programming
    - Code/design reviews for anything not pair-programmed
    - Unit tests for every piece of code
    - Architectural quality must be maintained. This can happen only when the developers are given and take responsibility for it.
- Managing technical debt
- Unit tests shape design
    - Having a good set of automated tests for your system allows you to make fundamental architectural changes with minimal risk. It gives you space in which to work.
    - Unit testing your code leads to better software designs, so design for testability.
- Time for design
    = Good project planning leads to superior designs. Allot sufficient time to create an architectural masterpiece—they don’t appear instantly.
- Working with the design
    - A team’s organization has an inevitable affect on the code it produces. Over time, the architecture also affects how well the team works together. When teams separate, the code interacts clumsily. When they work together, the architecture integrates well.
    - `Conway’s Law` states that code structure follows team structure. Simply stated, it says, “If you have four groups working on a compiler, you’ll get a four-pass compiler.”


### Chapter 3 - Architecting for Scale （MMO or virtual worlds)
ONE OF THE MORE INTERESTING PROBLEMS IN DESIGNING AN ARCHITECTURE for a system is ensuring flexibility in the scale of that system. Scaling is becoming increasingly important, as more of our systems are run on networks or are available on the Web. For such systems, `the idea of capacity planning is absurd` if you want a margin of error that is under a couple of orders of magnitude. **If you put up a site and it becomes popular, you might suddenly find that there are millions of users accessing your site**. Just as easily (and just as much of a disaster), you can put up a site and find that no one is particularly interested, and all of the equipment in which you invested now lies idle, soaking up money in energy costs and administrative effort. In the networked world, a site can transition from one of these states to the other in a matter of minutes.

#### Context
Thus we knew at the beginning that the overall architecture would need to be a distributed system.

The classic enterprise environment is envisioned as `a thin client connected to a thick server` (which is itself often connected to an even thicker database server). The server will hold most of the information needed by the clients, and will act as a filter to the backend database. Very little state is held at the client...This environment in which MMOs and virtual worlds exist is nearly a mirror image of the classic enterprise environments

Most of the computation goes on at the client. The real job of the server is to hold `the shared truth of the state of the world`, ensuring that any variation in the view of the world held at the various clients can be corrected as needed.

The `data access patterns` of MMOs and virtual worlds are also quite different from those that are seen in enterprise situations. The usual rule of thumb within the enterprise is that 90% of data accesses will be read-only, and most tasks read a large amount of data before altering a small amount. In the MMO and virtual world environment, most tasks access only a very small amount of the state on the server, but of the data that they access, about half of it will be altered.

In an enterprise environment, the goal is to conduct business, and some lags in processing are acceptable if the overall throughput is improved. In the MMO and virtual world environment, the goal is to have fun, and `latency is the enemy of fun`.

Online games and virtual worlds have clearly found ways to scale to large numbers of users. The current mechanisms fall into two groups.
- The first of these is geographic in nature.
- A second way of dealing with areas that are overcrowded in a game or world is known as `sharding`.

### Chapter 5 - Resources oriented architectures.
The take-home message is that not all problems are technical.

The Web’s success is largely due to the fact that it has raised the possibilities for information sharing while also lowering the bar.

The real magic, however, is the explicit linkage between publicly available information, what that linkage represents, and the ease with which we can create windows into this underlying content.

We like giving names to things because we are fundamentally name-oriented beings; we use names to disambiguate “that thing” from “that other thing.”

`The separation of concerns` here is among the key abstractions of the interaction style. We isolate
- the things we are interested in discussing
- the actions by which we manipulate those things
- the forms we choose to send and receive them in.

The `resource-oriented style` is marked by a process of issuing `logical requests` for named resources. These requests are interpreted by some kind of engine and turned into a `physical representation` of the resource.

SOAP is a fine technology for invoking behavior, but it falls down as a means of managing information. REST is about managing information, not necessarily invoking arbitrary behavior through URLs. When people start scratching their heads and wondering if four verbs are enough to do what they want to do, they are probably not thinking about information; they are thinking about invoking behavior.

Software developers do not usually care about `data`; they care about algorithms, objects, services, and other constructs such as this....Unfortunately, most of these blueprints ignore `information` as a first-class citizen. They tie us into specific bindings that make it hard to make changes without breaking existing clients.

It is time to take a step away from software-centric architectures and start to focus on `information` and how it flows.

### Chapter 6 - Data grows up: The architecture of the facebook platform
Information architects have a solid understanding that `data` rather than `algorithms` sit at the center of most systems.

Most of the architectural decisions made to create universally available social context are shaped by this yin and yang: `data availability` and `user privacy`.

- Creating a social web service
    - PRODUCT PROBLEM: Applications could make use of a user’s social data on Facebook, but this data is inaccessible.
    - DATA SOLUTION: Make Facebook data available through an externally accessible web service
- Creating a social data query service
    - PRODUCT PROBLEM: Obtaining data from the Facebook Platform APIs incurs much more cost than obtaining internal data.
    - DATA SOLUTION: Implement external data access patterns using the same one employed for internal data: a query service.

应用在FB页面中展示并能够利用更多FB内部数据（不能通过API service分享的数据）：Developers create application content for execution and display on the social site itself through a data-driven markup language, interpreted by Facebook.

some incorrect ways to attempt this:
- Applications on Facebook: Directly Rendering HTML, CSS, and JS
    - This changes the n-tier model of an application significantly.
    - this allows the application to completely violate the user’s expectation of the more controlled experience on FB, and opens the site and its users up to all kinds of nasty security attacks.
    - solves neither of our product problems fully
- Applications on Facebook: iframes
    - This essentially results in the browser becoming the request broker rather than FB.
    - a separable (and safe) execution sandbox
    - no new data beyond that exposed by the API service.

Applications on Facebook: FBML As Data-Driven Execution Markup
- retain the application-as-service model and the safety and trust of the iframe, while enabling developers to use more social data.
- Send back not HTML but specific markup that defines sufficient amounts of the application’s logic and display, plus requests for protected data, and let FB render it entirely in its trusted server environment!
- a example of data at the center of execution. FBML is simply declarative execution rather than imperative flow

`FBML` augments browser parse technology with callbacks wrapping the data, execution, and display macros created and managed by Facebook. This simple idea allows full integration of applications, enabling use of data intentionally exposed through the API while maintaining the safety of the user experience. Almost a programming language in itself, FBML is data fully grown up: externally provided declarative execution safely controlling data, execution, and display on Facebook.

Supporting Functionality for the System
- Platform Cookies：FB端cookie
- FBJS 避免application script获取用户信息，处理所有的application script，所有代码一律加prefix，避免调用browser代码，实际调用FBJS

### Chapter 7 - Xen and the Beauty of Virtualization
When Xen was first released, it employed `paravirtualization` to run commodity operating systems such as Linux.

`Paravirtualization (PV)` is an enhancement of virtualization technology in which a guest operating system (guest OS) is modified prior to installation inside a virtual machine (VM) in order to allow all guest OS within the system to share resources and successfully collaborate, rather than attempt to emulate an entire hardware environment. 超虚拟化或类虚拟化（一些文章翻译为半虚拟化或部分虚拟化，含义很奇怪），感觉para应该是alongside of，因此翻译为操作系统辅助虚拟化更合适

A `trusted system`, then, is one that is allowed access to your data. When `distrust` is built into the architecture, the number of trusted components is minimized, and this therefore provides security by default.

`give each user an account` compared to virtualization has much less flexibility(其他系统上运行的软件、依赖超级用户才能安装的软件) and performance isolation。

Xen is an example of `native virtualization` (also known as `Type 1 virtualization`). The alternative approach is to run a hypervisor on top of a host operating system. In this case, each virtual machine effectively becomes a process in the host operating system.

The `separation of mechanism and policy` is a design principle in computer science. It states that mechanisms (those parts of a system implementation that control the authorization of operations and the allocation of resources) should not dictate (or overly restrict) the policies according to which decisions are made about which operations to authorize, and which resources to allocate.

Virtualization is simply a form of indirection, and even though modern computers have hardware support for virtualization, naive reliance on this support leads to poor performance. The same problems arise when you make naive use of any type of virtualization.

`Live migration`, which enables a virtual machine to be moved between physical computers with only a negligible period of downtime.

### Chapter 8 - Guardian: A Fault-Tolerant Operating System Environment
### Chapter 9 - JPC: An x86 PC Emulator in Pure Java
However, `pure virtualization` has its problems, as it relies on some degree of hardware support to function and is therefore exposed to instabilities caused by such close links to the physical machine. `Emulators`, by contrast, are virtual computers built entirely in software, and therefore have no specific requirements on the underlying hardware.

Java Performance Tips: Invoke theseguidelines only when either a positive effect will be seen on the design or that last drop of performance is really necessary.
- Tip #1: Object creation is bad
- Tip #2: Static is good
- Tip #3: Table switch good, lookup switch bad
- Tip #4: Small methods are good methods
- Tip #5: Exceptions are exceptional
- Tip #6: Use decorator patterns with care
- Tip #7: instanceof is faster on classes
- Tip #8: Use synchronized minimally
- Tip #9: Beware external libraries

### Chapter 10 - The Strength of Metacircular Virtual Machines: Jikes RVM
a self-hosting runtime

Self-hosting runtime environments are known as `metacircular`.

A meta-circular evaluator (MCE) or meta-circular interpreter (MCI) is an interpreter which defines each feature of the interpreted language using a similar facility of the interpreter's host language.

Jikes RVM does not include an interpreter; all bytecodes must first be translated by one of Jikes RVM’s compilers into native machine code.

### Chapter 11 - GNU Emacs: Creeping Featurism Is a Strength
`Featuritis` or `creeping featurism` is the tendency for the number of features in a product (usually software product) to rise with each release of the product.

Looking under the hood, the story gets stranger. Emacs Lisp has no object system, its module system is just a naming convention, all the fundamental text editing operations use implicit global arguments, and even local variables aren’t quite local. `Almost every software engineering principle that has become generally accepted as useful and valuable, Emacs flouts. But it works—and works rather well.`

one we can ask of any extension language we encounter
- how easy is it to use the results of one command as input to another?
- what sort of interfaces are available for plug-ins to use?
- is the extension language the preferred way to implement most new features for the application?

The key to this solution is that Emacs is a collection of packages, not a unified whole.

Although a web browser is not a text editor, there are some striking resemblances between Emacs’s architecture and that of a browser:
- their semantics have many essential traits in common: like Emacs Lisp, JavaScript is interpreted, highly dynamic, and safe. Both are garbage-collected languages.
- As with Emacs Lisp, it’s very practical to begin with a small fragment of JavaScript on a page to improve some minor aspect of its behavior, and then grow that incrementally into something more sophisticated. The barrier to entry is low, but the language scales up to larger problems.
- As in Emacs, display management is automatic. JavaScript code simply edits the tree of nodes representing the web page, and the browser takes care of bringing the display up to date as needed.
- As in Emacs, the process of dispatching input events to JavaScript code is managed by the browser. Firefox takes care of deciding which element of the web page an event was directed at, finds an appropriate handler, and invokes it.

Firefox developers to migrate more and more of the browser itself from `C++` to `JavaScript`, a much more comfortable and flexible language for the problem. In this sense, Firefox’s architecture is evolving to look more like that of Emacs, with its `all-Lisp Controller`.

Like Emacs, Firefox places its extension language at the heart of its architecture, a strong argument that the language’s relationship with the application has been designed properly.

### Chapter 12 - When the Bazaar Sets Out to Build Cathedrals (How ThreadWeaver and Akonadi were shaped by the KDE community and how they shape it in turn)

### Chapter 13 - Software Architecture: Object-Oriented Versus Functional
“Beauty,” as a slogan for a software architecture, is not strictly for the beholder to judge. Clear objective criteria exist:
- Reliability
    - Does the architecture help establish the correctness and robustness of the software?
- Extendibility
    - How easy is it to accommodate changes?
- Reusability
    - Is the solution general, or better yet, can we turn it into a component to be plugged in directly, off-the-shelf, into a new application?

It finds that the relationship is the other way around: `object-oriented architecture, retaining its architectural advantages while correcting its limitations`, if enriched with recent developments such as agents in Eiffel terminology (“closures” or “delegates” in other languages), subsumes functional programming

### Chapter 14 - Rereading the Classics
Programming, like architecture, is a story of practice. We had better avoid being dogmatic, and instead focus on what works.

Architecture is a chaotic adventure because beautiful architecture alone is not enough; not only beauty, but also usefulness, is the law for architecture and programming alike.

