### Builder pattern
It decouples the creation of a complex object and its representation to build objects
with many possible configurations. By doing so, the same construction process can create different representations.

### Notes:
* Usually, there is a single creation method and several methods to configure the object.
* It makes sense to use the Builder pattern only when your products are quite complex and 
require extensive configuration.
* A more pythonic way to add Setters/Getters methods is to use decorators.
* Instead of the optional Director class, one may encapsulate configure methods in the __init__ for simple objects 
and in an external constructor function for complex objects.
* The Director can construct several product variations using the same building steps.
* Concreate Builder classes (IphoneBuilder, RedmiBuilder) are used to create the concrete representations and
not for subclassing. Each such class can have its own interface and objects.