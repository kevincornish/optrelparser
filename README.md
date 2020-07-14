# Optrel Parser

The Optrel Parser is a django/python script that enables you to import batch reports and audit logs to a readable user friendly website using postgres.

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
python manage.py import_vials

python manage.py import_ampoules

python manage.py import_ampoule_audit

python manage.py import_vial_audit
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

## Login to admin site
```
localhost:8000/admin
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.