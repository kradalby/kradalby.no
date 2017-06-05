Title: PostgreSQL usage
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: database, postgres, postgresql, sql
Summary: Basic PostgreSQL commands that i use.
+++
title = "PostgreSQL notes"
description = "Notes about PostgreSQL"
tags = ["database", "postgres", "postgresql", "sql"]
date = "2014-01-01T10:00:00"
+++

## Use

My preferred way to get access:

    su postgres -
    psql template1

    OR

    create/drop commands


**Connect to a database**

    \c databasename

## Information

**List attributes and settings for table**

    \d+ tablename

**List databases**

    \list

**List tables**

    \dt

**List users**

    \du


## Create and Drop

### Users

From shell:

    createuser username

    dropuser username

From psql:

    CREATE USER tom WITH PASSWORD 'myPassword';

### Database

From shell:

    createdb dbname

    dropdb dbname

From psql:

    CREATE DATABASE dbname;

#### Grant

Grant access for user on database with psql:

    GRANT ALL PRIVILEGES ON DATABASE dbname TO username;


We can also create a database with the user as owner:

    createdb --owner user dbname
