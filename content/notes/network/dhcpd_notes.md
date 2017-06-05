+++
title = "Notes about ISC DHCPD"
description = "These are my notes for ISC DHCPD, some tricks, and stuff"
tags = ["network", "networking", "DHCP"]
date = "2014-01-01T10:00:00"
+++

### Find vendor identifier easy

Simply put the following string into the dhcpd.conf file, the information will then show up in the lease file.

    
    set vendor-string = option vendor-class-identifier;


### DHCP Links
#### Codes
https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml

#### ISC DHCP options/man
http://linux.about.com/od/commands/l/blcmdl5_dhcpopt.htm
