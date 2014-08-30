Title: Handy commands for nmap
Tags: network, networking, nmap, portscan, ipscan
Summary: A collection of commands that are useful for network stuff with nmap.

[TOC]

## Scan ip range
Find host that is alive within a ip range.

    :::bash
    nmap -sP 192.168.0.0/24

## Scan port range
Find ports on host.

    :::bash
    nmap 192.168.1.1 -p100-200

## Scan for OS
Try to find out what OS a host is running.

    :::bash
    nmap -O 192.168.1.1

## Scan for udp servies
This needs root privileges.

    :::bash
    nmap 192.168.1.1 -sU
