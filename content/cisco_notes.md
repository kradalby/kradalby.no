Title: Notes about configuring Cisco equipment
Category: Cisco
Tags: network, networking, cisco, switch
Summary: My notes for configuring cisco switches and routers, at some point, this will have both basic and advance stuff.

[TOC]

## Setting ip on Vlan1 for basic management

This is the basic steps for setting a static ip to a cisco switch and giving it a default gateway.
This will configure the standard Vlan1, which may not be a good idea in most setups.
    
    :::C
    Switch> enable
    Switch# conf t
    Switch(config)# int vlan1
    
    # You can also use ip address dhcp.
    Switch(config-if)# ip address 192.168.1.10 255.255.255.0
    
    # Remember to activate the interface
    Switch(config-if)# no shutdown
    Switch(config-if)# end
    Switch(config)# end


## Backup or Restore via TFTP

To backup:

    :::C
    Switch# copy running-config tftp://ip/filename

To restore:

    :::C
    Switch# copy tftp://ip/filename running-config


## Write and erase config

To save:
    
    :::C
    Switch# copy runn start
    or
    Switch# write mem
    Switch# reload

To erase

    :::C
    Switch# write erase
    Switch# reload

## DHCP autoconfiguration

Most Cisco switches, to my knowledge, can be autoconfigured with a combination of dhcp and tftp. This is a great feature.
My main use of these switches are table switches at lan parties.
With some proper configuration we can configure the dhcp, core switch and tftp server so that every table switch can fetch its correct configuration on boot. It will also give great flexibility when it comes to switches that break during the event or something else. There will actually be possible to just put in a drop-in replacement, and it will automaticly be configured correctly.

### Notes from testing C2950-24
I have been testing when the C2950 fetches a configuration and when it is not. 

It will allways fetch the configuration when it has no configuration (duhh).
It will not save the configuration. Which is great for us, since we want it to always fetch the latest.
It will not fetch a configuration once the switch has a startup config.
