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

Before running project you have to set environment variables in .env file

```
touch .env
```

specify following variables inside .env file:

```
SECRET_KEY="{your secret key for project}"

# use False in deployment
DEBUG=True

ALLOWED_HOSTS="localhost,127.0.0.1"

```

## Running the tests

Tests will be located in shopapp/test folder

```
python3 manage.py test
```

## Deployment

currently there are no deployment details

they will be added soon

## Authors

- [github.com/saparmuratxo](https://github.com/saparmuratxo/)
