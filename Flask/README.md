This Flask folder is used for Interview Preparation, Here the will create a project in which
i will do the following things:
Create Stores  POST   /stores
Create Items    POST   /stores/My_store/item
Retrive all stores and their items  GET /stores
Get a particular store  GET /stores/My_store
Get only a item in a store   GET /stores/My_store/item

So, we will create the 5 endpoints.


I Created a file .flaskenv which is used to set the environment variables needed by the flask to run.
FLASK_APP=app
<!-- FLASK_ENV=development -->
FLASK_DEBUG=1
