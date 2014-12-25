Title: Hook to prevent dhclient to update resolv.conf
Tags: dhclient, dns, resolv, hook, prevent, 
Date: 2014-12-25 20:49
Modified: 2014-12-25 20:49
Summary: Hook to prevent dhclient to update resolv.conf

[TOC]

I ran into a issue where i had a server with two static ip interface and one dynamic. The setup required the system to have a spesific DNS setup in resolv.conf, but the dynamic interface was overriding it everytime it got a new lease.

### Create the hook
dhclient supports scripts that will run when it starts and when it exits.

We need a script that will run on enter hooks so we will create the file in this directory.

    :::
    vim /etc/dhcp3/dhclient-enter-hooks.d/nodnsupdate

Add the following code:

    :::bash
    #!/bin/sh
    make_resolv_conf(){
        :
    }

And make it executable:

    :::
    chmod +x /etc/dhcp3/dhclient-enter-hooks.d/nodnsupdate
