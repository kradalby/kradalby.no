Title: Basic Wordpress HHVM Benchmark using ApacheBench
Category: HHVM
Tags: wordpress, hhvm, apachebench, benchmark
Summary: Basic Wordpress HHVM Benchmark using ApacheBench

I have a Wordpress site running for our brewing project, and i though it would be fun to see if a very basic benchmark would show any changes between two different ways of running PHP code.

My current setup is Nginx and PHP-FPM and i will test against Nginx and Facebooks Hip Hop VM.

Since i already got the site running with PHP-FPM i will not use any time to explain how to set it up, both setup will be using pretty much standard config, not any special tweaking.

First, install ab:

    :::bash
    apt-get install apache2-utils

## The tests

I will try to run the test with this different settings on each server:

Test 1
Concurrenty (-c): 2
Number of request (-n): 1000

Test 2
Concurrenty (-c): 5
Number of request (-n): 1000

Test 3
Concurrenty (-c): 200
Number of request (-n): 100000

Test 4
Concurrenty (-c): 500
Number of request (-n): 100000


## Installing HHVM

My server runs Debian 7 Wheezy and i will therefore show how to install HHVM on this system.

Add the repositories and install hhvm

    :::bash
    wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add -
    echo deb http://dl.hhvm.com/debian wheezy main | sudo tee /etc/apt/sources.list.d/hhvm.list
    apt-get update
    apt-get install hhvm


