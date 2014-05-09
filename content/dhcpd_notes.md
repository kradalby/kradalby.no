Title: Notes about ISC DHCPD
Category: DHCP
Tags: network, networking, dhcp
Summary: These are my notes for ISC DHCPD, some tricks and stuff

### Find vendor identifier easy

Simply put the following string into the dhcpd.conf file, the information will then show up in the lease file.

    :::bash
    set vendor-string = option vendor-class-identifier;




