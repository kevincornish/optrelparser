# Getting Started

## Create postgres database
`psql postgres`
`create database optrel_reports;`

## Install Requirements
`pip install -r requirements.txt`

## Run migrations
`python manage.py migrate`

## Import Vials
`python manage.py import_vials`

## Create superuser
`python manage.py createsuperuser`

## Run Server
`python manage.py runserver 8000`

## Login to admin site
`localhost:8000/admin`