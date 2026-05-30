---
layout: post
title: "Overclocking: guide from a n00b perspective"
date: 2013-04-17 17:58:35 +0000
tags: ["guide", "how to", "MeeGo", "mod", "N9", "Nokia", "OPPtimize", "overclock"]
---
I'm a N9 n00b, no problem saying that. The best part of the story is that I'm happy to learn and try out new things, so my experience with the N9 suits me perfectly. One of my latest achievement in the N9 modsland is overclocking. Thanks to the always kind Andy ([@N9Andy](<http://twitter.com/N9Andy>)) I managed to find out a safe clock for the not so up-to-date 1GHz CPU, that makes my N9 silky smooth.

## Disclaimer

Before to start, please keep in mind the following: 1) You have to be aware what the overclock is. If you don't know, please read up what it is, what it does and all the pros and cons. Internet is your friend. 2) These are the steps I made on MY device to make the thing works, so if you make everything right you should not be in troubles. Anyway, I am not responsible for what you choose to do on your device. 3) This mod worked for me and almost all the N9 users I know, but if you notice your device becomes unstable, please take everything back to the default values. 4) If something differs for you or you have any question, please don't hesitate to ask to me or, best option, to the [proper thread](<http://talk.maemo.org/showthread.php?t=83357>) on the [TMO forum](<http://talk.maemo.org/>). 

## Before you start

First of all, ensure you run _Inception_ mod on your N9. If not, the fastest way is to apply it via _QTweak_ (a comprehensive wiki is available [here](<http://wiki.maemo.org/N9QTweak>)). Have you already incepted your device? Well, let's start. 

## Installation

1) Download these two files: [Kernel Modules 1.5.4](<http://www.appcheck.net/storage/opptimizer_1.5.4_armel.deb>) [User Interface 1.2.7](<http://www.appcheck.net/storage/opptimizer-ui_1.2.7_armel.deb>) 2) Don't try to direct-install them, you will be given an installation error. Instead, move them in the `MyDocs` folder. Files are located into the `.downloads` folder, so you may have to enable the "Show hidden files" option into the _FileCase_ settings page (of course you can use any file browser you want). 3) Open your preferred terminal app and type: `devel-su` Type your password. If you've not changed it, the default one is `rootme`. Press enter again. 4) Type: `/usr/sbin/incept /home/user/MyDocs/opptimizer_1.5.4_armel.deb` You will be asked to type your devel-su password. Type it and wait until the process ends. 5) Enter: `/usr/sbin/incept /home/user/MyDocs/opptimizer-ui_1.2.7_armel.deb` 6) Again, type your password and wait until the process ends. 

## OPPtimization

1) Close your terminal and open _OppUI_. You will be prompted on a screen like this: [![OppUI](/assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-09-43-1.png)](</assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-09-43.png>) 2) Switch to the _Settings_ tab. [![OppUI](/assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-09-26-1.png)](</assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-09-26.png>) 3) Leave _Custom voltage_ untouched and drag the _Frequency (MHz)_ indicator up to 1100, Andy has setted it up to 1150. Some users have taken the clock up to 1200 MHz and beyond, but both Andy's and mine ones should be safer and less stressing for the CPU. 4) Move to _Test iterations_ and drag the indicator up to 15000. Now you are ready to press the _OPPtimize!_ button. This is what you get: [![OppUI - test](/assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-34-15-1.png)](</assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-34-15.png>) 5) Wait until the process ends. It will take about 10 minutes, so be patient. After it ends, you will be able to set the _Apply on startup_ switch on: [![OppUI](/assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-34-39-1.png)](</assets/posts/2013/04/overclocking-guide-from-a-n00b-perspective-2013-04-17_17-34-39.png>)

## Battery impact and considerations

I dare to say overclock doesn't affect my battery life so much, I can reach 12-13 hours of mixed usage quite easily. To reach the best experience, you can also install the _FasterN9_ mod (either in the QTweak package); the latest stable 1.0.1 version is bug-free. I have currently brought my N9 back to the default 1GHz clock to test the impact on the active usage. Battery Usage reported up to 284mA consumption with 1.1GHz - idle usage settles around 16-22mA. I'm going to to test if there is any remarkable difference and post the results in the following days. 

Thanks to [@N9Andy](<http://twitter.com/N9Andy>) and [@TheRajN9](<http://twitter.com/TheRajN9>) to have been my mod companion | [_via_](<http://talk.maemo.org/showthread.php?t=83357>)
