# Optrel Parser
The Optrel Parser is a django/python script that enables you to import batch reports and audit logs to a postgres database from any Optrel Inspection machine using WinCC Flexible PVSI and view them in a readable user friendly website.

# Installation
## Create Postgres database
```bash
psql postgres
create database optrel_reports;
```
## Install requirements
```bash
pip install -r requirements.txt
```

## Settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'optrel_reports',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## Run migrations
```bash
python manage.py migrate
```

## Importing data

PDF location:
```
"/files/vials"
"/files/ampoules"
```
CSV location:
```
"/files/vial_audit"
"/files/ampoule_audit"
```
```
python manage.py import_vials --truncate

python manage.py import_ampoules  --truncate

python manage.py import_ampoule_audit --truncate

python manage.py import_vial_audit --truncate
```

## Create superuser
```
python manage.py createsuperuser
```
# Running Server
```
python manage.py runserver 8000
```
## View data
```
localhost:8000/ampoules

localhost:8000/vials
```
## Stylesheets 
The stylesheet is located at ``` /static/reports/style.css ``` will need to be updated to match your production recipes
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.