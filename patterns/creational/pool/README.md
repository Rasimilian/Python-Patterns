### Pool pattern
The pool of objects uses a set of initialized objects that are ready to be used
or reused instead of creating new ones. It is useful when creating a new object
is costly, occurs frequently, and only a few are used at a time. Putting simply, 
we reuse inactive objects instead of additional object creation.

### Notes:
* ObjectPool class can be a wrapper (context manager) to be used the "with" statement.
After exiting the pool, it would reset all settings for the further reusing.
* One can create methods for managing (divide, get, remove, add...) used or unused object.
* It is possible to specify the max limit of objects stored.
* Pool can encapsulate different queue-like structures to store items.
* The ObjectPool class is better to be Singleton.