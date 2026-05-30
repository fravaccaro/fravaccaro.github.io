---
layout: post
title: "Sailfish OS: a new Events view concept"
date: 2017-03-01 19:17:20 +0000
tags: ["concept", "Events view", "notifications", "Pointless thoughts", "Sailfish OS", "UI", "UX"]
---
I do love the _MeeGo-ish_ Sailfish OS 2.x UI for a very simple reason: it brings you, _straight in your face_ , two main aspects of modern smartphones, usually hidden in other OS’: multitasking and notifications. The main flaw is that most of the time they act like blank canvas and I have no way to retrieve my recent activities on the smartphone. Should it change? 

## Sailfish OS 2.2

In this post I will focus mainly on the Events view and notifications - which in my humble opinion need the more love - but I will also suggest a way to make the multitasking view more useful than it is today. Surprise surprise, I even included some _superb_ first grade-level sketches to show what my idea is. 

## The Home view

[![Pin app cover](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn6005.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn6005/#main)A simple addition would dramatically improve the usefulness of the multitasking view: adding pinned apps. Since in Sailfish OS 2.x there’s no longer the 9 covers view limit of the 1.x iteration, having apps pinned at startup would both help to interact with the most used ones (even because of muscle memory) and partially solve the current lack of an autostart option (at least in Store-approved apps). 

## The Events view

It would not be heretic to say that nowadays the Events view is largely underused; the Twitter feed shows only the last 10 tweets and changes in the Facebook APIs prevent a future implementation of a feed (as it was in MeeGo Harmattan). So why not taking the whole feed away (albeit it could be implemented in a different way, more on this later) and focusing on notifications? 

### A notification hub

[![Events view](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn6006.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn6006/#main)The main Events view screen would show, from top to bottom: 

  * The weather widget.
  * A larger-than-today calendar widget.
  * A _What's on your mind?_ form to post across different social networks.
  * Music player controls for the running MPRIS-enabled player (if any).
  * Notifications.

The main difference with the current behaviour would be than, once selected, the notification would not go away, but change status as read and stay to form a notification history _à la Blackberry 10_. Also, if the Events view is accessed from an app with the left swipe, swiping away from the events would bring the user back to the previous active app. To interact with the new system, a pulley menu would offer (from top to bottom): 

  * Clear all notifications
  * Mark all as read
  * Categories
  * Show unread only/all

_Note: 'Clear' is used to actually delete the notification(s) from the list._

#### Notification item

[![Expanded notifications](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn6004.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn6004/#main)Interaction with the notification item would occur in three ways: 

  * Tap: to open the app.
  * Long-tap: to show a contextual menu with _Mark as read/unread_ and _Clear notification_ options.
  * Swipe up/down with two fingers: to expand/collapse the notification. It’s an action already in use in Android, so it would not feel totally new to an user. Furthermore, the expanded view would provide a max. 2 quick actions, ideally including inline replies in case of a messaging app. These are also present in Android, so an update to the Alien Dalvik would expose this feature even for Android apps (Option B: to improve one-hand usability, quick actions can be placed in the long-tap menu).

_Note: even the weather and the calendar widgets may profit from the two fingers-to expand gesture._

#### Category item

Interaction with the category item would occur in two ways: 

  * Tap: to open the category page.
  * Long-tap: to show a contextual menu with _Mark category as read/unread_ , _Change priority_ and _Clear category notifications_ options.

To avoid clutter, only the first 4-5 notifications per category could be displayed, with a _more_ button right below - as it happens with the current implementation. 

#### Category view

[![Category view](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn5999.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn5999/#main)Selecting this option from the pulley menu would open an attached page with a simple list of all the notification categories (well, the apps those notifications are from) alongside an individual indicator with a unread/total count. 

#### Category page

[![Category page](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn5998.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn5998/#main)This would list all the notifications from the given app. Interaction with the notification items would be the same as in the main Events view. The pulley menu would offer (from top to bottom): 

  * Clear category notifications
  * Change priority
  * Mark category as read/unread

Below the notifications, an optional feed could be displayed (as with Twitter). 

## Priority

To better sort all the apps the notifications are from, I would introduce a priority system: 

  * High: notifications from this category trigger a sound/vibration and are displayed above all the other notifications in the Events view. They have a notification icon in the lockscreen.
  * Normal: notifications from this category trigger a sound/vibration and are displayed below all the important notifications in the Events view. They don’t have a notification icon in the lockscreen.
  * Low: notifications from this category don’t trigger a sound/vibration and are displayed below all the normal notifications in the Events view. They don’t have a notification icon in the lockscreen.

## Notification banner

[![Notification banner](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn6002.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn6002/#main)A bigger notification banner would fit the entire screen width and offer the following interactions: 

  * Tap: to open the app.
  * Swipe left/right: to dismiss the notification.
  * Swipe up/down with two fingers: to expand/collapse notification. Furthermore, the expanded view would provide a max. 2 quick actions, ideally including inline replies in case of a messaging app Option B: to improve one-hand usability, a one-finger swipe can be used).

## What about the controls?

[![Controls/Ambiences drop-down menu](/assets/posts/2017/03/sailfish-os-a-new-events-view-concept-dscn6001.jpg)](https://fravaccaro.wordpress.com/2017/03/01/sailfish-os-a-new-events-view-concept/dscn6001/#main)With the pulley menu taking the upper-part of the Events view, toggles and quick actions would be moved to the Ambience drop-down menu. This would make them more accessible throughout the whole system. The new drop-down would show (from top to bottom): 

  * A narrower lock button.
  * Toggles and quick actions.
  * Favourite ambiences.

## Wrap-up

I tried to be as comprehensive as possible. I’m not an UI designer myself and of course I don’t want to criticize the amazing work designers have been doing on the platform, but I wanted to show my thoughts on the areas which may be improved. Comments and suggestions are welcome. [Cover image](https://cdn-blog.jolla.com/wp-content/uploads/2015/09/events.jpg)
