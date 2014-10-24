Title: Mac OS X socks proxy
Tags: socks, proxy, mac
Summary: Turn on and off Mac OS X Socks proxy with commandline

[TOC]

Set the Mac OS X settings from commandline:

Set proxy settings for a device:
    
    :::
    networksetup -setsocksfirewallproxy "Ethernet" localhost 9999

To clear settings for a device:
    
    :::
    networksetup -setsocksfirewallproxy "Ethernet" "" ""

To turn the proxy on or off:

    :::
    networksetup -setsocksfirewallproxystate "Ethernet" off/on

    
