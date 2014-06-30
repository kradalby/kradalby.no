Title: PostgreSQL usage
Tags: database, postgres, postgresql, sql
Summary: Basic PostgreSQL commands that i use.

## Use

My prefered way to get access:

    :::bash
    su postgres -
    psql template1

    OR

    create/drop commands

## Information 

**List attributes and settings for table**

    :::bash
    \d+ tablename


## Create and Drop

### Users

From shell:

    :::bash 
    createuser username

    dropuser username

From psql:

    :::bash
    CREATE USER tom WITH PASSWORD 'myPassword';

### Database

From shell:
    
    :::bash
    createdb dbname

    dropdb dbname

From psql:

    :::bash
    CREATE DATABASE dbname;

#### Grant

Grant access for user on database with psql:

    :::bash
    GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
