Title: VMware ESXi Notes
Tags: vmware, esxi, vmware esxi, ovftool, vm, virtual, virtual machine, machine
Date: 2015-07-18 14:53
Modified: 2015-07-18 16:52
Summary: Notes that might come in handy when working with VMware ESXi.

[TOC]

These are my notes and experiences when working with VMware ESXi. VMwares OFVtool is also featured here as it is a crucial part to moving virtual machines between ESXi hosts.

## OVFtool

### Gotchas
After a lot of receiving this error, where root is the username:

    :::
    Error: Host name (root) resolve failed

I found that the solution was to change to a alphanumeric password.

### List VMs on ESXi host

    :::
    ovftool vi://<HOST>/ 


### Moving a VM between ESXi hosts
Remember to turn of the VM before moving it.

    :::
    ovftool -ds=<NAME OF STORAGE POOL> vi://<HOST FROM>/<VM NAME> vi://<HOST TO>/


