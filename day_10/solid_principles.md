# SOLID Principles

## [S]ingle Responsibility Principle

- A class should have one and only one reason to change.
- A class should have only one job.

## [O]pen/Closed Principle

- Objects or entities should be open for extension but closed for modification.

## [L]iskov Substitution Principle

- Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable of objects of y of type S where S is a subtype of T.
- When extending a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the client code.

## [I]nterface Segregation Principle

- A client should never be forced to implement an interface that it doesn't use, or clients shouldn't be forced to depend on methods they don't use.

## [D]ependency Inversion Principle

- Entities must depend on abstraction, not on concretions.
- It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.
