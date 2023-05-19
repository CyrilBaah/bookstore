# Bookstore API
Bookstore API

## Technology Stack
- [Python](https://www.python.org/ "python")
- [Postgres](https://www.postgresql.org/ "Postgres")
- [Django](https://www.django-rest-framework.org/ "Django")

## Formatter or Linters
- [Flake8](https://flake8.pycqa.org/en/latest/index.html# "Flake8")
- [Black](https://black.readthedocs.io/en/stable/ "Black") 
- [Isort](https://pycqa.github.io/isort/ "Isort")

## Generate API documentation

```sh
$ ./manage.py spectacular --color --file schema.yml
```

## Generate Seeder
- Users
```sh
 ./manage seed_users
```