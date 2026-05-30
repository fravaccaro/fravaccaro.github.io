---
layout: post
title: "[ITA] Aumentare la dimensione del file di Swap su N9"
date: 2013-09-24 08:55:23 +0000
tags: ["aumentare", "guida", "italiano", "MeeGo", "N9", "Nokia", "Swap"]
---
Questo post è la versione italiana dell'[articolo precedente](http://fravaccaro.wordpress.com/?p=360), che spiega come aumentare la dimensione del file di Swap su MeeGo Harmattan. Ho deciso di riscriverlo in italiano perché mi sono reso conto che non esiste una traduzione della guida e potrebbe quindi risultare comodo per chi non mastica l'inglese o è pigro (sono con voi!). Non mi soffermerò su cos'è un file di Swap, perché se siete arrivati fin qui sapete cosa cercare. Dirò invece che questa guida è basata sul post scritto da Shaun su [EverythingN9](http://everythingn9.com/speed-mod-increase-the-swap-file-size/) (che vi consiglio, ad ogni modo, di leggere insieme al [thread su TMO](http://talk.maemo.org/showthread.php?t=86752)) qualche tempo fa. Ho sentito la necessità di riscriverlo dal momento che CODeRUS ha rilasciato _Aegis-hack_ e _OpenSudo_ e alcuni comandi sono cambiati. ENGLISH VERSION [HERE](http://fravaccaro.wordpress.com/?p=360). 

## Disclaimer

Siccome molti di voi lo salteranno, cercherò di essere il più coinciso possibile: FATELO SE SIETE SICURI DI COSA FATE. Leggete tutta la guida prima di iniziare. Se non avete idea di cosa ci sia scritto, non continuate o poi non prendetevela con me se qualcosa dovesse andare storto e dovrete flashare il vostro N9. 

## Per iniziare

1\. Innanzitutto, assicuratevi che la modalità sviluppatore sia attiva, con il terminale e l'_SDK Connectivity Tool_ installati correttamente. Dopodiché installate, preferibilmente via _N9QTweak_ , l'Aegis-hack, che a sua volta dovrebbe installare Opensudo. Scegliete una password per OpenSudo (per comodità potete usare `rootme`) e chiudete N9QTweak. 2\. Da terminale digitate: `devel-su` `rootme` `passwd user` Anche in questo caso vi consiglio l'ormai classica `rootme`. 3\. Se non lo avete già installato, installate _nano_ , un semplice editor di file, digitando: `# apt-get install nano` Ora potete chiudere il terminale. 

## Collegamento SSH

4\. Aprite l'SDK Connectivity Tool e selezionate WLAN, quindi segnatevi l'indirizzo IP. 5\. Se avete Windows, una buona idea è scaricare [Putty](https://www.dropbox.com/s/3b7t91ehn0f4o6m/putty.exe), che non ha bisogno di installazione. Da Linux invece è sufficiente aprire il terminale e digitare: `ssh user@indirizzoIP` In entrambi i casi, digitate la password che avete scelto in precedenza (passo 2). 6\. Una volta aperta la sessione SSH, digitate: `devel-su` `rootme` `sudo -s` `(password di OpenSudo, vedi passo 1)` `accli -I |grep tcb-sign` L'ultimo comando DEVE restituirvi: `aegis-enabler::tcb-sign` Se così non fosse, non continuate oltre. 

## La parte decisiva

7\. Digitate: `cp /etc/init/enable-swap.conf /tmp/enable-swap.conf` `nano /tmp/enable-swap.conf` 8\. A questo punto si aprirà nano. Trovate questa linea: `if [ $ramsize -gt 1000000 ]; then` e sostituite il primo `0` con un `1`, in modo che diventi: `if [ $ramsize -gt 1100000 ]; then` Quindi trovate questa linea: `swappart=`sed -n -e '/swap/s/mtd\([0-9]\).*/\1/p' /proc/mtd` || true` e sostituite `swap` con `var`, in modo che diventi: `swappart=`sed -n -e '/var/s/mtd\([0-9]\).*/\1/p' /proc/mtd` || true` Tenete premuto _Ctrl + X_ e salvate, assicurandovi che il nome del nuovo file corrisponda al nome di quello originale. 9\. Ora digitate: `cp /tmp/enable-swap.conf /etc/init/enable-swap.conf` `export A=`sha1sum /tmp/enable-swap.conf |cut -b1-40`;` `perl -pi -w -e 's#40 (.*) A(.*)enable-swap#40 $ENV{A} A$2enable-swap#smg' /var/lib/aegis/refhashlist` `accli -c tcb-sign -F /var/lib/aegis/refhashlist -i /var/lib/aegis/refhashlist` `/usr/sbin/validator-init; aegis-loader;echo 1 > /sys/kernel/security/validator/flush` `/sbin/reboot` 10\. A questo punto il cellulare si riavvierà. Incrociate le dita! 

## Conclusioni

Prima di applicare la mod, _DropCache_ segnala una dimensione del file di Swap di 255mb. Dopo, dovrebbe segnare 412mb. In soldoni, ora il telefono dovrebbe essere in grado di tenere più applicazioni aperte, prima di rallentare. Spero di esservi stato utile. A presto! 

_via [[1](http://everythingn9.com/speed-mod-increase-the-swap-file-size/)], [[2](http://everythingn9.com/how-to-use-putty-on-the-nokia-n9/)]_
