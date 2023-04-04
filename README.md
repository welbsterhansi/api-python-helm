## API Catalog

This is a Python code that implements a simple API catalog using the FastAPI framework. The API provides endpoints for managing user data, including retrieving all users, adding a new user, retrieving a specific user by ID, and checking the health status of the API.

Dependencies
This code requires the following dependencies:

* FastAPI: a modern, fast (high-performance) web framework for building APIs with Python.
* uvicorn: an ASGI server that serves as the interface between the FastAPI application and the outside world.
These dependencies can be installed using the pip package manager with the following command:


##  Functionality

The code defines the following endpoints:

* GET /: This endpoint returns a welcome message indicating the version of the API catalog.

* GET /health: This endpoint returns a JSON response with a status field indicating that the API is functioning properly.

* GET /users: This endpoint returns a JSON response containing a dictionary of users. The users are stored as key-value pairs, where the keys are user IDs and the values are dictionaries containing user information such as name, CPF (Brazilian identification number), and chip number.

* POST /users: This endpoint allows adding a new user to the user dictionary. The user information is provided in the request body as a User model, which is imported from the models module. The endpoint returns a JSON response containing the added user information. If the user ID already exists in the user dictionary, a HTTPException with a 409 status code and a detail message indicating a conflict is raised.

* GET /users/{user_id}: This endpoint allows retrieving a specific user by ID. The user ID is passed as a path parameter. If the user ID is found in the user dictionary, a JSON response containing the user information is returned. Otherwise, a HTTPException with a 404 status code and a detail message indicating that the user ID was not found is raised.
