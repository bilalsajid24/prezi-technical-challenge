## Run Frontend Stack

The following commands will show you how to build and run the local environment.

    $ make build_frontend
    $ make start_frontend

The environment variables are already set in .env and .env.test files


### Unit Tests

In order to run all Python unit test, simply run the following command::

    $ make test_frontend


### Code Coverage

In order to run all unit test, simply run the following command::

    $ docker-compose -f frontend/docker-compose.yml run --rm frontend npm run test:coverage


## Linting

In order to see linting errors and/or fix them, run the following command

    $ docker-compose -f frontend/docker-compose.yml run --rm frontend npm run lint
    $ docker-compose -f frontend/docker-compose.yml run --rm frontend npm run lint:fix
