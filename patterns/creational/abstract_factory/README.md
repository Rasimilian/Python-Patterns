### Abstract factory pattern
Provides an interface for creating related/dependent objects without specifying 
their concrete classes. The client code calls the creation methods of a factory 
object instead of creating products directly with a constructor call.

### Notes:
* In Python, the interface can be simply a callable, which is "built-in" interface
in Python, and we can simply use the class itself as that callable, because 
classes are first class objects in Python.
* A way to encapsulate a group of individual factories.