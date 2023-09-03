### Lazy evaluation pattern
It is an evaluation strategy which delays the expression evaluation until the result
of the expression is needed. It also avoids repeated evaluations by using the sharing
and caching mechanisms.

### Notes:
* Helps to reorganize and optimize computational load of a program: to execute a code and 
allocate memory by need.
* It is possible to define large data structures avoiding instantaneous memory usage and 
to retrieve the values when needed.
* In Python, lazy evaluation is implemented in built-in functions: range(), zip(), open(), map()...
* It is better to implement lazy functions instead of lazy properties since Python's static analyzer
warns that the method wrapped in @property should be callable.