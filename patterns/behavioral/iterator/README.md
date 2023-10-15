### Iterator pattern
Allows one to traverse the elements of a complex data structures without exposing
its internal details.

### Notes:
* Usually, self-made iterators are not efficient and one should use already
optimized ones in popular libraries.
* One can create a class implementing both Iterator and Iterable behaviors by 
adding \__iter__ and \__next__ methods.