Title: Compile latest Linux kernel for Debian
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: Linux, kernel, Debian, latest
Summary: a Quick collection of commands on how to compile the latest Linux kernel for Debian.

## Install needed packages

    :::bash
    apt-get install fakeroot kernel-package libncurses5-dev

## Download latest Kernel source
As of this writing, the latest source is 3.15.1

    :::bash
    wget https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.15.1.tar.xz
    tar xvJf linux-3.15.1.tar.xz

## Start configuring

    :::bash
    cd linux-3.15.1

Get current config

    :::bash
    cp /boot/config-`uname –r` .config

Start menuconfig and change the stuff you want to:

    :::bash
    make menuconfig

Clean:

    :::bash
    make-kpkg clean

## Building
Export the wanted concurrency (number of cores + 1) and build a Debian package of the kernel.

    :::bash
    export CONCURRENCY_LEVEL=5
    fakeroot make-kpkg --append-to-version "-customkernel" --revision "1" --initrd kernel_image kernel_headers

When this command is complete, we will have two dpkg files, one for the kernel and one for headers. The great thing about this is that we can just install them and it will fix grub for us.

    :::bash
    dpkg -i linux-headers-3.15.1-customkernel_1_amd64.deb linux-image-3.15.1-customkernel_1_amd64.deb

## Remove a custom kernel
To remove a kernel that we are not using, or that does not work just uninstall it.

    :::bash
    apt-get remove linux-image-3.15.1-customkernel linux-headers-3.15.1-customkernel
