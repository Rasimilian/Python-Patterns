### Strategy pattern
Defines a family of classes, encapsulates each one and makes them interchangeable.
Each class can be varied independently by a user at runtime.

### Notes:
* It is similar to the State pattern. 
* In Strategy, each implementation is passed to a context object as a parameter 
to replace another one, while States are created by the context object itself.
* State stores a reference to the context object that contains it. Strategy does not. 
* State is allowed to replace themselves while Strategy is not. 
* Strategy only handles a single, specific task, while State provides the underlying 
implementation for most everything the context object does.