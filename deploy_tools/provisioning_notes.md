Provisioning a new site
==========================

## Required packages:

* nginx
* python 3.6
* virtualenv + pip
* Git

eg, on CentOS:
    
    yum install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com
* replace PWD with email password

## Folder structure:
Assume we have a user account at /home/username

/home/username
|-- sites
    |-- SITENAME
         |-- database
         |-- source
         |-- static
         |-- virtualenv