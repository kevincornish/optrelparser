# Optrel Parser (Stevanto / S.P.A.M.I)
The Optrel Parser (Stevanto / S.P.A.M.I) is a django/python script that enables you to import batch reports (.pdf) and audit logs (.csv) to a postgres database from any Optrel Inspection (I was using the MCA 150 and MCA 200 LKD machines) machine that is using WinCC Flexible PVSI which will enable you to view them in a readable, user friendly website. 

I created this script due to there being no way to tie processed batch reports to their corresponding audit log, this program will highlight any issues that have happened while inspection has taken place. e.g common faults such as safety clutche slips or having to remove a vial manually when it faults to the wrong reject channel

# Screenshots
### List of batches processed
![Image](https://i.ibb.co/j3km3kJ/batchlist.png)

### Batch report detail view
![Image](https://i.ibb.co/0XT2Chj/detailview.png)

# Features
- Import batch report .pdf's
- Import audit log .csv's
- Authentication is required before viewing any reports

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

I created a batch script making use of Robocopy on windows to automatically retrieve all newly created audit logs / batch reports from the machines and copy to the projects directory nightly.

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
## Importing

Use the ``--truncate`` argument to empty table before importing

```
python manage.py import_vials
```
```
python manage.py import_ampoules
```
```
python manage.py import_ampoule_audit
```
```
python manage.py import_vial_audit
```
These can take a long time to run on first import

## Create superuser
```
python manage.py createsuperuser
```

# Running Server
## First we create a superuser
```
python manage.py createsuperuser
```
## Run the server
```
python manage.py runserver 8000
```

## View data
To view imported batch data
```
localhost:8000/ampoules
```

```
localhost:8000/vials
```
You must be logged in to view these pages!

## Stylesheets 
The stylesheet located at ``` /static/reports/style.css ``` will need to be updated to match your inspection machines recipes - starting at ```line 371```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Tech
Optrel Parser uses a number of open source projects
* [Heroku](https://www.heroku.com/) - I used this to deploy my original project
* [Django](https://www.djangoproject.com/) - Python Web Framework
* [POSTGRES ](https://www.postgresql.org/) - PostgreSQL is a powerful, open source object-relational database system.
