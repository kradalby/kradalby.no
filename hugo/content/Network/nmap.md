+++
title = "Handy commands for nmap"
description = "<p>A collection of commands that are useful for network stuff with nmap.</p>"
tags = ["network", "networking", "nmap", "portscan", "ipscan"]
date = "2014-01-01T10:00:00"
+++
Title: Handy commands for nmap
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: network, networking, nmap, portscan, ipscan
Summary: A collection of commands that are useful for network stuff with nmap.

[TOC]

## Scan IP range
Find the hosts that are alive within an IP range.

    :::bash
    nmap -sP 192.168.0.0/24

## Scan port range
Find ports on a host.

    :::bash
    nmap 192.168.1.1 -p100-200

## Scan for OS
Try to find out what OS a host is running.

    :::bash
    nmap -O 192.168.1.1

## Scan for udp services
This needs root privileges.

    :::bash
    nmap 192.168.1.1 -sU
