### 3-tier pattern
This is a software application architecture that separates presentation (UI), 
application processing, and data management functions. Presentation tier stands 
for a GUI. Application tier stands for the application logic: computing, data processing, etc.
Data tier stands for data storage and management systems.


### Notes:
* While MVC pattern is a UI pattern, 3-tier is an application architecture pattern.
* Benefit: each tier can be developed simultaneously and independently.
* N-tier architecture is also possible but rare.
* A fundamental rule in a three tier architecture is the client tier never communicates 
directly with the data tier; in a three-tier model all communication must pass 
through the middle tier. So the communication between layers is linear:
a->b, b->c; c->b, b->a.