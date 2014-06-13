Title: uWSGI and Nginx on Debian Wheezy
Tags: nginx, uwsgi, django, python, debian
Summary: Setup instructions for uWSGI on Debian Wheezy.

[TOC]


Preconditions: Nginx is installed on the server.

We will set up uWSGI in emperor mode, which basicly means that a uWSGI daemon will spawn a master with workers for every uWSGI application we got.


## Install uWSGI 
We are going to install uWSGI via pip, so we need to install:

    :::bash
    apt-get install build-essential python python-dev

Now install the latest version through pip:
    
    :::bash 
    pip install uwsgi

Create a /etc directory for the uWSGI application ini files:

    :::bash 
    mkdir -p /etc/uwsgi/apps-available
    mkdir -p /etc/uwsgi/apps-enable

Now get the init script:

    :::bash
    cd /etc/init.d
    wget https://gist.githubusercontent.com/kradalby/3252b8bacca6622bf864/raw/0d6d2b034284a8256c646433782ee0217b04c437/uwsgi

    # Make it start automaticly
    update-rc.d uwsgi defaults

[Link to gist](https://gist.github.com/kradalby/3252b8bacca6622bf864)

## Application configuration

### Python/Django
Currently i only got Django applications running on uWSGI. Below you will find a sample config from one of my applications:

    :::bash
    [uwsgi]
    socket          = /srv/www/dfektlan.no/lanweb/dfektlan.sock
    chdir           = /srv/www/dfektlan.no/lanweb
    wsgi-file       = dfektlan/wsgi.py
    env             = DJANGO_SETTINGS_MODULE=dfektlan.settings
    chmod-socket    = 664
    home            = /srv/www/dfektlan.no/env
    vacuum          = true
    master          = true
    processes       = 10
    daemonize       = /var/log/uwsgi/dfektlan.log


## Controlling uWSGI

With the provided init script you can use the debian standard service command to control uWSGI:

Stop, start restart:

    :::bash
    service uwsgi start
    service uwsgi stop
    service uwsgi restart

Reload:
    
    :::bash
    service uwsgi reload

    # Or the send command directly
    uwsgi --reload /var/run/uwsgi/uwsgi.pid

A neat feature uWSGI also has, is auto reload if a config file for a application is changed. So every time you change a .ini file which is linked to the apps-enabled directory it will reload that particular app.
