+++
title = "Server To Do list"
description = "What need to be done for every new server."
tags = ["todo"]
date = "2015-06-06T23:11:00"
+++

[TOC]

## DNS
The server needs to be added to DNS, both diglett and DigitalOcean

[DigitalOcean](https://cloud.digitalocean.com/domains/fap.no)

## Backup
Setup backup of the server. Edit /backup/backup.py on metapod

The minimum is to take backup of /etc and /backup.

## Ansible
Add the server to the inventory in the plays repo.

## Portforward
If needed, forward the server.

## sshconfig
Add the new server to the sshconfig in the dotfiles repo.
