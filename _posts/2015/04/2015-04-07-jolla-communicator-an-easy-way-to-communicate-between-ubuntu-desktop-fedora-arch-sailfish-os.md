---
layout: post
title: "Jolla Communicator: An Easy Way to Communicate between Ubuntu Desktop, Fedora, Arch & Sailfish OS"
date: 2015-04-07 20:11:49 +0000
tags: ["Arch", "Fedora", "Jolla Communicator", "Sailfish OS", "Ubuntu"]
---
Nowadays, everything spins around ecosystems: Apple, Microsoft and Google are continuously tightening their products' experience to make the life or their users easier (and well, try to bound them to their services, but this is another story). What if we use GNU/Linux? We've been trough hard times, poor support and so on. But now now things are a-changing. Yes, because Jolla and their Sailfish OS are the new big guys in the city and with the growing interested of the FLOSS community, we may be at the beginning of a new, community-driven ecosystem. After [KODI](https://openrepos.net/content/robertme/kodimote) and [VLC](https://openrepos.net/content/mariusmssj/vlc-remote) controllers, [URLs and text forwarders](https://openrepos.net/content/mkiol/send-phone) and [picture uploaders](https://openrepos.net/content/beidl/owncloud-photo-backup-daemon), another block has been added: [Jolla Communicator](http://www.messaggiero.it/blogpost.php?id_images=8). [![Jolla Communicator](/assets/posts/2015/04/jolla-communicator-an-easy-way-to-communicate-between-ubuntu-desktop-fedora-arch-sailfish-os-schermata-del-2015-04-01-17)](https://fravaccaro.wordpress.com/2015/04/07/jolla-communicator-an-easy-way-to-communicate-between-ubuntu-desktop-fedora-arch-sailfish-os/schermata-del-2015-04-01-17_10_12/#main) Unlike [similar solutions](http://talk.maemo.org/showthread.php?p=1433854#post1433854), it doesn't require any app to be installed on the phone, but it's a PC client (compatible with Ubuntu 14.04 and higher) that lets you read and write messages on the phone. These are the features included so far: 

  * Connection via USB.
  * Connection via WLAN.
  * Reading messages on the Jolla phone.
  * Picking a contact and send them a message.

The configuration is pretty straightforward: 
  1. If you want to connect your phone to the computer via WiFi, make sure they are connected to the same network.
  2. Enable `Developer mode` on your phone via `Settings > Developer mode`.
  3. On the same page, enable `Remote connection` and set a password.
  4. If you want to connect your phone and the computer via WiFi, take note of the WLAN IP address.
  5. If you want to connect your phone and the computer via USB, take note of the USB IP address, then connect your phone to the computer and select `Developer mode` in the pop up on your Jolla.
  6. Download the `.deb` package from [this page](http://www.messaggiero.it/blogpost.php?id_images=8) and install it on your Ubuntu-based distro.
  7. Open the application and insert the IP address, the remote connection password and select your country code.
  8. Once you saved your settings, start the connection by clicking the button in the toolbar.

You've done! To read and delete your messages use the `SMS` tab, to write a new one pick a contact from the `Contacts` tab. 

### Update

The developer has just released the Fedora-compatible package. You can download it from [here](http://www.messaggiero.it/blogpost.php?id_images=8). `libssh` may be needed, install it via `yum install libssh` The application has been ported to Arch Linux as well and it's downloadable from the [AUR repository](https://aur.archlinux.org/packages/jollacommunicator/). [Source](<>) [Source](http://jollacommunity.it/leggere-ed-inviare-messaggi-dal-proprio-pc-ubuntu/) | [Appeared on JollaUsers](http://www.jollausers.com/2015/04/jolla-communicator-an-easy-way-to-communicate-between-ubuntu-desktop-sailfish-os/)
