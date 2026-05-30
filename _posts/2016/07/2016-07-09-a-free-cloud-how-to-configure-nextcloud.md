---
layout: post
title: "A free cloud - how to configure Nextcloud"
date: 2016-07-09 17:36:29 +0000
tags: ["CertBot", "DietPi", "guide", "installation", "LAMP", "Letsencrypt", "Linux", "Nextcloud", "OwnCloud", "Raspberry Pi"]
---
As some of you may know, I’m a quite open source-oriented guy. I run different flavors of GNU/Linux on my machines (currently the amazing Arch-based Antergos), I used to be an avid N9 (MeeGo) user and a current Jolla (Sailfish OS) one. I’m not that kind of man who bashes everything is closed-sourced though; I look at different solutions and choose the best one. And a lot of times the best one is open source. Why am I writing this preface? Because open source fans are usually pictured as blatant long-bearded programmers or (pseudo-)philosophers with Steve Ballmer's face printed on their toilet paper. And although the Ballmer-paper is a brilliant idea, I’m not a programmer, nor a philosopher and I hope blatant neither. And my beard grows in patches. I’m just a guy willing to learn new stuff and who’s becoming more conscious where his data go. All the major platforms (both mobile and desktop) work great, but are they worth my privacy and my personal information as a price to pay? In one word, _nope_. This is one of the reasons I am approaching more to open solutions instead of closed ones and why I am writing this post – post conceived to show that even a not so IT-skilled guy as me can set up a small personal cloud to store his data. But, all in all, what exactly is the so-called _cloud_? 

## The cloud

In a nutshell, the _cloud computing_ lets you archive your contacts, calendars, files, pictures and so on on a company server to reach them no matter what device you are using. Easy, isn’t it? But here it comes the first caveat. Yes, because all your data are literally on someone else computer and under the law of the countries where those servers are located in and this is a matter – as the _NSA affair_ showed – to not be understated. People may say “ _Oh if you have nothing to hide you should not be afraid_ ”. **Bullshit**. Since you have nothing to hide, would it be okay for you if policemen came from time to time at your place to rummage into your things? It would bother me. So why should I be okay to let a foreign (but neither my home one would be fine) government rummage into my data? Even if data were not at the mercy of foreign governments still, accepting the _End User License Agreement_ (EULA), we grant to those companies the right to do whatever they like with our information. Have you noticed that if you book a flight and you receive the ticket into your Gmail, the relative event is added to Google Calendar within minutes? This is because Google analyzes the content of your emails (but also your files, photos, etc.) to give you a - yes - convenient service, but also to enrich the profile of you they have and yield it to their trading partners. Sure, it’s handy and straightforward, but am I the only one to find it a little bit _creepy_? 

### Is an alternative solution possible?

Short answer: _Yes it is_. All we need is a low-powered board (as it’s going to be on all the time). Check. A way to manage and route data from the server to our devices. Check. We are going to use that mighty little board called **Raspberry Pi** and an open source application called **Nextcloud** , which lets you set up your own cloud at home and access to it remotely as it was one of the solutions offered by Google, Microsoft or Apple. Oh, also some time, patience and basic Linux knowledge would not hurt. 

## Why the Pi?

Why is the Raspberry Pi a perfect choice for this project? Because it’s a fairly cheap piece of hardware with endless community support, guides and posts written about it. It’s not the most powerful hardware out there (although it’s improved with latter generations), but this small-sized server we are going to make is intended for personal use, so I suppose we can live with no top-notch performance. 

## Why Nextcloud?

Albeit the name may sound new to you, it's a software which has solid roots into ownCloud, an open source and mature cloud solution aimed to both private and enterprise users. Recently one of its co-founders, Frank Karlitschek, left ownCloud and forked it into this new project, stating some mistakes where quite hard to solve without a reboot. I'm not going to discuss his claims here, I chose to use Nextcloud because: 

  1. It more likely will be the project which inherits and carries on the ownCloud legacy, as almost all the core developers switched to Nextcloud.
  2. Few guides are available on the net and they usually treat it as an ownCloud update to be done, whereas in my guide I'm going to describe an installation from the scratch.

So, without further ado, let's dive into it. 

## Index

  1. What we need
  2. Install the OS and first configuration
  3. Configure the DNS
  4. Create and install the cert
  5. Configure the router
  6. Configure Nextcloud

## What we need

  * A Raspberry Pi.
  * An SD card (or microSD, depending on your Raspberry model), minimum 16 GB and class 10 recommended.
  * A router with port mapping capabilities (check on your router user manual).
  * Of course, a monitor and a keyboard for the first configuration.

## Install the OS and first configuration

We are going to use a bare-bone Raspbian-derived distribution called DietPi. Its strengths are the ease of use and configuration and the sleekness; it’s particularly suitable as a server distro as it offers no graphical interface nor any blob at all by default. 

  1. Download the image from [here](http://dietpi.com/) and unzip it.
  2. Insert the SD card into your PC.
  3. (On Windows) Use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) to burn the image onto the SD or (on Linux) open a terminal and type: # dd if=FILEPATH/FILE.img of=/dev/sdX Where X is the letter associated with the SD. _Note: you should use sdX, not sdX1, sdX2, etc._

* * *

### (Optional) Configure the Wifi

  * Open the file `dietpi.txt` on the SD.
  * Set `Wifi_Enabled=1`
  * Set your network's SSID in `Wifi_SSID=SSIDWifi` and password in `Wifi_KEY=PasswordWifi`

