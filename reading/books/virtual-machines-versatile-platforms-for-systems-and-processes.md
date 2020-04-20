### Virtual Machines - Versatile Platforms for Systems and Processes
Virtualization diffs from abstraction in that virtualization does not necessarily hide details; the level of detail in a virtual system is often the same as that in the underlying real system.

- Process Virtual machines
- System virtual machines

Process-level virtual machines provide user applications with a virtual ABI environment. In their various implementations, process VMs can provide replication, emulation and optimization.

Instruction set emulation is a key aspect of many virtual machine implementations. Instruction set emulation can be carried out using:
- interpretation
    - decode and dispatch interpreter
    - indirect threaded interpreter
    - predecoding and directed threaded interpreter
- binary translation

Static predecoding or translation is impossible sometimes, such as a branch instruction dependent on the contant of a register, or variable-length instructions. It's called `code discovery problem`. Another problem is `code location problem`.

A more efficient interpreter can be built around the principle: "make the common case faster".

The important, useful aspect of same-ISA emulation is that the emulation-manager is always in control of the software being emulated.

### Process Virtual Machine
components of process virtual machine
- loader
- initialization block
- emulation engine
- code cache manager
- profile database
- os call emulator
- exception emulator
- side tables(auxiliary data structures)

process VM compatibility

levels of compatibility
- intrinsic compatibility(complete compatibility)
- extrinsic compatibility
    - stating the external properties that must hold in order for compatibility to be achieved.

start-up performance and stead-state performance.

Based on the performance tradeoff just described, a typical high performance emulation framework implements multiple emulation methods and applies them in stages.(JVM的默认做法)

The three levels of emulation---interpretion, binary translation of bisic blocks and binary translation with optimization(on superblocks)---allow a number of staged interpretion strategies.

Instruction sets are `logically complete`, in the sense that any function can be performed on input operands to produce a result, given enough time...Hence, with ISA emulation it's not a matter of `whether` emulation can be done, just how `efficiently` it can be done and how it'll be....It's difficult to come up with a set of overall rules or strategies for different-OS emulation because of the wide variety of cases that must be handled. Consequently, OS emulation is very much an `ad hoc` process that must be implemented on a case-by-case basic and that requires considerable knowledge of both the guest and host OSs.

#### purpose of process VMs
- (dynamic) binary translation (`dynamic binary translation` is also called `dynamic recompilation`)
- dynamic binary optimization
- dynamic binary instrumentation/analysis
- emulator

#### examples of process VMs
- valgrind
- DynamoRIO
- BOLT(of facebook)
- JVM/CLR
- Wine
- Wabi(of Sun)
- Dolphin
- IA-32 Execution Layer(of Intel)
- FX!32(of DEC)

### dynamic binary optimization
#### dynamic program behavior
One important property of programs is that dynamic control flow is highly predictable
- any given conditional branch instruction is very often decided the same way(taken or not taken) a large fraction of the time.
- a high percentage of branches are decided the same way as on their recent previous execution.
- Another important property of conditional branch instructions is that backward branches, i.e., branches to lower-address, are typically taken, because they're often a part of a loop
- With indirect jumps, the issue is determining the destination address of the jump. Some jump destination address seldom changes and are highly predictable, while others change often and are very difficult to predict

data value predictibility
- The data values used by a program are often predictable, and in many cases they change relatively little over the course of a program’s execution.

#### profiling
1. Traditional profiling applied across multiple program runs
2. on the-fly profiling in a dynamic optimizing VM

When dynamic optimization is being used, there are overhead costs every time a guest program is run...in a dynamic optimization environment, the overhead of optimization must be outweighed by the benefits of executing the optimized code.

types of profiles
- how frequently different code regions are being executed.
- control flow (branch and jump) predictability
- data or address values
- Another type of profile based on control flow is the `path profile`

In general, there are more edges(branches) than nodes(basic blocks), so it may appear slightly more expensive to profile all the edges.

