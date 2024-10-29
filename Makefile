# Need to import values from .env
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

DC = docker compose
DB_FILE = docker_compose/db.yaml
APP_FILE = docker_compose/app.yaml
APP_PROD_FILE = docker_compose/docker-compose.prod.yaml
EXEC = docker exec -it
DB_CONTAINER = opinions-db
APP_CONTAINER = opinions-app
LOGS = docker logs
ENV = --env-file .env


.PHONY: db
db:
	${DC} -f ${DB_FILE} ${ENV} up -d

.PHONY: db-down
db-down:
	${DC} -f ${DB_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}

.PHONY: db-logs
db-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${DB_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${DB_FILE} down

.PHONY: app-container
app-container:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} flask db upgrade


.PHONY: app-prod
app-prod:
	${DC} -f ${APP_PROD_FILE} ${ENV} up --build -d

.PHONY: app-prod-down
app-prod-down:
	${DC} -f ${APP_PROD_FILE} down
