+++
title = "Use Sendmail as a satellite system"
description = "<p>Quick note on how to use Sendmail as a satellite mail system.</p>"
tags = ["mail", "SMTP", "satellite", "sendmail"]
date = "2014-01-01T10:00:00"
+++
Title: Use Sendmail as a satellite system
Date: 2014-01-01 10:00
Modified: 2014-01-01 10:00
Tags: mail, SMTP, satellite, sendmail
Summary: Quick note on how to use Sendmail as a satellite mail system.

First, the only time I have actually used sendmail is on our very outdated work server, which comes with Sendmail as standard and do not have a package manager.

This guide has been created by configuring a Red Hat Enterprise Linux ES release 4 (Nahant).

To configure Sendmail, we need to locate sendmail.cf, the main configuration file.

In this particular install, it is located at /etc/mail/sendmail.cf

Open it in your favorite editor, which is vim and search for DS.

Edit so it looks something like this:

    :::bash
    # "Smart" relay host (may be null)
    DSsmtp.company.com
