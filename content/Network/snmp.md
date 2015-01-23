Title: Useful SNMP notes
Tags: snmp, snmpd, oid, oids, mib, mibs, linux, set, get
Date: 2015-01-14 17:35
Modified: 2015-01-14 17:35
Summary: Useful collection of SNMP information i have used, and use frequently.

[TOC]

## Useful OIDs

### Interface related

*Interface description*

OID value: 1.3.6.1.2.1.2.2.1.2

*Interface octet in*

64 bit counter for total number of received octets/bytes.

OID value: 1.3.6.1.2.1.31.1.1.1.6

*Interface octet out*

64 bit counter for total number of transmitted octets/bytes.

OID value: 1.3.6.1.2.1.31.1.1.1.10


## Turn of SNMPd cache
To turn off SNMPd cache on the Debian linux package you have to, as far as i know, do this with SNMP.

First, check your current cache time:

    :::
    $ snmpwalk -v2c -c public 10.0.0.1 1.3.6.1.4.1.8072.1.5.3.1.2.1.3.6.1.2.1.2.2
    NET-SNMP-AGENT-MIB::nsCacheTimeout.1.3.6.1.2.1.2.2 = INTEGER: 15

The integer represents seconds.

To change it, from a rwcommunity issue:

    :::
    $ snmpset -v2c -c public 10.0.0.1 1.3.6.1.4.1.8072.1.5.3.1.2.1.3.6.1.2.1.2.2 i 0
    NET-SNMP-AGENT-MIB::nsCacheTimeout.1.3.6.1.2.1.2.2 = INTEGER: 0
