### MVC pattern
This is a UI architecture separates an application into three interconnected components: 
the Model (data manipulation, logic), View (GUI), and Controller (user interaction and
connection between the Model and View). It decouples data presentation and access.


### Notes:
* While MVC pattern is a UI pattern, 3-tier is an application architecture pattern.
* The View and Controller both fit into the Presentation layer.
* MVC does not have a separate component for data access, though the Model 
and Logic tiers seem identical.
* Benefit: each component can be developed simultaneously and independently.
* There are also derivatives of this pattern: MVP (Model-View-Presenter) and
MVVM (Model-View-ViewModel).
* Compared to 3-tier, MVC architecture is triangular and components communicate
2 by 2: a->b, b->c, c->a.