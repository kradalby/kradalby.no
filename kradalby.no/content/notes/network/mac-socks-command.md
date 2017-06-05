+++
title = "Mac OS X socks proxy"
description = "Turn on and off Mac OS X Socks proxy with command line"
tags = ["socks", "proxy", "mac"]
date = "2014-01-01T10:00:00"
+++



Set the Mac OS X settings from command line:

Set proxy settings for a device:

    
    networksetup -setsocksfirewallproxy "Ethernet" localhost 9999

To clear settings for a device:

    
    networksetup -setsocksfirewallproxy "Ethernet" "" ""

To turn the proxy on or off:

    
    networksetup -setsocksfirewallproxystate "Ethernet" off/oo
