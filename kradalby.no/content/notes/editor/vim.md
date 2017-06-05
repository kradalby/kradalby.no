+++
title = "Vim"
description = "Tips and tricks I use in vim"
tags = ["vim", "editor", "awesome"]
date = "2014-01-01T10:00:00"
+++

[TOC]

## Encrypt a file with Vim

*Important!*

When you open a encrypted file with vim and enter the wrong password, the file will still be open but encrypted and all the text will be gibberish! It is very important that you don't write the file. Quit it right away.

When you have opened the file issue:

    
    :set viminfo=

Then set the password you want:

    
    :set key=PASSWORD

We want to use the blowfish encryption algorithm:

    
    :setlocal cm=blowfish
