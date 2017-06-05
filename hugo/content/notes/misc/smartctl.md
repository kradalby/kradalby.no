+++
title = "Checking S.M.A.R.T. status under Linux"
description = "Checking S.M.A.R.T. status under Debian Linux"
tags = ["smart", "Linux", "harddrive", "SSD"]
date = "2014-01-01T10:00:00"
+++

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
