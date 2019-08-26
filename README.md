# Cuenca Docker Compose

|Service| Service Name | Host | Port |
|---|---|---|---|
| Databases | db | db.cuenca-dev.com | 5432 |
| Puzzle | app | shell.cuenca-dev.com | - |

## Setting everything up

1. Add the following entries to your `/etc/hosts` file.

  ```
  # Services

  127.0.0.1  db.cuenca-dev.com
  127.0.0.1  app.cuenca-dev.com
  ```

2. Install docker https://www.docker.com/get-docker
3. Install docker-compose https://docs.docker.com/compose/install/
4. Start the **docker-compose** service.

## Basic Usage

- Enter in compose `cd compose`

- Build all services `docker-compose up --build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

- Open a shell `docker-compose exec [service_name] /bin/sh`

- Open a shell `docker-compose run [service_name] /bin/sh`

## Commitize

1. Install Commitizen https://github.com/commitizen/cz-cli#installing-the-command-line-tool
2. Initialize the Commitize on project

```
$ npm init --yes
$ npm install commitizen -g
$ commitizen init cz-conventional-changelog --save-dev --save-exact
```
3. Run commitizen after create a new changes on the project

```
$ git add .
$ git cz
```
