Title: Server To Do list
Tags: todo
Date: 2015-06-06 23:11
Modified: 2015-06-06 23:11
Summary: What need to be done for every new server.
URL: private/server-todo-list.html
save_as: private/server-todo-list.html

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