Furthermore, the edge profile data provides a more precise view of program execution than the basic block profile; i.e., the basic block profile can be derived from the edge profile by summing the number of incoming edges to each block (or by summing outgoing edge counts).

There are two ways of collecting a profile: `with instrumentation` and `with sampling`.
- `Instrumentation-based profiling` typically targets specific program-related events and counts all instances of the events being profiled.
- With `sampling-based profiling`, the program runs in its unmodified form, and, at either fixed or random intervals, the program is interrupted and an instance of a program-related event is captured

Counter overflow can be solved using:
- counter saturating: i.e., when a counter reaches its maximum value, it stays there
- counter decaying(such as divide the counter by 2 periodically)

`compensation code`: to `compensate for any effects that out of order execution may have had`.

#### optimizing translation blocks
- improve locality
    - spatial locality
        - rearrange memory layout
        - procedure inlining
            - full inlining
            - dynamic or partial procedure inlining
    - temporal locality
- optimize superblocks

three ways of rearranging basic blocks according to control flow.
- trace formation
    - trace: a contiguous sequence of basic blocks
- superblock formation
    - superblocks have only one entrance at the top and no side entrances.
- tree groups, a generalization of superblocks, which are useful when control flow is difficult to predict, and provides a wider scope for optimization.

implementing a code-scheduling algorithm
- translate to single-assignment form
- form register map(RMAP)
- reorder code
- determine checkpoints(the backup points if it traps)
- assign registers
- add compensation code

superblocks versus traces
- instruction cache and branch prediction performance
- issues that come into play when dynamic superblock/trace formation and optimization are implemented.
    - superblocks require compensation code only at exit points, which is relatively straightforward.

### HLL Virtual machine implementation

optimizations
- code relayout
- method inlining
- optimize virtual method calls
- multiversoning and specialization
- on-stack replacement
- optimization of heap-allocated objects
    - scalar replacement(requires reference escape analysis)
    - ordering object fields according to usage patterns to improve data cache performance
- lower level optimizations
    - eliminate null/range checking
    - loop peeling
- optimizing garbage collection

### Codesigned virtual machines
Virtual machine technologies can turn processor development into a codesign effort, where the host architecture (the target ISA in particular) is designed concurrently with the VM software that runs on it. ...Taken together, however, the codesigned hardware and software support a conventional source ISA (and all the software developed for it).

These `codesigned virtual machines` open new avenues for architectural innovation. Because software becomes part of the “hardware” platform, the interface between hardware and conventional software is shifted upward, and there are new opportunities for dividing the implementation between hardware and software in an optimal way.

### System Virtual Machine
some of the applications of system vm:
- implementing multiprogramming
- multiple single-application VMs
- multiple secure environments
- managed application environments
- mixed-os environments
- legacy applications
- multiple platform application development
- new system transition
- system software development
- operating system training
- help desk support
- operating system instrumentation
- event monitoring
- system encapsulation

key concepts
- outward apperaence
- state mangement
- resource control
- native and hosted VMs

#### resource virtualization -- processors
- emulation
    - interpretation
    - binary translation
- direct native execution
    - possible only when wht ISA of the host is identical to the ISA of the target.

The assumptions made in the analysis(by Popek and Goldberg) are as follows:
- The hardware consists of a processor and a uniformly addressable memory
- the processor can operate in one of two modes, thes ystem mode or the user mode
- some subset of the instructionset is available only in the system mode
- memory addressing is done relative to the contents of a relocation register

instruction catatories:
- `Control-sensitive` instructions: are those that attempt to change the configuration of resources in the system, for example, the physical memory assigned to a program or the mode of the system.
    - The `Load PSW` and `Set CPU Timer` instructions are examples of controlsensitive instructions.
