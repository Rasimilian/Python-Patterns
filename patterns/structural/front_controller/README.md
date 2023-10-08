### Front controller pattern
Often used for the design of web applications to implement workflows. It is 
a controller that handles all requests for a website and then dispatches to the
appropriate handler for that type of request.


### Notes:
* Centralized control: a front controller handles all the request of the web app.
* It is not possible to scale an app using a front controller since it performs alone.
* The page-controller pattern is an alternative to the front controller approach 
in the MVC model.
* Front controller is a part of MVC pattern which uses one main controller and several
auxiliary controllers.