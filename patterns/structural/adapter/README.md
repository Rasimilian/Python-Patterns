### Adapter pattern
Due to different interfaces, classes can't be easily integrated into a code snippet.
For two incompatible interfaces of classes, this pattern transforms one interface to 
another one a client needs. It makes a collaboration between two classes having inconsistent
interfaces without changing these objects. 

### Notes:
* Often used in the systems with legacy code to make integrations with modern classes.
* In other languages, the Adapter implementation via inheritance would be more typical by using
class extension and interface implementation.
* In Python, the Adapter class can be made of inheritance or composition (when an object
is passed as an argument for its method further call)
* There is no need to create the Adapter class. One may create just a wrapper function
instead.
* The Adapter pattern makes things work after they're designed; Bridge makes them 
work before they are.