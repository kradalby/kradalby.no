Title: Quassel IRC with LDAP backend
Tags: irc, quassel, ldap, internet relay chat
Date: 2015-02-13 10:53
Modified: 2015-02-13 10:53
Summary: How to build and setup the experimental LDAP support for Quassel

[TOC]

I like IRC alot, but for some people the threshold is to high to join because of the need of having a always on client. My personal client is Weechat, but the command line clients on a server idea does not fit all.

Here the IRC client Quassel has a great solution, it allows us to have the Quassel Core on the server and connect to it with a GUI client. Unfortunately the official client does not support a LDAP backend, but there is a pullrequest pending for this feauture, and heres how i built it and installed it on my IRC server.

# Work in progress

## Header

git clone https://github.com/abustany/quassel.git
git checkout generic-ldap
apt-get install libldap2-dev
cmake /root/quassel -DWANT_CORE=ON -DWANT_QTCLIENT=OFF -DWANT_MONO=OFF -DWITH_KDE=OFF -DWITH_OXYGEN=OFF -DWITH_OPENSSL=ON -DWITH_WEBKIT=OFF -DWITH_LDAP=ON
make
make install