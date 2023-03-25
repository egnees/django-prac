# Cheat list

# Virtual enviroment installation
+ Go the application root folder and run python3 -m venv venv
+ Then run source venv/bin/activate
+ To deactivate type deactivate

# Django installation via pip3
+ pip3 install "Django==3.0.*"

# Start project and run server
+ django-admin startproject <project_name>
+ python3 manage.py runserver <host>:<port> \--settings=<mysite.settings>
+ python3 manage.py runserver // runs server with host=127.0.0.1, 
port=8000 and default settings

# Create django application
+ python3 manage.py startapp <app_name>

# Create data-base migration
+ python manage.py makemigrations <app_name>

# To see migration SQL queries
+ python manage.py sqlmigrate <app_name> <migration_id>

# Do migration
+ python3 manage.py migrate

# Create superuser
+ python manage.py createsuperuser
