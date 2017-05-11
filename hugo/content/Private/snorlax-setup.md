+++
title = "Setup documentation for Snorlax"
description = "<p>Documentation covering the setup of Snorlax.</p>"
tags = ["backup"]
date = "2014-01-01T10:00:00"
+++
Title: Setup documentation for Snorlax
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: backup
Summary: Documentation covering the setup of Snorlax.
URL: private/snorlax-setup.html
save_as: private/snorlax-setup.html

[TOC]

## Hard drives

### Overview

#### SATA2

    Brand: Kingston
    Type: SSD
    Size: 120gb
    Filesystem: EXT4
    Mountpoint: /

#### SATA3

    Brand: Western Digital VelociRaptor
    Type: HDD
    Size: 160gb
    Filesystem: EXT4
    Mountpoint: /media/160g

#### SATA5

    Brand: Seagate Barracuda
    Type: HDD
    Size: 4tb
    Filesystem: btrfs
    Raid: Storage

#### SATA6

    Brand: Seagate Barracuda
    Type: HDD
    Size: 4tb
    Filesystem: btrfs
    Raid: Storage

### Raids

#### Storage

    Disks: SATA5, SATA6
    Size: 4tb
    Type: RAID1
    Mountpoint: /storage


## Backup user

### Creating the user

    :::bash
    useradd -b /storage/backup -d /storage/backup -M -s /bin/bash meepo
    chown -R meepo.meepo /storage/backup

I do not set a password since I am only going to use keys for this account.


## Jottacloud


## Samba
Example samba config files are available on GitHub.
