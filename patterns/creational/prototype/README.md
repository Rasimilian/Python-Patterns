### Prototype pattern
Dynamically, at run-time, this pattern creates objects by copying a prototype instance 
without specifying concrete classes. It is possible to make either a shallow or 
deep copies having nested data structures. It can be used when instances to be cloned 
can only have a few different state configurations or when new object instantiation is 
computationally expensive.

### Notes:
* It is possible to override "magic" \__copy__ and \__deepcopy__ methods of a Prototype class 
and to use built-in copy.copy() and copy.deepcopy() methods on the class.
* Pay attention to deepcopy's memo arguments. It prevents from making copies of recursively
referenced objects.
* Pattern also prevents from creating complex class hierarchy and subsequent subclassing 
since it can be redundant.