Title: Dig usage
Tags: network, networking, dns, bind
Summary: Most of the dig commands i use.

[TOC]

## Usage
You can do many neat things with dig. Here is a few neat things.

### Misc

If you add +short after all commands, you will get a nice neat output that is very scriptable.

### Standard dig

    :::bash
    dig redhat.com

### Dig after record type
We can dig after different types of records. Just switch out type with A, AAAA, MX, TXT, NS, SRV.
If you use ANY all records of all types will be available.

    :::bash
    dig -t TYPE redhat.com

### Reverse DNS lookup
We can find an ip address domain name by doing a reverse lookup.

    :::bash
    dig -x 8.8.8.8

### Lookup domain using a spesific domain server
If you for example want to check how a domain is configured on a server that is not your DNS server, or it is a server that not yet in use. You can force dig to use this server.

    :::bash
    dig @8.8.8.8 redhat.com
