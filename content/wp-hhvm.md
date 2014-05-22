Title: Wordpress HHVM Benchmark
Category: HHVM
Tags: wordpress, hhvm, apachebench, benchmark
Summary: Basic Wordpress HHVM Benchmark using ApacheBench

[TOC]


I have a Wordpress site running for our brewing project, and i though it would be fun to see if a very basic benchmark would show any changes between two different ways of running PHP code.

My current setup is Nginx and PHP-FPM and i will test against Nginx and Facebooks Hip Hop VM.

Since i already got the site running with PHP-FPM i will not use any time to explain how to set it up, both setup will be using pretty much standard config, not any special tweaking.

First, install ab:

    :::bash
    apt-get install apache2-utils

## The tests

The tests will be run from the same machine as the Nginx is hosted on.

The specifications for the server is:

    :::
    Intel i7 2600 3.4 ghz
    16gb RAM
    Intel 330 120gb SSD

I will try to run the test with this different settings on each PHP backend:

Test 1
Concurrenty (-c): 2
Number of request (-n): 1000

Test 2
Concurrenty (-c): 5
Number of request (-n): 1000

Test 3
Concurrenty (-c): 200
Number of request (-n): 100000

## Installing HHVM

My server runs Debian 7 Wheezy and i will therefore show how to install HHVM on this system.

Add the repositories and install hhvm

    :::bash
    wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add -
    echo deb http://dl.hhvm.com/debian wheezy main | sudo tee /etc/apt/sources.list.d/hhvm.list
    apt-get update
    apt-get install hhvm

And since HHVM gives us a nice install script which takes care of Nginx we just issue:

    :::bash
    /usr/share/hhvm/install_fastcgi.sh

## Running the tests

I actually got some interesting unexpected numbers. I guess that most of them can be changed with some tweaking.

### Test 1
PHP-FPM:
    
    :::bash
    Time taken for tests:   56.205 seconds
    Requests per second:    17.79 [#/sec] (mean)
    Time per request:       112.410 [ms] (mean)
    Time per request:       56.205 [ms] (mean, across all concurrent requests)
    Transfer rate:          401.71 [Kbytes/sec] received

HHVM:
    
    :::bash
    Time taken for tests:   11.450 seconds
    Requests per second:    87.34 [#/sec] (mean)
    Time per request:       22.900 [ms] (mean)
    Time per request:       11.450 [ms] (mean, across all concurrent requests)
    Transfer rate:          1971.13 [Kbytes/sec] received

### Test 2
PHP-FPM:
    
    :::bash
    Time taken for tests:   30.708 seconds
    Requests per second:    32.56 [#/sec] (mean)
    Time per request:       153.540 [ms] (mean)
    Time per request:       30.708 [ms] (mean, across all concurrent requests)
    Transfer rate:          735.25 [Kbytes/sec] received

HHVM:
    
    :::bash
    Time taken for tests:   5.225 seconds
    Requests per second:    191.38 [#/sec] (mean)
    Time per request:       26.125 [ms] (mean)
    Time per request:       5.225 [ms] (mean, across all concurrent requests)
    Transfer rate:          4319.43 [Kbytes/sec] received

### Test 3
PHP-FPM:
    
    :::bash
    Time taken for tests:   168.360 seconds
    Requests per second:    593.97 [#/sec] (mean)
    Time per request:       336.719 [ms] (mean)
    Time per request:       1.684 [ms] (mean, across all concurrent requests)
    Transfer rate:          960.51 [Kbytes/sec] received

HHVM:
    
    :::bash
    Time taken for tests:   383.876 seconds
    Requests per second:    260.50 [#/sec] (mean)
    Time per request:       767.751 [ms] (mean)
    Time per request:       3.839 [ms] (mean, across all concurrent requests)
    Transfer rate:          5879.34 [Kbytes/sec] received

Note: When running the third test, i observed very high load during the HHVM test.

## Conclusion

I was a little supprised how much HHVM outperformed PHP-FPM at the lower concurrencies, and i was very suprised that PHP-FPM actually won the high concurrency test. I guess that this can be turned around with a little tweaking. Both installs are without anything but stock install, both can proably do better.

I will also let the test site run HHVM from now on, i will not, at first, tweak anything, as i dont get any amount of hits that will need this.

An other interesting observation from my side is that the site actually feels snappier. This may only be in my head.


