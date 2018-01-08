+++
title = "Pulse Secure"
description = "Setting up Pulse Secure VPN on Ubuntu"
tags = ["pulse secure", "vpn", "ubuntu"]
date = "2018-01-08T11:34:00"
+++

## Installation

Download and install the Pulse Secure deb:

    dpkg -i ps-pulse-linux-8.2r5.0-b49363-ubuntu-debian-installer.deb

On Ubuntu 17.10, install additional dependencies:

    apt install libc6-i386 lib32z1 libwebkitgtk-1.0-0:i386 libdconf1:i386 dconf-gsettings-backend:i386 net-tools

Add the Pulse libraries to ld's search path:

    echo "/usr/local/pulse" | tee /etc/ld.so.conf.d/pulse.conf
    ldconfig


## Usage

Run the client:

    /usr/local/pulse/PulseClient.sh -h secure.company.com -u user01 -p password01 -U https://secure.company.com/linux -r "Realm Name"
