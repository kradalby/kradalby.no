+++
title = "Install VMware tools on Debian"
description = "How to install VMware tools on a Debian guest."
tags = ["VMware", "tools", "Linux", "Debian"]
date = "2014-01-01T10:00:00"
+++

[TOC]

## Install

First use the "Guest - Install/Upgrade VMware Tools" to get the install iso mounted on the guest.

Secondly log in as root on the guest.

Mount the CD room:

    :::
    mount /dev/cdromm /mnt

Unarchive the files: (remember to stay in your home folder so the files end up there)

    tar xzf /mnt/VMwareTools*

Unmount the drive:

    :::
    umount /mnt

Install the needed packages to build VMware tools:

    :::
    apt-get update
    apt-get install gcc make linux-headers-$(uname -r)

Execute the install script:

    :::
    cd vmware-tools-distrib
    ./vmware-install.pl

Go through the install process, when it finishes remove the directory with the install files and reboot the server.
