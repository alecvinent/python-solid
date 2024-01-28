from https://realpython.com/solid-principles-python/

- Single-responsibility principle (SRP)
- Open–closed principle (OCP)
- Liskov substitution principle (LSP)
- Interface segregation principle (ISP)
- Dependency inversion principle (DIP)


**1 The single-responsibility principle (SRP)**

The single-responsibility principle (SRP) comes from Robert C. Martin, more commonly known by his nickname Uncle Bob, who’s a well-respected figure in the software engineering world and one of the original signatories of the Agile Manifesto. In fact, he coined the term SOLID.

A class should have only one reason to change.

`This means that a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes.`


**2 Open-Closed Principle (OCP)**

The open-closed principle (OCP) for object-oriented design was originally introduced by Bertrand Meyer in 1988 and means that:

`Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.`


**3 Liskov Substitution Principle (LSP)**

The Liskov substitution principle (LSP) was introduced by Barbara Liskov at an OOPSLA conference in 1987. Since then, this principle has been a fundamental part of object-oriented programming. The principle states that:

`Subtypes must be substitutable for their base types.`

**4 Interface Segregation Principle (ISP)**

The interface segregation principle (ISP) comes from the same mind as the single-responsibility principle. Yes, it’s another feather in Uncle Bob’s cap. The principle’s main idea is that:

`Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.`

In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes should be segregated into more specific classes.

**5 Dependency Inversion Principle (DIP)**

The dependency inversion principle (DIP) is the last principle in the SOLID set. This principle states that:

`Abstractions should not depend upon details. Details should depend upon abstractions.`

