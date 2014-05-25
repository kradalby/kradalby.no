Title: Using Nginx to serve bootstrap script
Tags: nginx, bootstrapping, debian, lazy
Summary: Using Nginx to serve bootstrap script

In this post i will walk through the easy steps on how to host a bootstrap script on Github and make it possible to proxy it through a shorter domain.

The goal is to be able to setup the basic needed stuff on a new server with one simple command. The same way you install Oh my zsh and Brew.

I choose to host the script on Github as this provides me with flexibility and ease when i need to update and keep track of it.

In this example, i will use [this](https://raw.githubusercontent.com/kradalby/scripts/master/bs.sh) which i use to bootstrap Debian servers i use.

In my Nginx configuration file for the used domain, i have this:

    :::bash
    location /bs.sh {
        proxy_pass https://raw.githubusercontent.com/kradalby/scripts/master/bs.sh;
    }

This makes the Github script available at: https://kradalby.no/bs.sh

To use the script on a machine you will need curl or wget:

curl:

    :::bash
    curl -k https://kradalby.no/bs.sh | bash

The k option tells curl to skip the certificate, as i had some problems with this. Bash is piped at the end to run the script from stdout.

We can do the same with wget:

    :::bash
    wget --no-check-certificate https://kradalby.no/bs.sh -O - | bash
