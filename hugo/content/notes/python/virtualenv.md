+++
title = "Setting up virtualenv for Python"
description = "How to set up a virtualenv for python development and production."
tags = ["python", "python3", "virtualenv"]
date = "2014-01-01T10:00:00"
+++

[TOC]

## Install virtualenv on Debian Wheezy

Install via pip:

    :::bash
    pip install virtualenvwrapper

Add global variables to your shell startup file:

    :::
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

Remember to reload your shell.


## Creating a virtualenv
Here is a collection of creating commands that I have needed.

### Standard create

    :::bash
    mkvirtualenv name

### Python3 create

    :::bash
    mkvirtualenv -p /usr/bin/python3 name

### Custom path

    :::bash
    mkvirtualenv /path/to/env

Note: This will create the env where you want it, but you will not be able to use workon and lsvirtualenv to find it.
