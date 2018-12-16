## Principles of Software Construction - Final Review Part I

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
