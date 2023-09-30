### Flyweight pattern
Focuses on minimizing the number of objects required by a program at run-time.
It is achieved by sharing (caching) parts of object state between multiple objects. It 
becomes indistinguishable within the shared states of interest from an object 
that is not shared. The shared state (object attributes, etc.) should not be 
affected by the object's context (attributes, additional info, etc.). This makes 
the Flyweight object unique, immutable and being shared. Once such objects 
have been created, they can't be modified.


### Notes:
* Minimizing the number of objects means performance increase and reducing 
the memory usage.
* Same concepts can be met in the Pool Pattern description.
* Since it uses the idea of Pool one may require thread-safe constructions.