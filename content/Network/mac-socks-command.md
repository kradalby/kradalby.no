Title: Mac OS X socks proxy
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: socks, proxy, mac
Summary: Turn on and off Mac OS X Socks proxy with command line

[TOC]

Set the Mac OS X settings from command line:

Set proxy settings for a device:

    :::
    networksetup -setsocksfirewallproxy "Ethernet" localhost 9999

To clear settings for a device:

    :::
    networksetup -setsocksfirewallproxy "Ethernet" "" ""

To turn the proxy on or off:

    :::
    networksetup -setsocksfirewallproxystate "Ethernet" off/oo
