### Borg pattern
Provides singleton-like behavior sharing state between instances.
Compared to Singleton, this pattern focuses on sharing state instead
of sharing instance identity, meaning that there are several instances possible.
Perhaps, the use cases are the same as for Singleton: connections, logging, etc.

### Notes:
* While subclassing, all child classes will have the same state as their parent classes
unless the shared state is explicitly overriden.
* To change class fields, one may use Setter/Getters in Pythonic way but 
with the help of thread-locking constructions.
* Borg can be also implemented via the Meta Class concept.