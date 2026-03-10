### Developer Guide
Get started developing by following this guide.

## Package manager
turtle uses the [poetry](https://python-poetry.org/) package manager to manage its dependencies. To install the dependencies, run the following command:
```
poetry install
```
See the [poetry](https://python-poetry.org/) documentation for more information and
installation instructions.

## Running the app
You'll need to have [Docker installed](https://docs.docker.com/get-docker/).

#### Clone this repo and move into the directory
```shell
git clone https://github.com/galacticglum/turtle-game.git
cd turtle-game
```

#### Copy starter files
```shell
cp .env.example .env
```
The defaults are for running in *development* mode. Go through each variable in the file and make sure it is properly set. You will likely need to update the credentials. Once the file is updated, run
```shell
source .env
```
to load the environment variables into your shell. This is important as the Makefile and Docker Compose commands rely on these variables.

#### Build the Docker image and start the Docker container

You start the Docker container by running

*The first time you run this, it's going to take 5-10 minutes depending on your internet connection and hardware.*
```shell
make dev.up
```
This will build the image, if needed, and once built, automatically spin up a container with the image. If you'd like to force a rebuild of the image, you may additionally pass an optional ``c="--build"`` argument to the command.

#### Stopping the Docker container

You can stop running the container by running ``make dev.down``, which will stop the container and remove it. If you'd like to stop the container without removing it, you can run ``make dev.stop``. To remove everything, including the volumes, run ``make dev.destroy``.

#### Setting up the database

turtle uses MongoDB, a NoSQL database program. If you're using Docker, an instance of MongoDB is already setup for you. Optionally, you can run an instance locally or use a number of database providers. sure you update the ``.env`` file with your instance information (host, credentials, and db name).

## Native Development Environment
If you prefer to work natively, rather than bootstrapping the application in a Docker container, see the [native development workflow](docs/develop-native.md) docs for setup instructions.