Title: Checking S.M.A.R.T. status under Linux
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: smart, Linux, harddrive, SSD
Summary: Checking S.M.A.R.T. status under Debian Linux

[TOC]


## Install

    apt-get install smartmontools

## Checking status

Check status of the drive:

    :::bash
    smartctl -H /dev/sda

Check out information about the drive:

    :::bash
    smartctl -i /dev/sda

Check out everything:

    :::bash
    smartctl -a /dev/sda


## Testing

Run long/full test of the drive:

    :::bash
    smartctl --test=long /dev/sda

Run short/quick test of the drive:

    :::bash
    smartctl --test=short /dev/sda
