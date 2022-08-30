# Tasksapp CS50x 2022

Using Flask to build task management app for people with ADHD.

Extensions:

* Flask-Session

* Flask-SQLalchemy

* Flask-login

# Installation

## Install flask with pip from requirements:

    $ pip install -r requirements.txt

## Run Flask app:

    flask run

## Initial setup of a flask project

1. Make sure you have python, pip installed.

2. Install virtual enviroment:

        python3 -m venv virt

3. Run virtual enviroment:

        source virt/bin/activate

    * to deactivate virtual enviroment:

            deactivate

    * Check what installed in the virtual enviroment:

            pip freeze

4. To install flask with dependences:

        pip install flask

    * Check if it got installed correct:

            flask --version

5. Set variables:

        export FLASK_ENV=development

6. Debug mode: on (if needed for development):

        export FLASK_DEBUG=1 

7. Add app.py:

        export FLASK_APP=app.py

### Flask-Session installation

1. Install flask session:

        pip install Flask-Session

### Database

1. Install sqlalchemy:

        pip install flask-sqlalchemy

2. Open interactive python:

        python3

3. Import and create database:

        from app import db

        db.create_all()

### Login

1. Install flask login:

        pip install flask-login


### Add requirements for easier installation:

    pip freeze > requirements.txt