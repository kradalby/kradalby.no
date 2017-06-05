Title: HP ACU cli utility 
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: hp, acu, p410i, raid, cli, linux
Summary: Little collection of some HP ACU commands i might use.

[TOC]

## Usage

Display controller and disk status:

    :::
    ctrl all show config

View Controller status:

    :::
    ctrl all show status

View Drive Status

    ::: 
    ctrl slot=0 pd all show status

View Individual Drive Status

    :::
    ctrl slot=0 pd 2I:1:6 show detail

View All Logical Drives

    :::
    ctrl slot=0 ld all show

View Detailed Logical Drive Status

    :::
    ctrl slot=0 ld 2 show

Blink Physical Disk LED

    ::: 
    ctrl slot=0 ld 2 modify led=on

Add raid controller license:

    :::
    ctrl slot=0 add licensekey=XXXXX-XXXXX...
