Title: PXE boot server
Category: Network
Tags: pxe, tftp, tftpd, boot, server
Summary: Setup instruction for a Debian netbootserver. This are the instruction for the TFTP part.

[TOC]

## Installing TFTP

This is empty for now.

## Setting up Debian netboot (i386 & amd64)
The easiest way to get the needed pxe files is to get them through the debian netboot package we are going to download anyway.

To do this wget the latest package, as of now, this is wheezy:

    :::bash
    cd /srv/tftp

    # Download for i386
    wget ftp://ftp.no.debian.org/debian/dists/wheezy/main/installer-i386/current/images/netboot/netboot.tar.gz
    tar -zxvf netboot.tar.gz
    rm netboot.tar.gz

    # Download for amd64
    wget ftp://ftp.no.debian.org/debian/dists/wheezy/main/installer-amd64/current/images/netboot/netboot.tar.gz
    tar -zxvf netboot.tar.gz
    rm netboot.tar.gz

Now the needed files is available in the tftp folder. We got both amd64 and i386 in debian-installer and the needed pxelinux files.

The next thing we need to do is customizing the menu so we get both options. I will not go through this here, as i already have a menu ready for my use.

My menu is available [here](https://github.com/dfektlan/server/blob/master/tftp/menu.cfg)
This is based on the Debian menu, and it needs the packages over to work. It also includes the Ubuntu live part that we will look into later.

To use the menu, edit pxelinux.cfg/default and make it look like this:

    :::bash
    include menu.cfg
    defaul debian-installer/i386/boot-screens/vesamenu.c32
    prompt 0
    timeout 30


## Setting up Ubuntu live netboot (i386)


## Adding memory test
