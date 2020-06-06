# spotify-grinder

## Basic Usage
1. First add in /.envs, /.envs/.django and .envs/.postgres there format is shown here [envs](#envs)
2. run **`make build`** inside root directory.
3. Then run **`make up`** to start up the project for first time.
4. Use/update environment variables from [**`.envs`**]
Checkout the [commands](#commands) section for more usage.

## Envs
`.django`     DB_HOST=db
              DB_PORT=5432
              DB_PASSWORD=password
              DB_USER=user
              DB_NAME=django_db

`.postgres`   POSTGRES_HOST=db
              POSTGRES_PORT=5432
              POSTGRES_USER=user
              POSTGRES_PASSWORD=password
              POSTGRES_DB=django_db


## Commands
To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.
16. `make prune` to delete all stopped containers and cached data
17. `make ps` to list all active containers
18. `make deploy` to list django's deployment checklist more at https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
