+++
title = "Checking S.M.A.R.T. status under Linux"
description = "Checking S.M.A.R.T. status under Debian Linux"
tags = ["smart", "Linux", "harddrive", "SSD"]
date = "2014-01-01T10:00:00"
+++




## Install

    apt-get install smartmontools

## Checking status

Check status of the drive:

    
    smartctl -H /dev/sda

Check out information about the drive:

    
    smartctl -i /dev/sda

Check out everything:

    
    smartctl -a /dev/sda


## Testing

Run long/full test of the drive:

    
    smartctl --test=long /dev/sda

Run short/quick test of the drive:

    
    smartctl --test=short /dev/sda
