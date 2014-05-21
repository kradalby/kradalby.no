Title: PXE boot server
Category: Network
Tags: pxe, tftp, tftpd, boot, server
Summary: Setup instruction for a Debian netbootserver. This are the instruction for the TFTP part.

[TOC]

## Installing TFTP

This is empty for now.

## Get menu config from github
I have a ready server config with the needed pxe packages, a splash, and menus on github.

Everything can be found [here](https://github.com/dfektlan/server/tree/master/tftp)

You are free to use parts of the config, or to clone the whole repo. It also contains other relevant and irrelevant configs.

## Setting up Debian netboot (i386 & amd64)
When the basic pxe files and menu has been downloaded, we need the Debian netboot files. 

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

Now the needed files is available in the tftp folder. We now got both amd64 and i386 in debian-installer.

If the Debian version in the menu from github is not the latest, you will need to change the menu to fit the new name.

## Setting up Ubuntu live netboot (i386)
To boot live ubuntu over network we also need NFS as TFTP is very slow and a little unreliable. 
This will only explain how to setup the 32bit version of ubuntu. The procedure should be pretty much the same for the 64bit version.
I will use Ubuntu 14.04 LTS because it is the newest LTS release.

First install nfs:

    :::bash
    apt-get install nfs-kernel-server nfs-common -y
    
Download and mount Ubuntu iso:
    
    :::bash
    wget http://releases.ubuntu.com/14.04/ubuntu-14.04-desktop-i386.iso
    mkdir /media/ubuntu
    mount -o loop ubuntu-14.04-desktop-i386.iso /media/ubuntu

Create folders in the TFTP directory:

    :::bash
    mkdir -p /srv/tftp/ubuntu-live-boot/14.04/i386/

Create folders for NFS:

    :::bash
    mkdir -p /srv/nfs/ubuntu-live/i386

Copy files from the iso to the appropriate:

    :::bash
    # NFS
    cp -av /media/ubuntu/* /srv/nfs/ubuntu-live/i386
    cp -av /media/ubuntu/.disk /srv/nfs/ubuntu-live/i386

    # TFTP
    cp -av /media/ubuntu/casper/initrd.lz /srv/tftp/ubuntu-live-boot/14.04/i386/
    cp -av /media/ubuntu/casper/vmlinuz /srv/tftp/ubuntu-live-boot/14.04/i386/

Now, add the nfs dir to the exports file and reload it:

    :::bash
    echo "/srv/nfs/ubuntu-live/i386        *(ro,async,no_root_squash,no_subtree_check)" >> /etc/exports
    exportfs -a

Edit the menu.cfg file so it is correct with the server you now have running.


## Adding memory test
The memory test is included in the github repo. If there is a newer version available do this.

Download the latest precompiled binary version of [memtestpluss](http://www.memtest.org/#downiso)

    :::bash
    wget http://www.memtest.org/download/5.01/memtest86+-5.01.bin.gz
    gzip -d memtest86+-5.01.bin.gz
    ln -s memtest86+-5.01.bin memtest86+-5.01

We need to symlink or move the file to get rid of the .bin extension for some reason.

Now update the Memory test in the menu.cfg file to the new version.