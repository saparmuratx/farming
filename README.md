# Farming

## Installing

---

Execute following CLI commands on your machine

```
# setup virtual environment inside project folder
$ python -m venv venv

# activate virtual environment
$ source /venv/bin/activate

#install all dependencies

$(venv) pip install -r requirements.txt 
```

Before running project you have to set environment variables in .env file. When running without Docker.

```

touch .env

```

specify following variables inside .env file:

```

SECRET_KEY="{your secret key for project}"

## use False in deployment

DEBUG=True

ALLOWED_HOSTS="localhost,127.0.0.1"

DB_ENGINE="django.contrib.gis.db.backends.postgis"
DB_NAME="gis"
DB_USER="user001"
DB_PASSWORD="123456789"
DB_HOST="localhost"
DB_PORT="5432"

```

<!-- ## Running the tests

Tests will be located in shopapp/test folder

```
python3 manage.py test
``` -->

## Deployment with Docker

There is a Dockerfile and docker-compose.yml for deploying with Docker

You can configure some environment variables in docker-compose.yml:

```

web:
    environment:
      - DB_NAME=gis
      - DB_USER=user
      - DB_PASSWORD=password

```

After configuring run:

```

docker compose up

```

## Authors

- [github.com/saparmuratxo](https://github.com/saparmuratxo/)
