## Principles of Software Construction - Final Review Part I

Lectures from begin of semester to midterm 1, in chronological order.

### Introduction to Java

- "Hello World" program
  - You must use a class
  - `main` must be public and static
  - `main` must return `void`
  - `main` must declare command-line arguments
  - Standard I/O uses `System`
  - Compile to `.class`
  - `JVM` executes `main` method
  - Some verbosity is not bad: reduce errors, increase readability
  - Managed runtime: safe, flexible, enables gabage collection
  - Good language for large-scale programming
- Primitive types
  - `int long byte short char float double boolean`
  - No identity, only value
  - Immutable
  - On stack, exist only when use
  - `byte short`: use `int` instead
  - `float`: use `double` instead
- Object reference types
  - class, interface, array, enum, annotation
  - Have identity distinct from value
  - On heap, gabage collected
  - Unity of expression with generics
  - More costly
- The class hierarchy
  - Root is `Object`
  - All class except `Object` has one parent class
  - Overriding method must obey contracts of superclass
  - Liskov Substitution Principle
  - Interface defines type without implementation
- Collections
  - `Set HashSet`
  - `List ArrayList`
  - `Queue ArrayDeque`
  - `Deque ArrayDeque`
  - `[stack] ArrayDeque`
  - `Map HashMap`
  - Prefer collections to arrays
  - Common methods to all objects
    - `equals`: must implement equivalence relation
    - `hashCode`: `int` value, must equal for equal objects, likely differ for unequal objects
    - `toString`

### Object-Oriented Programming in Java

- An object is a bundle of state and behavior
- Methods and fields are collectively members
- Class defines both type and implementation
- The methods of a class are its API
- Interface specifies expectations
- Class delivers on expectations
- Use interface instead of class for declarations: support change of implementation, prevent dependence on implementation details
- Well-designed code hides all implementation details
- Known as information hiding or encapsulation
- Provide only functionality required by the client
- Exceptions
  - Unchecked: programming error, or unrecoverable failures
  - Checked: every caller should be aware of and handle
  - Do not use return codes
  - Do not return `null` to indicate zero-length result
  - Avoid unnecessary checked exceptions
  - Favor standard exceptions
    - `IllegalArgumentException`: invalid parameter value
    - `IllegalStateException`: invalid object state
    - `NullPointerException`: `null` parameter where prohibited
    - `IndexOutOfBoundsException`: invalid index parameter
  - Don't ignore exceptions
  - Try with resources

### Testing and Object Methods in Java

### Behavioral subtyping, Design for reuse

- Design goals: functional correctness, robustness, flexibility, reusability, efficiency, scalability, security
- Delegation: an object relies on another object for some subset of its functionality
- Usually favor delegation/composition over inheritance

### Introduction to Design Patterns

- `final`
  - Final field prevents reassignment to the field
  - Final method prevents overriding the method
  - Final class prevents extending the class

### Design Patterns for Reuse

- UML you should know
  - Interface vs classs
  - Fields vs methods
  - Relationships
    - "extend" (inheritance)
    - "implements" (realization)
    - "has a" (aggregation)
    - non-specific association
  - Visibility: `(+)public (-)private (#)protected`
