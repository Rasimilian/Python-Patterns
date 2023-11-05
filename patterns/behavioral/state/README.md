### State pattern
Manages an object's behavior depending on its internal state. It operates 
state-related behaviors separated into classes of the state interface and 
delegates the work to an instance of these classes, instead of acting on its own.

### Notes:
* Converts massive if-else based state machines into objects.
* Usually, the state transition procedure is implemented to make an object's 
behavior cyclical.
* * It is similar to the Strategy pattern. 
* In Strategy, each implementation is passed to a context object as a parameter 
to replace another one, while States are created by the context object itself.
* State stores a reference to the context object that contains it. Strategy does not. 
* State is allowed to replace other implementations while Strategy is not. 
* Strategy only handles a single, specific task, while State provides the underlying 
implementation for most everything the context object does.