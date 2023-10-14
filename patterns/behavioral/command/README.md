### Command pattern
Encapsulates a request into an object. It decouples the object invoking a job
from object doing a special action (example: each press button invokes specific 
object to perform a specific command).

### Notes:
* Most often it’s used as an alternative for callbacks to parameterizing UI elements 
with actions. It’s also used for queueing tasks, tracking operations history, logging, etc.
* The conversion allows deferred or remote execution of commands, storing command 
history, cancelling, etc. Putting simply, such command objects will have additional 
properties.
* It also can be thought of as an object-oriented implementation of callback functions.
Since one pass a command object as an argument.
* In command classes, there can be a receiver, another object which will finally
get a command to specific actions.