+++
title = "Hook to prevent dhclient to update resolv.conf"
description = "Hook to prevent dhclient to update resolv.conf"
tags = ["dhclient", "DNS", "resolv", "hook", "prevent"]
date = "2014-12-25T20:49:00"
+++

[TOC]

I ran into an issue where I had a server with two static IP interface and one dynamic. The setup required the system to have a specific DNS setup in resolv.conf, but the dynamic interface was overriding it every time it got a new lease.

### Create the hook
dhclient supports scripts that will run when it starts and when it exits.

We need a script that will run on entering hooks so we will create the file in this directory.

    
    vim /etc/dhcp3/dhclient-enter-hooks.d/nodnsupdate

Add the following code:

    
    #!/bin/sh
    make_resolv_conf(){
        :
    }

And make it executable:

    
    chmod +x /etc/dhcp3/dhclient-enter-hooks.d/nodnsupdate
