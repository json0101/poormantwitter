# Scrummers test, Vue and Django

## Project setup frontend
```
  1) Install package: 
    npm install
  2) Run Project: 
    npm run serve
```

## Project setup backend
```
  1) Create a virtual environment to isolate our package dependencies locally
    python3 -m venv env
    source env/bin/activate  (On Windows use `env\Scripts\activate`)

  2) Install Django and Django REST framework into the virtual environment
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
  
  3) Migrations
    python manage.py makemigrations
    python manage.py migrate
    
  4) Run Project
    python manage.py runserver
```
