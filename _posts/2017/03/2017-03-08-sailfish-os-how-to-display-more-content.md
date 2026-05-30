---
layout: post
title: "Sailfish OS: how to display more content"
date: 2017-03-08 09:07:06 +0000
tags: ["DPR", "guide", "PPI", "Sailfish OS"]
---
Some people prefer to have a more content-packed screen to have as much information as possible at a glance. On Android devices, this can be obtained by fiddling with DPI, i.e. the amount of dots per inch, while on Sailfish OS the device pixel ratio (DPR) is used for the same purpose - more on this [here](http://stackoverflow.com/a/21413366). 

## Check the DPR

The DPR value is stored in a dconf key. To read the value open the terminal and type, as regular user: `dconf read /desktop/sailfish/silica/theme_pixel_ratio` On a Jolla C, this will return a value of 1.25. 

## Custom value

Empirically, a lower number would give more space to be filled by content, at the expense of a smaller font (although this can be tuned from the Settings). To edit the value type, as regular user: `dconf write /desktop/sailfish/silica/theme_pixel_ratio VALUE` then refresh the homescreen. 

### DPR 1.10

Type, as regular user: `dconf write /desktop/sailfish/silica/theme_pixel_ratio 1.10` then refresh the homescreen. [![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_001.png) ](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_001/#main)![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_011.png) ![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_010.png) [![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_002.png)](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_002/#main)

### DPR 0.90

Type, as regular user: `dconf write /desktop/sailfish/silica/theme_pixel_ratio 0.90` then refresh the homescreen. [![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_012.png) ](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_012/#main)[![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_005.png) ](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_005/#main)[![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_013.png) ](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_013/#main)[![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170307_008.png)](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170307_008/#main)

## Reset the DPR to the default value

Type, as regular user: `dconf reset /desktop/sailfish/silica/theme_pixel_ratio` then refresh the homescreen. 

## Tablet UI

With smaller DPR values, it may make sense to enable the quick settings sidebar like seen on the Jolla Tablet. Open, as root, the file: `/usr/share/lipstick-jolla-home-qt5/main/Desktop.qml` locate the line: `property bool showEventsViewSidebar: Screen.sizeCategory >= Screen.Large` and change it as following: `property bool showEventsViewSidebar: Screen.sizeCategory >= Screen.Small` then refresh the homescreen. [![](/assets/posts/2017/03/sailfish-os-how-to-display-more-content-schermata_20170308_003.png)](https://fravaccaro.wordpress.com/2017/03/08/sailfish-os-how-to-display-more-content/schermata_20170308_003/#main)

## Alien Dalvik

Android apps will follow a standard DPI setting. To tune it open, as root, the file: `/opt/alien/system/build.prop` then edit the following line: `ro.sf.lcd_density=VALUE` Even here, a lower number would give more space to the content. Common values are 240, 280, 300, 320. Restart the Android environment to apply the changes. 

## Wrap-up

I may work on some simple UI to edit the DPR value, but my programming skiils are really limited, so feel free to use the infos from this post to create your app/patch, considering a link to this page if it was useful. 

## Update

A preliminary package has been uploaded [here](https://openrepos.net/content/fravaccaro/ui-themer).
