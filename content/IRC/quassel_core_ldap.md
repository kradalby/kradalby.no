Title: 
Tags: 
Date: 
Modified: 
Summary: 

[TOC]

## Header

git clone https://github.com/abustany/quassel.git
git checkout generic-ldap
apt-get install libldap2-dev
cmake /root/quassel -DWANT_CORE=ON -DWANT_QTCLIENT=OFF -DWANT_MONO=OFF -DWITH_KDE=OFF -DWITH_OXYGEN=OFF -DWITH_OPENSSL=ON -DWITH_WEBKIT=OFF -DWITH_LDAP=ON
make
make install
