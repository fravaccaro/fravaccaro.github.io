---
layout: post
title: "Disable Android environment in Jolla at startup"
date: 2014-08-14 10:56:39 +0000
tags: ["Alien Dalvik", "Android", "disable", "environment", "guide", "Jolla", "Sailfish OS", "startup"]
---
I realized the first think I do as I bootup my Jolla is stopping the Alien Dalvik. Having it on Sailfish is handy (and it really comes in help when you can't find the needed apps on Store/Warehouse), but it slow down my phone at start (to check the various notifications), so I looked for something to disable it. First, make sure you have nano installed on your Jolla. If it isn't there, install it with: `pkcon install nano`

### Complete disabling (prevent Android apps to start)

`devel-su <password> systemctl stop aliendalvik.service systemctl mask aliendalvik.service` To re-enable it: `# systemctl unmask aliendalvik.service # systemctl start aliendalvik.service`

### Disabling the Alien Dalvik at startup (it will start when you want to)

From the terminal: `devel-su <password> nano /etc/systemd/system/nodroidavvio.service` In nano paste: ` [Unit] After=aliendalvik.service Description=No Android al riavvio` `[Service] Type=oneshot RemainAfterExit=no ExecStart=/bin/systemctl stop aliendalvik.service` `[Install] WantedBy=multi-user.target` Close and save by pressing `CTRL+X` and within the terminal prompt: `# systemctl enable nodroidavvio.service` To re-enable the Alien Dalvik at startup: `# systemctl disable nodroidavvio.service`

_thanks to[@iliveinpublic](<http://twitter.com/iliveinpublic>) and [@eugenio_g7](<http://twitter.com/eugenio_g7>) for the tips._
