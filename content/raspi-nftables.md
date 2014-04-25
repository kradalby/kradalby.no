Title: Testing nftables with Raspberry Pi and Arch
Category: Raspberry Pi
Tags: raspberry pi, nftables, arch linux
Summary: Testing the new linux packet filter, nftables on a Raspberry Pi and Arch.

[Work in progress]

Yesterday i learned that iptables will be replaced by the successor nftables. Nftables was merged into the linux kernel on 19. January 2014 and was released with the 3.13 kernel.

nftables will make it possible to write rules more efficient and reduce code duplication. The userpace utility nft will replace iptables, ip6tables, arptables and ebtables.

In this setup i will use a Raspberry Pi with the Arch Linux ARM 2014.04 build. However i would recommend to always get the latest version if setting up a new Pi. You can find this [Here](http://archlinuxarm.org/platforms/armv6/raspberry-pi)


## Compiling the newest kernel
When i was writing this guide, the latest available precompiled kernel for RPI was 3.10, which means i had to compile a newer kernel myself. I found that the 3.14 kernel had a branch on the RPI github so i decided to try that one.

At this point i decided to compile the kernel on the Raspberry Pi, this gave me some problems when i was trying to recieve the code. I tried to fetch it directly from the correct branch from git, but i got an out of memory error. I also tried to take it down through wget, curl and lynx, but all of them presentet me with the same type of error. In the end i used rsync via ssh to move the downloaded files from my mac to the RPI. I used rsync because the scp process also ran out of memory.

When i finally got the code to my RPI i needed to update the current Arch installation and install the build utilities:
    
    :::bash
    pacman -Syu
    pacman -S bc gcc make

After this was done, i needed to actually compile the kernel. This starts with making sure the build directory is clean:

    :::bash
    make mrproper

Then i needed to get a standard config for the RPI kernel, the default config is located at "arch/arm/configs/bcmrpi_defconfig" in the source code directory.

    :::bash
    cp arch/arm/configs/bcmrpi_defconfig .config

Now that we have a standard config, we can start the requierd configuration for our needs:
    
    :::bash
    make menuconfig

CONFIG

When you are finished configuring, you will start the actuall compiling:

    :::bash
    make
    make modules

removed btrfs and a lot of other unneeded filesystems since they are not needed and produced compile errors.


