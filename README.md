[![Python](https://img.shields.io/badge/Python-3.12.2-3776AB?style=flat&logo=Python&logoColor=yellow)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL--336791?style=flat&logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![Flask-SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-D71F00?style=flat&logo=sqlalchemy&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker--2496ED?style=flat&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Psycopg2](https://img.shields.io/badge/Psycopg2-2.9.10-4169E1?style=flat)](https://pypi.org/project/psycopg2-binary/)

# Simple Flask WebApp with Docker Compose, Makefile, and PostgreSQL

## Table of Contents

- [Project Description](#Project-Description)
- [Requirements](#Requirements)
- [Quick Start](#Quick-Start)
- [Project Structure](#Project-Structure)
- [API Endpoints](#API-Endpoints)
- [Implemented Makefile Commands](#Implemented-Makefile-Commands)
- [License](#license)

## Project Description

This project is a simple Flask web application that generates random opinions about movies and allows users to interact with these opinions.Key features include:
- ***Retrieve a Random Opinion:*** Users can get a random opinion about a movie.
- ***View Specific Opinions:*** Navigate to specific opinion details through direct links.
- ***Add New Opinions:*** Users can contribute their own movie opinions.


### Features
- ***Flask:*** Straightforward project structure with configurations for easy local setup.
- ***Docker Compose:*** Manages containerized services for the Flask app and PostgreSQL database.
- ***PostgreSQL:*** Configured as the default database, ready to run in a Docker container.
- ***Makefile:*** Simplifies common tasks, such as building containers, starting/stopping services, and running migrations.
- ***Environment Variables:*** .env.example included to simplify configuration of database credentials and other sensitive settings.

## Requirements
*To use this app, ensure you have the following installed on your machine:*

- ***Docker:*** Required for containerizing the Django application and PostgreSQL database.
  - [Install Docker](https://docs.docker.com/get-docker/)
- ***Docker Compose:*** Used to manage multiple Docker containers in a single setup.
  - Docker Desktop includes Docker Compose. Alternatively, install it separately: [Docker Compose Installation](https://docs.docker.com/compose/install/)
- ***Make:*** Allows simplified command execution using the Makefile.
  - *Linux/macOS:* Make is usually pre-installed. If not, install it via your package manager:
```sh
   # Ubuntu/Debian
   sudo apt install make

   # macOS (with Homebrew)
   brew install make
```
  - *Windows:* Use make with [Git Bash](https://gitforwindows.org/) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux).

## Quick Start

1. **Clone the repository:**

   ```sh
   git clone https://github.com/dev-lymar/
   cd
   ```

2. Setup environment variables from .env.example:
```sh
    cp .env.example .env
```

3. Run project
```sh
   make app
```

## Project Structure

*The project structure is organized to keep core components isolated and manageable:*

```sh
.
├── .env
├── Dockerfile
├── entrypoint.sh
├── Makefile
├── LICENSE
├── README.md
├── app
│   ├── static/
│   ├── templates/
│   ├── api_views.py
│   ├── cli_commands.py
│   ├── error_handlers.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
└── docker_compose
    ├── app.yaml
    ├── db.yaml
    └── docker-compose.prod.yaml
```

## API Endpoints
*The API provides the following endpoints for interacting with opinions:*

1. **Get, Update, or Delete a Specific Opinion**
- Endpoint: `/api/opinions/<id>/`
- Methods: `GET` (retrieve a specific opinion), `PATCH` (update an opinion), `DELETE` (remove an opinion)

2. **Retrieve List of Opinions or Add New Opinion**
- Endpoint: `/api/opinions/`
- Methods: `GET` (retrieve all opinions), `POST` (add a new opinion)

3. **Get Random Opinion**
- Endpoint: `/api/get-random-opinion/`
- Methods: `GET` (retrieve a random opinion from the database)


## Implemented Makefile Commands

* `make app` - Starts the application and database infrastructure.
* `make app-logs` - Follow the logs in app container.
* `make app-container` - Connects to the application container for interactive commands.
* `make app-down` - Down application and all infrastructure.

* `make db` - Up only infrastructure. You should run your application locally for debugging/developing purposes.
* `make db-logs` - Follow the logs in storages containers.
* `make db-down` - Down all infrastructure.
* `make postgres` - Enter postgres container.

* `make migrate` - Runs database migrations inside the app container.

* `make app-prod` - Launches the application in production mode with production-specific settings.
* `make app-prod-down` - Stops and removes the production setup.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
