+++
title = "Setup Vmware player headless on Debian"
description = "Guide on how to install and use Vmware player on a Debian server without X server."
tags = ["VM", "VMware", "Debian", "headless", "virtualization"]
date = "2014-01-01T10:00:00"
+++


## Download
Vmware player cannot be downloaded directly, so you will need to navigate to the following URLs.

Download Player:

https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0|PLAYER-602|product_downloads

Download VIX:
https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0|PLAYER-602|drivers_tools

VIX is the command line tools we need to stop and start the VMs.

## Install
To install just execute the downloaded files:

    
    sh VMware.bundle --eulas-agreed
    sh VMware-vix.bundle --eulas-agreed

### Packages
We need some packages for VMware Player to run:

    
    apt-get install libxt6 libxtst6 libxcursor-dev libxinerama-dev build-essential


### Build modules
If your Linux computer uses a kernel older than 3.13 you can just build the needed modules.

    
    vmware-modconfig --console --install-all

If you are on a later kernel, look at the patch section.

### Add user
As i will run my VMs on a server, i want a spesific user for running them:

    
    useradd -b /home/vmware -d /home/vmware -m -s /bin/bash vmware
    passwd vmware

## Configuration

### Activate VNC
To activate VNC add/edit the following:

    
    RemoteDisplay.vnc.enabled = "TRUE"
    RemoteDisplay.vnc.port = "5950"
    RemoteDisplay.vnc.password = "your_password"

For the password, you can use a hash, but I do not know what kind it is.


## Usage

Start:

    
    vmrun -T player start /path/to/vm/my.vmx nogui

Reboot:

    
    vmrun -T player reset /path/to/vm/my.vmx soft

Stop:

    
    vmrun -T player stop /path/to/vm/my.vmx soft

Clone:
Clone is actually not supported by VMware Player.

    


## Patch
If you are using 3.15 kernel (as I am) follow this URL to patch the module source.
http://oldpapyrus.wordpress.com/2014/05/28/vmware-player-6-0-2-ubuntu-14-04-kernel-3-15-0-rc7/


## Resources
Arch Wiki

https://wiki.archlinux.org/index.php/VMware
