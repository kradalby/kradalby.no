Title: Installing Nginx on Debian Wheezy 
Tags: webserver wheezy debian nginx
Summary: Installation guide for the latest Nginx on Debian Wheezy

[TOC]

## Add the Official Nginx repository

Download the signed key and add it:

    :::bash
    wget http://nginx.org/keys/nginx_signing.key
    apt-key add nginx_signing.key

Then add the repos to source.list:

    :::bash
    deb http://nginx.org/packages/debian/ codename nginx
    deb-src http://nginx.org/packages/debian/ codename nginx

Remember to swap out codename for the current debian version, as of now, wheezy.

## Install
Now that we have repositories for installing Nginx we can go ahead and do so:

    :::bash
    apt-get update
    apt-get install nginx


## Running a Django app from a suburl
If we want to run a django application from a suburl (kradalby.no/someapp) we need to make the app aware of that path when we send the url to it.
If we use a proxy to send request, add this line:
    
    :::
    proxy_set_header SCRIPT_NAME /myapp;
