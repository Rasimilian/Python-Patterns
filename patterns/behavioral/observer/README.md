### Observer pattern
Defines a "one-to-many" relationship between objects. While an object's state is 
changed, all dependents get a notification about this change and change too without
coupling to specific classes. 

### Notes:
* Often used in the GUI components to provide a way to react to events happening
in other components.
* If an observer is not detached when needed, one may face Lapsed listener problem and
memory leaks.