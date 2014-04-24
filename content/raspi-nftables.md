Title: Testing nftables with Raspberry Pi and Arch
Category: Raspberry Pi
Tags: raspberry pi, nftables, arch linux
Summary: Testing the new linux packet filter, nftables on a Raspberry Pi and Arch.

[Work in progress]

Yesterday i learned that iptables will be replaced by the successor nftables. Nftables was merged into the linux kernel on 19. January 2014 and was released with the 3.13 kernel.

nftables will make it possible to write rules more efficient and reduce code duplication. The userpace utility nft will replace iptables, ip6tables, arptables and ebtables.

In this setup i will use a Raspberry Pi with the Arch Linux ARM 2014.04 build. However i would recommend to always get the latest version if setting up a new Pi. You can find this (Here)[http://archlinuxarm.org/platforms/armv6/raspberry-pi]

