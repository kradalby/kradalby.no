Title: Libvirt with KVM/QEMU on Debian Linux
Tags: KVM, VM, Virtualization, virtual, virtual machine, debian, linux, windows, qemu, libvirt, virsh
Date: 2015-12-18 07:29
Modified: 2015-12-20 13:33
Summary: KVM/QEMU on Debian Linux

[TOC]

KVM requires that the processor has virtualization support, named VT-x for Intel, and AMD-V for AMD.

Check by issuing lscpu:

    :::
    $ lscpu
    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                4
    On-line CPU(s) list:   0-3
    Thread(s) per core:    1
    Core(s) per socket:    4
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 15
    Model name:            Intel(R) Core(TM)2 Quad CPU    Q6600  @ 2.40GHz
    Stepping:              11
    CPU MHz:               3604.054
    BogoMIPS:              7208.10
    Virtualization:        ___VT-x___
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              4096K
    NUMA node0 CPU(s):     0-3

Install libvirt, QEMU, and KVM:

    :::
    apt-get install qemu-kvm libvirt-bin virtinst


Create a Windows 10 VM with virt-install:

:::
virt-install --name win10 --memory 1024 --cdrom /storage/software/Microsoft/windows/SW_DVD5_WIN_ENT_10_64BIT_English_MLF_X20-26061.ISO --disk /var/lib/libvirt/images/win10.qcow2,size=30 --network=bridge:bridge-lan --graphics vnc,listen=0.0.0.0,password=test

Get the VNC port:

:::
virsh vncdisplay <VM>

Edit the configuration of a VM:

:::
virsh edit <VM>

Start:

:::
virsh start <VM>

Stop/shutdown:

:::
virsh shutdown <VM>

Restart/reboot:

:::
virsh reboot <VM>

Set the VM to autostart:

:::
virsh autostart win10


## Configure for bridge

Install bridge-utils:


Configure bridge in /etc/network/interfaces:

:::
apt-get install bridge-utils

:::
auto eth0
iface eth0 inet manual

auto bridge-lan
iface bridge-lan inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
    bridge_ports    eth0
    bridge_stp      off
    bridge_fd       0
    bridge_maxwait  0
