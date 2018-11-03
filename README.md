# Reviews API

## Requirements

The main requirements are:

- Python 3.6+
- Django Django==2.1.2
- Django Rest Framework 3.9.0
- Postman

You can see the other requirements inside the requirements files.

## Installing

First you need to activate the environment.

On windows:
```bash
virtualenv env
env\Scripts\activate
```

On linux:
```bash
virtualenv env
source env/bin/activate
```

To install this project you can use `pip` or download individually which library from PyPI.

Using `pip`, you can run the following commands for each environment you want.

```bash
pip install -r requirements.txt
```

## Setting Up

The environment is using SQLite by default, to make easier to run and test the project. 

After setup the DB, you need to run the following commands to have the data scheme right.

```bash
python manage.py makemigrations authentication ratings companies
python manage.py migrate
python manage.py createsuperuser
```

There you will be prompted to enter the superuser credentials: username, email
and password.

## Loading initial data

To load some data into the database you must run the following commands. Being located in the root of the project

```bash
python manage.py loaddata companies.json
python manage.py loaddata reviewers.json
python manage.py loaddata reviews.json
```

## Running

To run this project, you can just run the following command:

```bash
python manage.py runserver
```

This command will run the project in `development` mode.

You can access the admin page by `http://localhost:8000/admin` and using the previous created superuser. 
Then, you can manage the users and their access tokens.

## Testing


To run all the tests, you run the following command:

```bash
python manage.py test
```

## Code coverage


To run all the tests, you run the following commands:

```bash
coverage run --source='api' manage.py test
coverage report
```

## Modeling Design

1) In this challenge I used JSON Web Token instead of DRF Token because nowadays it is considered an standard. Here you can see an answer that explain the difference between eachetter. https://goo.gl/t9ayqA

3) The architecture is based on the 12 factor app statement and the style guide and reference book Two Scoop of DJango 2.

2) Ip address is taken for the request object but It could be also fetched by the frontend.

4) Core module is used basically to implement DRY

5) Reviewers is a custom user module that provides boths authentication and review metadata. In broader cimcurstances is useful separating those concerns and implement some third party package for authentication as  




## API documentation

To take a look at the api endpoints you have to import the ca_challenge.postman_collection.json into Postman 
Also you can visit http://localhost:8000/swagger/ and http://localhost:8000/docs/