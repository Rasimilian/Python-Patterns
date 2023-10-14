### Chain of responsibility pattern
Decouples the senders of a request from its receiver by moving the request through
chained receivers till the end (when it is handled). Receivers are connected via references 
and all have access to a request to handle it.

### Notes:
* Some receivers can send requests in several directions forming a tree of responsibility.
* Receivers share the common interface.
* Chain of responsibility is an alternative to if-else blocks which can be dynamically
rearranged and reconfigured at runtime. A receiver has two options: to handle a 
request or to pass it to the next receiver.