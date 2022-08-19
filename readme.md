## Make sure you have python, pip

## Install virtual

python3 -m venv virt

## start virtual 

source virt/bin/activate

## to deactivate virt

deactivate

## To install flask dependences 

pip install flask

## install flask session

pip install Flask-Session

## Check if it got installed correct

flask --version

## Check what installed in the virtual enviroment

pip freeze

## set variables

export FLASK_ENV=development

### Add app.py

export FLASK_APP=app.py

### Debug mode: on

export FLASK_DEBUG=1 

### Run app

flask run

# DB