* * *

  4. Insert the SD into the Pi, connect the display and the keyboard and power it on; the DietPi wizard will lead you step-by-step throughout the installation process.
  5. In `Software Optimized` select `Nextcloud` and `CertBot`.
  6. Go back and select `Apache2` under `Webserver Preference`.
  7. Select `DietPi-Config > Network Options: Adapters`, then `Ethernet` or `WiFi` (depending from your connection).
  8. In `Change Mode` select `STATIC` and in `IP address` type the IP address of your choice for your Pi, e.g. `192.168.1.99`. Remember to check and edit the Gateway accordingly with your configuration (usually `192.168.1.1` or `192.168.0.1`).
  9. Go back and select `Go` to start installation. When completed, the Pi will reboot.

Once done, you may want to change your password. Type: `# passwd`

* * *

### (Optional) Autologin

Since your Pi is going to work as an _headless_ server, it may be useful if it could automatically login whether a spontaneous reboot occurs (as a sudden change in voltage, for instance). 

  * Type: `# nano /etc/systemd/system/getty.target.wants/getty@tty1.service`
  * Edit the line `"ExecStart="` as follows: `ExecStart=-/sbin/agetty -a root %I $TERM`
  * Save with `CTRL+X` and quit.

_Note: use this setting**ONLY** if you are sure you are the only one who can physically access to your Pi._

* * *

Now you can turn off the Pi, move it wherever you like and use it via SSH from your main PC, using [Putty](http://www.putty.org/) (on Windows) or `ssh root@192.168.1.99` from your Linux terminal. 

## Configure the DNS

Connecting to your server via your modem IP address is awkward, as it changes every now and then - that's why we are going to set up a dynamic DNS service, which gives you an human-readable address and takes care of linking it with your modem IP. 

### FreeDNS

  1. Register on `http://freedns.afraid.org/`
  2. Login. From the menu on the left select `Dynamic DNS`. At the bottom of the page, create a new record - let's use `mypi.homenet.org` as a reference.
  3. Click on `Direct URL `[![FreeDNS](/assets/posts/2016/07/a-free-cloud-how-to-configure-nextcloud-freedns.png)](https://fravaccaro.wordpress.com/freedns/)
  4. The address bar will display an URL of this kind: `http://freedns.afraid.org/dynamic/update.php?[alphanumeric code]`
  5. Take note of the alphanumeric code.

### Inadyn

  1. On the Pi, install inadyn by typing: `# apt-get install inadyn`
  2. Backup the default configuration: `# mv /etc/inadyn.conf /etc/inadyn.conf.bk`
  3. Create a new one: `# touch /etc/inadyn.conf`
  4. Then edit it: `# nano /etc/inadyn.conf`
  5. Type: `--username yourfreednsusername --password yourfreednspassword --update_period 3600 --forced_update_period 14400 --alias mypi.homenet.org,freednsalphanumericcode --background --dyndns_system default@freedns.afraid.org --syslog`
  6. Save and quit.
  7. Set inadyn to start on boot: `# crontab -e`
  8. Type: `@reboot /usr/sbin/inadyn`
  9. Save and quit.

## Create and install the cert

  1. Create a new SSL certificate by typing: `# dietpi-letsencrypt`
  2. In the newly opened window insert: In Domain: `mypi.homenet.org` In Email: `your email` In Redirect: `Enabled` In Auto Renew: `Enabled` In Key Size: `2048`
  3. Then apply your settings.

_Note: it may take some time, if you see it stuck on 'Installing Python packages' for a while don't panic and let it finish._

## Configure the router

  1. Open a browser and login into your router (usually the address is something like `192.168.1.1` or `192.168.0.1`, but you may want to check it on the bottom/rear tag on the modem or on its user manual).
  2. Look for an option called _Port mapping_ (or similar).
  3. Open the ports 80 and 443 to your Pi IP address. [![Router configuration](/assets/posts/2016/07/a-free-cloud-how-to-configure-nextcloud-router_configuration.png)](https://fravaccaro.wordpress.com/2016/07/09/a-free-cloud-how-to-configure-nextcloud/router_configuration/#main)

Now you should be able to access to your server from any browser using the URL `mypi.homenet.org`

## Configure Nextcloud

  1. On a browser type: `https://mypi.homenet.org/nextcloud`
  2. Login by using: In User: `admin` In Password: your`dietpi`
  3. Change your password from `Admin` in the top-right menu. From there you can also add your profile picture or customize other options.

Once done, you can use your brand new Nextcloud! _Tip: you can create an user with the user name of your choice (and use those credentials to manage your cloud and login into apps) by using` Users` via the top-right menu._

### Set up your own language

You can switch to your own language by using `Admin` via the top-right menu. 

### Contacts and Calendar

You may need to manually activate the Contacts and Calendar apps by using `Applications` on the top-left menu. _That's all folks!_ Have fun using Nextcloud and regaining control over your own data.__ Sources [DietPi: Download DietPi image | Getting started](http://dietpi.com/phpbb/viewtopic.php?f=8&t=9), [DietPi: (Step by Step Guide) DietPi - Owncloud](http://dietpi.com/phpbb/viewtopic.php?f=8&t=10), [Techjawab: Setup Dynamic DNS / DynDNS for *FREE* on Raspberry Pi / Ubuntu ](http://www.techjawab.com/2013/06/setup-dynamic-dns-dyndns-for-free-on.html), [Details for ALL installation options](http://dietpi.com/phpbb/viewtopic.php?f=8&t=5&p=3026#p3026)
