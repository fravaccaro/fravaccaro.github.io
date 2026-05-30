---
layout: post
title: "Increase Swap file size on your N9"
date: 2013-09-24 08:54:14 +0000
tags: ["guide", "increase", "MeeGo", "N9", "Nokia", "Swap"]
---
Hi everyone. It's been long time since I wrote my last post, but I'm a bit busy with some projects (among them...mhmm...how it's called...oh, yes, life), so sorry if you missed me. I decided to post about a pretty intriguing mod for the N9 I found some time ago on [EverythingN9](http://everythingn9.com/speed-mod-increase-the-swap-file-size/). Yeah, there's already a guide and a [thread on TMO](http://talk.maemo.org/showthread.php?t=86752), but I would like to write it down since with CODeRUS' _Aegis-hack_ and _OpenSudo_ some step may be changed - and, you know, I consider this miserable blog as my scrapbook, so no offense on this, I'm not afraid to give credits and I don't want to appropriate others' hard work. I will not bother you trying to explain what a Swap file is, if you are here you already know what you're looking for. So, let's start. VERSIONE ITALIANA [QUI](http://fravaccaro.wordpress.com/?p=361). 

## Disclaimer

I'll try to be as concise as possible, since anyone hardly read a disclaimer: DO IT IF YOU KNOW WHAT YOU’RE DOING. Read the whole guide before you start and if you have no clue of what you're going to do, please don't go further or don’t blame on me if something gets wrong and you have to re-flash your N9. 

## Before you start

1\. First of all, be sure you’ve already installed _Developer Mode_ on your N9, you will need _Terminal_ and the _SDK Connectivity Tool_. Then install, rather via _N9QTweak_ , the Aegis hack, which should itself install OpenSudo. Choose a password for OpenSudo (using `rootme` could be a good idea) and close N9QTweak. 2\. Open the terminal and type: `devel-su` `rootme` `passwd user` I tip you to use `rootme` once again. 3\. If it's not already installed, install _nano_ text editor by typing: `# apt-get install nano` Now you can close the terminal. 

## SSH connection

4\. Open the SDK Connectivity Tool, under WLAN you'll find your IP address. Take note of it. 5\. If you run Windows, you can use [Putty](https://www.dropbox.com/s/3b7t91ehn0f4o6m/putty.exe), it doesn't require installation. If you run Linux, just open the terminal and type: `ssh user@IPaddress` Use the password you chose on the step 2. 6\. From the SSH session, type: `devel-su` `rootme` `sudo -s` `(OpenSudo password, see step 1)` `accli -I |grep tcb-sign` This last line MUST return: `aegis-enabler::tcb-sign` If not, don't go further. 

## The crucial part

7\. Type: `cp /etc/init/enable-swap.conf /tmp/enable-swap.conf` `nano /tmp/enable-swap.conf` 8\. Nano will open. Locate this line: `if [ $ramsize -gt 1000000 ]; then` and replace the first `0` with a `1` so it becomes: `if [ $ramsize -gt 1100000 ]; then` Then locate this line: `swappart=`sed -n -e '/swap/s/mtd\([0-9]\).*/\1/p' /proc/mtd` || true` and replace `swap` with `var` so it becomes: `swappart=`sed -n -e '/var/s/mtd\([0-9]\).*/\1/p' /proc/mtd` || true` Press and hold _Ctrl + X_ and save, ensuring the new filename will overwrite the old one. 9\. Now type: `cp /tmp/enable-swap.conf /etc/init/enable-swap.conf` `export A=`sha1sum /tmp/enable-swap.conf |cut -b1-40`;` `perl -pi -w -e 's#40 (.*) A(.*)enable-swap#40 $ENV{A} A$2enable-swap#smg' /var/lib/aegis/refhashlist` `accli -c tcb-sign -F /var/lib/aegis/refhashlist -i /var/lib/aegis/refhashlist` `/usr/sbin/validator-init; aegis-loader;echo 1 > /sys/kernel/security/validator/flush` `/sbin/reboot` 10\. The phone should now reboot itself. Keep your fingers crossed! 

## Conclusions

Before applying the mod, _DropCache_ reports a Swap file size of 255mb. After, it should report 412mb. Practically, now the N9 should be able to keep more apps in background before it slow down. I hope this has been useful to you. See you soon! 

_via [[1](http://everythingn9.com/speed-mod-increase-the-swap-file-size/)], [[2](http://everythingn9.com/how-to-use-putty-on-the-nokia-n9/)]_
