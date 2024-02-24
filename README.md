# Bookstore API | DevSecOps CI/CD pipeline
The Bookstore API is a RESTful API built with a focus on DevSecOps practices to ensure security throughout the development lifecycle.

## Technology Stack
- [Python](https://www.python.org/ "python")
- [Postgres](https://www.postgresql.org/ "Postgres")
- [Django](https://www.django-rest-framework.org/ "Django")

## Formatter or Linters
- [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")
- [Black](https://black.readthedocs.io/en/stable/ "Black") 
- [Isort](https://pycqa.github.io/isort/ "Isort")

## Run test cases
- Users
```sh
 ./manage test
```

## How to set up locally using Docker container - **Recommended**
### Prerequisite
- Make sure **Docker** is installed locally. *Checkout installation here* [Docker](https://www.docker.com/ "Docker")
- Make sure **Postgres** is installed locally. *Checkout installation here* [Postgres](https://www.postgresql.org/ "Postgres")

1. Clone the project.
```sh
 git clone https://github.com/CyrilBaah/bookstore.git
```
```sh
 cd bookstore
```
2. Change the env.example file to .env 
3. Run 
```sh
 docker-compose build --no-cache
```
4. Run 
```sh
 docker-compose build up
```

## Generate API documentation

```sh
$ ./manage.py spectacular --color --file schema.yml
```

## Generate Seeder
- Users
```sh
 ./manage seed_users
```
## Get docker image | PostgreSQL DB IP
```sh
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name
```

## Features in the DevSecOps Pipeline
- 