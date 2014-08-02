Title: Overview over my boxes and roughly what they run.
Tags: servers
Summary: Overview over my boxes and roughly what they run.
URL: private/boxes-ips-and-services.html
save_as: private/boxes-ips-and-services.html

[TOC]

## Active

### Sandefjord

#### Snorlax

    Hostname: snorlax
    Local ip: 192.168.1.250
    Remote ip: Dynamic
    Domain: tw.fap.no
    Purpose: Storage/Homeserver

    Service ports:
    SSH Local: 22
    SSH Remote: 21337
    VNC Jotta: 6000
    VNC Tupo: 6001
    HTTP: 80

    Notes:
    SSH portforward to connect to VNC or any other host on the local network.

#### kontor

    Hostname: kontor
    Local ip: 192.168.1.3
    Remote ip: Dynamic
    Domain: tw.fap.no
    Purpose: Tupperware Warehouse system

    Service ports:
    SSH Local: 22

    Notes:
    Only available on the local network.

#### kontor1

    Hostname: kontor1
    Local ip: 192.168.1.101
    Remote ip: Dynamic
    Domain: tw.fap.no
    Purpose: Office computer for employee

    Service ports:
    VNC: 5900

    Notes:
    Only available on the local network.

#### kontor2

    Hostname: kontor2
    Local ip: 192.168.1.102
    Remote ip: Dynamic
    Domain: tw.fap.no
    Purpose: Office computer for employee

    Service ports:
    VNC: 5900

    Notes:
    Only available on the local network.


### Trondheim

#### Tentacruel

    Hostname: tentacruel
    Local ip: -
    Remote ip: Dynamic
    Domain: th.fap.no
    Purpose: Router, mailinglists, kavik

    Service ports:
    SSH: 21337
    SMTP: 25
    HTTP: 80

    Notes:

#### Onyx

    Hostname: onyx
    Local ip: 129.241.210.105
    Remote ip: 129.241.210.105
    Domain: onyx.fap.no
    Purpose: Web

    Service ports:
    SSH: 21337
    HTTP: 80
    HTTPS: 443

    Notes:
    Located at NTNU in the IT building.


#### Zapdos

    Hostname: zapdos
    Local ip: 129.241.210.105
    Remote ip: 129.241.210.105
    Domain: zapdos.fap.no
    Purpose: Game

    Service ports:
    SSH: 21337

    Notes:
    Located at NTNU in the IT building.


### Miscellaneous

#### Oddish

    Hostname: oddish
    Local ip: 37.139.3.217
    Remote ip: 37.139.3.217
    Domain: fap.no
    Purpose: IRC

    Service ports:
    SSH: 22

    Notes:
    Located at DigitalOcean


## Not active