- `Behavior-sensitive` instructions: are those whose behavior or results produced depend on the configuration of resources — in the model, this includes the value in the relocation bounds register or on the mode of operation.
    - such as `Load Real Address` and `Pop Stack into Flags Register` instrucions
- innocuous: If an instruction is neither control sensitive nor behavior sensitive, it is termed innocuous

The functions of the VMM can be divided into three parts:
- dispatcher
- allocator
- interpreter

According to Popek and Goldberg, a potential virtual machine monitor must satisfy three properties before qualifying as a true virtual machine monitor: `efficiency`, `resource control`, and `equivalence`.

recusive virtualization

We refer to a virtual machine system in which some of the nonprivileged instructions must be emulated as a `hybrid virtual machine system`.

#### resource virtualization -- memory
On contemporary platforms, `page translation` is supported by a combination of a `page table` and a `translation lookaside buffer` (TLB). Depending on the ISA, either the page table or the TLB is architected.

#### resource virtualization -- I/O
- Virtualizing at the I/O Operation Level
- Virtualizing at the Device Driver Level
- Virtualizing at the System Call Level

a dual-mode hosted virtual machine system must have three components for its VMM:
- the VMM-n, which is the component working in a privileged native mode
- the VMM-u, the component that runs as an application on the host operating system
- the VMM-d, the component that enables communication between the VMM-n and VMM-u

#### performance enchancement of system virtual machines
reasons for performance degradation
- setup
- emulation
- interrupt handling
- state saving
- bookkeeping
- time elongation

hardware techniques that help improve the performance of VMs:
- Instruction Emulation Assists
- Virtual Machine Monitor Assists
- Improving Performance of the Guest System
    - it is possible to get an improvement in performance if a guest OS knows whether it is currently executing natively or in a virtual machine environment
    - The notion that the performance of a virtual machine system can be improved by making modifications to the guest operating system has received renewed interest through what is being called `paravirtualization`.
- Specialized Systems
- Generalized Support for Virtual Machines
    - interpretive execution facility (IEF)

### Multiprocessor Virtualization
As described earlier, the spectrum of possible implementations for a large multiprocessing system with n processors has two extreme points.
- At one end is a simple cluster of n nodes, each consisting of a single processor.
- At the other extreme is an n-way shared-memory system with n processors, all sharing the same main memory.

physical partitioning and logical partitioning

key advantages of physical partitioning over other forms of partitioning.
- Failure isolation
- Better security isolation
- Better ability to meet system-level objectives

While physical partitioning has a number of attractive features, it is probably not the ideal solution if system utilization is to be optimized.

Logical partitioning has been introduced on several systems that do not have microcoded processor implementations. .... If the mode is not exposed in the ISA, then the software that runs in this mode can be viewed essentially as an extension of the hardware itself, very much like the VMM software in a codesigned virtual machine. The common name given to this piece of software is the `hypervisor`.

Comparison with System Virtual Machines
- Hypervisors and conventional system VMMs are similar, in that both run in the highest-privilege mode.
- hypervisors need hardware support and work in a special mode, while system virtual machines may be implemented on standard unmodified hardware.
- The guest operating system in a logically partitioned system works in the `privileged mode`, just as it would on native hardware, whereas in a conventional system VM, the guest operating system works in `user mode`.

Hypervisor Services Interface
- the performance can be made even better if a guest operating system is made aware of the fact that it is operating in a hypervisor environment.

#### Virtualization with Different Host and Guest ISAs
- The instructions of the target ISA must be dynamically emulated by the host system.
- The memory model of the target system, particularly the coherence and memory ordering rules, must be observed on the virtual system.

Memory Model Emulation...two main aspects of the memory model, the `memory coherence` and the `memory consistency models`.

Recall that `memory coherence` is said to be implemented on a multiprocessor system if the order of writes to a given location by one processor is maintained when observed by any other processor in the system. `memory coherence`是`memory consistency`的一个子集

