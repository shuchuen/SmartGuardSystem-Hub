# SmartGuardSystem-ControlHub



## Environment

### Prerequisite

- python 3.10

### Install python dependencies

- `brew install pyenv pipenv`
- `pipenv install`

### Run development server

```bash
python manage.py runserver
# or
pipenv run server
```

It will start a local server at `localhost:8000` and you can access the API
The API document at `localhost:8000/redoc/` or `localhost:8000/swagger-ui/`

### Django ORM migrations

> Run these two commands only when changes are made to the Django models

```bash
# create migration files
python manage.py makemigrations
# or
pipenv run makemigrations

# apply the migration operations
python manage.py migrate
# or
pipenv run migrate
```

### Testing

```bash
python manage.py test
```

## API Document

This project uses [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) to generate the Redoc and OpenAPI schema.

- Redoc
  - [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- OpenApi 3.0 Schema (JSON)
  - [http://localhost:8000/schema/](http://localhost:8000/schema/)
- swagger ui
  - [http://localhost:8000/swagger-ui/](http://localhost:8000/swagger-ui/)

<img width="1216" alt="image" src="https://user-images.githubusercontent.com/10266845/193379071-4bbb1563-86fe-405b-ac7d-c1380d39d8db.png">


## ER dirgram
![diagram](https://user-images.githubusercontent.com/10266845/193379035-705450c8-d577-4a1e-9909-c7cb98c13443.png)


## Run Celery

Make sure install the redis

```bash
sudo celery -A smart_guard_api worker -l INFO
```