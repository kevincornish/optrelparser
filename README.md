# Optrel Parser

The Optrel Parser is a django/python script that enables you to import batch reports and audit logs to a postgres database from any Optrel Inspection machine that is using WinCC Flexible PVSI which will then enable you to view them in a readable user friendly website.

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

## Settings

Located in ``` /optrel/.env.example ```, fill this with the correct environment varibles before continuing and rename to ``` .env ```

## Run migrations
```bash
python manage.py migrate
```

## Storing / Importing data

### PDF location
```
"/files/vials"
"/files/ampoules"
```
### CSV location
```
"/files/vial_audit"
"/files/ampoule_audit"
```
### Importing

Use the --truncate args to start fresh

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

To view imported batch data
```
localhost:8000/ampoules

localhost:8000/vials
```

You must be logged in to view these pages!

## Stylesheets 
The stylesheet located at ``` /static/reports/style.css ``` will need to be updated to match your production recipes

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
