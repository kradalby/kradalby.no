Title: Vim 
Tags: vim, editor, awesome
Summary: Tips and tricks i use in vim

[TOC]

## Encrypt a file with Vim

*Important!*

When you open a encrypted file with vim and enter the wrong password, the file will still be open but encrypted and all the text will be gibberish! It is very important that you dont write the file. Quit it right away.

When you have opened the file issue:

    :::
    :set viminfo=

Then set the password you want:

    :::
    :set key=PASSWORD

We want to use the blowfish encryption algorithm:

    :::bash
    :setlocal cm=blowfish
