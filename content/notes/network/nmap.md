+++
title = "Handy commands for nmap"
description = "A collection of commands that are useful for network stuff with nmap."
tags = ["network", "networking", "nmap", "portscan", "ipscan"]
date = "2014-01-01T10:00:00"
+++



## Scan IP range
Find the hosts that are alive within an IP range.

    
    nmap -sP 192.168.0.0/24

## Scan port range
Find ports on a host.

    
    nmap 192.168.1.1 -p100-200

## Scan for OS
Try to find out what OS a host is running.

    
    nmap -O 192.168.1.1

## Scan for udp services
This needs root privileges.

    
    nmap 192.168.1.1 -sU
