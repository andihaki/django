# django 
# vent
django
source /bin/activate

## DB ORM
create db connection in models.py
python manage.py migrate
python manage.py makemigrates app_name

interactive command
python manage.py shell

>>> from app_name.models import class_name
>>> t = class_name(column="value")
>>> t.save()
>>> print(class_name.objects.all())
>>> quit()

import models di admin.py

python manage.py createsuperuser

# venv
## start venv
source bin/activate

## stop venv
deactivate

# command
## create project
django-admin startproject project_name

## create app
django-admin startapp app_name

supaya bisa akses ke app_name, tambahkan 'app_name' ke file settings.py, di bagian INSTALLED_APPS
