# Getting Started

## Create postgres database
`psql postgres`
`create database optrel_reports;`

## Install Requirements
`pip install -r requirements.txt`

## Run migrations
`python manage.py migrate`

## Import Vials & Ampoules
`python manage.py import_vials`
`python manage.py import_ampoules`

## Create superuser
`python manage.py createsuperuser`

## Run Server
`python manage.py runserver 8000`

## View data
`localhost:8000/ampoules`
`localhost:8000/vials`

## Login to admin site
`localhost:8000/admin`
