### Singleton pattern
Singleton pattern restricts the instantiation of a class and ensures
that only one instance of the class exists. The singleton class must provide
a global access point to get the instance of the class. Singleton pattern is
used for logging, drivers objects, caching, connections, and thread pool.

### Notes:
* In Python, one should avoid monkey patching due to lack of class field encapsulation.
* In Python, one have to synchronize threads during the first creation of the Singleton object.
* The best to read Singleton implementation is a classical implementation.
* Global instance is considered to be an anti-pattern.
* Single responsibility principle is violated since a class controls its own creation and lifecycle.
* It complicates the testing process due to coupled code and carrying a state around for the program lifetime.
* If another Singleton class or its methods are called in the base Singleton's __init__ a deadlock will be raised.
* Double-checked locking optimization should be used for thread-safety and performance.