---
layout: post
title: "Connect Jolla to Android via SSH or SFTP"
date: 2014-09-22 20:53:20 +0000
tags: ["Android", "ConnectBot", "guide", "Jolla", "JuiceSSH", "Sailfish OS", "SFTP", "SSH", "Total Commander"]
---
I recently switched my Manjaro-powered netbook with a Nexus 7 as a "in-mobility" device and I started to dig a bit to find alternatives to those tasks I easily did with Manjaro, like connecting my Jolla via SSH or via SFTP. I used these apps on CyanogenMod 11, but I guess they will work even on other devices and different flavours of Android. Remember that you can find the IP address of your Jolla in `Settings > System > Developer mode`. 

## SSH

Here you have two options, a FOSS one and a freemium app. The first one is [ConnectBot](https://f-droid.org/repository/browse/?fdfilter=ssh&fdid=org.connectbot), available on [F-Droid](https://f-droid.org/) (the build on the Play Store in out of date - and F-Droid is a great FOSS alternative marketplace, by the way), which has pretty basic features and graphics, but it gets the job done and I have no hitches in connecting my Jolla. If you are looking for a more complex and full-featured app, go for [JuiceSSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh), available on the Play Store. 

## SFTP

The best way to browse your files on Jolla without the hassle to have an USB cable. All you need to do is download [Total Commander](https://play.google.com/store/apps/details?id=com.ghisler.android.TotalCommander) and its [SFTP plugin](https://play.google.com/store/apps/details?id=com.ghisler.tcplugins.SFTP) (not the most original name, I know) from the Play Store. Then open Total Commander and select `SFTP > <New connection...>`. Assign a name to your connection and set the IP address, username (`nemo` by default) and the password of your Jolla. After this, you will be able to browse your Sailfish OS-powered device and copy/move directories and files from the two-paned file manager. Remember to close the connection from the toolbar below when you have done. Do you use other ways/apps to connect your Jolla to your Android, iOS, Windows Phone, Blackberry device? Let me know leaving a comment below.
