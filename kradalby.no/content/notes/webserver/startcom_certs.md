+++
title = "Setup StartCom SSL/TLS certs correctly"
description = "Notes to remember when creating a new certificate from StartCom"
tags = ["SSL", "tls", "certs", "startcom", "startssl", "nginx"]
date = "2014-01-01T10:00:00"
+++

[TOC]

## Decrypt the key
The password is the one you used to create the key.

    
    openssl rsa -in ssl.key -out ssl.key

Protect the key from everyone:

    
    chmod 600 ssl.key

Create certificate from key:

    
    TODO

Fetch the Root CA and Class 1 Intermediate Server CA certificates:

    
    wget http://www.startssl.com/certs/ca.pem
    wget http://www.startssl.com/certs/sub.class1.server.ca.pem

Concatinate the three certificates:

    
    cat ssl.pem sub.class1.server.ca.pem ca.pem > ssl-unified.pem

## Tell Nginx to use the Certificate
Add these lines to the vhost file for the correct domain:

    
    ssl                  on;
    ssl_certificate      /etc/certs/ssl.pem;
    ssl_certificate_key  /etc/certs/ssl.key;

    ssl_session_timeout  5m;

    ssl_protocols  SSLv2 SSLv3 TLSv1;
    ssl_ciphers  HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers   on;
    add_header Strict-Transport-Security max-age=15768000;
