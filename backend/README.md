## Run Local/Production Backend Stack

The project contains 2 different environments:

    **Local Stack**: It is used to run a local development environment.
    **Production Stack:** It is used to run a production environment.

The following commands will show you how to build and run the local environment.

    $ make build_backend
    $ make start_backend

Before running the above commands locally make sure project environment variables are set. In order to do that create a new directory
`.env` inside `docker/local` directory and create two files `.server` and `.postgres` for storing the env variables. 
These files will look something like this

### .server

```
USE_DOCKER=yes
DATABASE_URL=postgres://root:password@presentations_database:5151/presentations
DJANGO_SECRET_KEY="oXZwZXaJeoNwrxCizzaZmqvY9pQLjyJFS8vqWguIUuu2x28wZc1l4TXYSb2Hk6E4"
CORS_ALLOWED_ORIGINS="http://localhost:3000,http://frontend:3000"
```

### .postgres

```
POSTGRES_HOST=presentations_database
POSTGRES_PORT=5151
POSTGRES_DB=presentations
POSTGRES_USER=root
POSTGRES_PASSWORD=password
```

## How to Get Inside the Docker Container

It is necessary to get inside the docker container of the local stack, since it has all required libraries. To do so,
make sure the local environment is up and running.

Run the following command to get inside the "**presentations_backend**" container::

    $ make bash

Now, you are inside the Docker container and should see a location similar to this::

    root@32bf7e05723c:/app/

## How to Run Sanity Checks

In this section, you will find information of how to run the sanity checks to guarantee a good quality code.

## Unit Tests

The unit tests of the application are written using pytest. It is a framework that makes building simple and scalable
tests easy.

### Run All Unit Tests

In order to run all Python unit test, simply run the following command::

    $ make test_backend

### Run Specific Unit Test

In order to run a specific Python unit test, simply run the following command::

    $ make test_backend MODULE=<path_python_test_file>::<test_module>::<test_name>

For example::

    $ make test_backend MODULE=server/presentations/tests/test_api_views.py::TestPresentationAPIView::test_list_presentation


### Code Coverage

Test coverage is a technique which determines whether our test cases are actually covering the application code and how
much code is exercised when we run those test cases.

In order to generate an HTML code coverage report for Python unit tests, simply run the following command::

    $ coverage run -m pytest
    $ coverage html


Finally, to open the HTML coverage report simply run the following command in another terminal (not inside Docker
container)::

    $ open htmlcov/index.html


## Basic Commands

In this section, you will find some basic commands for the application.


### Load Presentations Data

To populate the presentations data from JSON file run the following command

    $ make load_data


### Setting Up Your Users

In this section, you will find information of how to create a **superuser** account.


#### Superuser Account

To create a **superuser** account, simply run::

    $ make superuser

After creating a **superuser account**, you can check the admin access in the following link to make sure
it was created successfully:

`<http://0.0.0.0:8000/admin/>`_


#### Localization

To create a django .po and .mo files::

    $ make makemessages
    $ make compilemessages

Make sure to update translations before compiling the translations


## Open a Shell

Django comes with a python shell where you can import your models and test things out.

In order to open a shell, simply run the following command::

    $  make shell

This opens up a terminal, but it has the Django settings already imported, so it allows you to work directly from the
root folder of a Django project.

There is another Django interactive shell called **shell_plus**. It auto-import all models, and the datetime module.

In order to open a **shell_plus**, simply run the following command::

    $ make shell_plus


## Auto formatting code

We make use of `isort` and `autopep8` to automatically format our code base. These tools can be used from the command line as follows:

isort:

    $ docker exec -it presentations_backend isort <file>
    $ docker exec -it presentations_backend isort -rc <folder>

autopep8:

    $ docker exec -it presentations_backend autopep8 -i <file>
    $ docker exec -it presentations_backend autopep8 -ir <folder>

If you want to check this manually without running the testing suite you can with the following command:

    $ docker exec -it presentations_backend flake8 <file/folder>
