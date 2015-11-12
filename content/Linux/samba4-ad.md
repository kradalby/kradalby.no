Title: Samba 4 AD on Debian
Tags: samba, active directory, samba4, 4, ad
Date: 2015-08-24 20:08
Modified: 2015-08-24 20:08
Summary: How to set up a Samba 4 Active Directory on Debian Linux

[TOC]

This is a quick guide/note on how to set up Samba 4 Active Directory on Debian Linux.

## Configuration

Edit /etc/fstab and add barrier=1 to the disk that Samba will use:

    :::
    /dev/...          /srv/samba/demo          ext4          defaults,barrier=1          1 1

Install Samba and Kerberos:

    :::
    apt-get install samba krb5-config samba-vfs-modules

Backup original configuration:

    :::
    mv /etc/samba/smb.conf /etc/samba/smb.conf.org

Provision the domain:

    :::
    samba-tool domain provision --use-rfc2307 --interactive

Example provision walkthrough:

    :::
    Realm [FAP.NO]: FAP.NO
     Domain [FAP.NO]: FAP.NO
     Server Role (dc, member, standalone) [dc]: dc
     DNS backend (SAMBA_INTERNAL, BIND9_FLATFILE, BIND9_DLZ, NONE) [SAMBA_INTERNAL]: SAMBA_INTERNAL
     DNS forwarder IP address (write 'none' to disable forwarding) [192.168.1.1]: SOME_DNS_SERVER
    Administrator password: passw0rd
    Retype password: passw0rd

Rais the domain level to 2008_R2 for more functionality:

    :::
    samba-tool domain level raise --domain-level 2008_R2 --forest-level 2008_R2 

Turn off password complexity:

    :::
    samba-tool domain passwordsettings set --complexity=off

Verify the level:

    :::
    samba-tool domain level show 


## ldapsearch

    :::
    ldapsearch \
        -x -h localhost \
        -D "read@fap.no" \
        -W \
        -b "dc=fap,dc=no" '(sAMAccountName=*)'

Filter by group:

    :::
    ldapsearch \
        -x -h localhost \
        -D "read@fap.no" \
        -W \
        -b "dc=fap,dc=no" '(&(sAMAccountName=kradalby)(CN=vpn,CN=Users,DC=fap,DC=no))'
