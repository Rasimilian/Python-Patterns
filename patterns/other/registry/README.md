### Registry pattern
A way to register and access instances within a project, allowing objects to be 
reused across different parts of an application. It creates a map of labels to class 
types, and allows you to access a single registry common to all of those classes. 

### Notes:
* Can be used to hold the Config instances.
* Useful if one wants the manager class to iterate over every available subclass 
and call a particular method on each subclass or if one wants to streamline a factory class, 
which takes an input label (like the name of a class) and creates/returns an object of that type.
* The shared variable REGISTRY is an example of the Borg pattern. 