`Memory consistency` deals with the order in which accesses by one processor to different locations in memory are observed by another processor. Memory consistency deals not only with different locations but with all accesses, whether reads or writes. four hazards have to be considered in a consistency model:
- the read-read (RR) hazard
- the read-write (RW) hazard,
- the write-read (WR) hazard
- the write-write (WW) hazard.

When emulating a consistency model of a guest using a different consistency model for the host, we can divide the space of possibilities into the following three categories.
1. The memory consistency model of the guest is the same as that of the host or weaker than that of the host:
2. The memory consistency model of the guest is stronger than (more restrictive than) the memory consistency model of the host
3. The memory consistency model of the guest is stronger in some respects and weaker in other respects

### Emerging Applications
three examples of emerging virtual machine applications
- computer security
- the migration of complete computing environments
- grid computing paradigm

#### Security
A common way of providing security protection for current systems is through the use of an intrusion-detection system (IDS)....`network-based intrusion-detection system`, or `NIDS` for short....host-based intrusion-detection system, or `HIDS`.

- Virtual Machine as a Sandbox
- Virtual Machine for Monitoring Low-Level Activity
- Secure and Complete Logging Using Virtual Machines

Role of Dynamic Binary Rewriting Technology in Security
- Restricting Control Transfers
- Restricting Code Execution
- Protecting the Runtime Monitor

#### Migration of Computing Environments
- Virtual Computers
    - The entire state of a computer (which could include tens of gigabytes or more of disk space) can be so large that the time taken to migrate the state may be prohibitive.
    - Having decided what portion of the machine state needs to be migrated, there is still the problem of packaging and securely transmitting the information.
    - When the hardware on the two machines is identical and when the virtual machine monitors running on them are identical, the process of transmitting the environment from one machine to another should be seamless.
    - Finally, the ISA of the user’s virtual machine and the ISA of each of the host computers determine the extent to which the performance of the system appears identical on the different sites.
- Using a Distributed File System: The Internet Suspend/Resume Scheme
- State Encapsulation in the Stanford Collective
- Migration of Virtual Machines in VMotion

#### Grids: Virtual Organizations
- Yet the nature of tasks that most users perform on their computers is such that only a tiny fraction of the available compute power is actually used
- Ironically, there are occasions when users would like even more computation power than what they have available on their own systems.

### Real Machine
#### The User ISA: Computation
Register Architecture
- Register Architecture
- Typed Registers
- Special-Purpose Registers

Memory Architecture
- In some ISAs, main memory appears as a single linear address space.
- In other ISAs, main memory appears as a set of segments pointed to by typed segment registers containing their base addresses.

User Instructions
- Memory Instructions
- Integer Instructions
- Floating-Point Instructions
- Branch Instructions

#### The System ISA: Resource Management
These registers are sometimes given only secondary importance because they are not exposed to the application and because the compiler usually does not use them. However, they are **very important in system-level virtual machine implementations**, because they often are the source of some of the thorniest problems that arise in the implementation of such VMs.
##### Privilege Levels
- system mode
    - sometimes referred to as supervisor mode, kernel mode, or privileged mode.
- user mode

Many operating systems (including UNIX and its derivatives) rely on only two privilege levels. On the other hand, the Intel IA-32 ISA supports up to four levels

##### System Register Architecture
- System Clock Register
- Trap and interrupt register
- Trap and interrupt mask register
- Translation table pointers

#### Memory Consistency Models
The sequential consistency model, described first by Leslie Lamport (1979), is an elegant and natural model. A multiprocessor system maintains sequential consistency if the set of observable memory access orderings made by a multithreaded program is a subset of the observable orderings when the program is run on a multiprogrammed uniprocessor system.

We will simply state here, without proof, that a `sufficient condition for sequential consistency in a multiprocessor system` is the following: For every pair of accesses to memory by any one processor, the first access in program order is observed by all other processors before the second access is observed. Any implementation that satisfies this condition guarantees sequential consistency in the system.

