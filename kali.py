#!/bin/usr/python

import os
import sys
import random, time


def run(s):
	for khazul in s + '\n':
		sys.stdout.write(khazul)
		sys.stdout.flush()
		time.sleep(100. / 2000)

os.system('clear')
print """\033[1;34m

               KALI LINUX BASIS GUI
	      ----------------------
Author : Khazul Yussery Shadiq
Name   : ZuLF4

   --------------------------
   |      Bahan - Bahan     |
--------------------------------------------------
1]. VNC Viewer ->>>>> Bisa Download Di Playstore |
2]. Termux ->>>>> Bisa Download Di Playstore     |
3]. Kouta ->>>>> Beli di Konter                  |
--------------------------------------------------
"""

n = raw_input(" Siapa Namanya? ")
if not n:
	print
	print "\033[1;33m [+] Seberapa Cantik sih nama lu bangsat !!! "
	sys.exit()
else:
	print
	print "\033[1;33m Salam Kenal ",n

a = raw_input(" Mau langsung nginstall? [y/t]: ")
if a == "y" or a == "Y":
	print
	os.system('clear')
	os.system('cowsay -f dragon "Kali Installer" ')
	print
	run("\033[1;31m   Hai nama aku khazul yussery shadiq")
	print
   	print " [+] Periksa Koneksi ! "
	time.sleep(3.5)
	print
	print " [+] Sukses ! "
	print
	run("\033[1;31m  Mungkin ini memerlukan Waktu beberapa menit ... ")
	print
b = raw_input("\033[1;31m  Apakah Anda Bersabar? (y/t): ")
if b == "y" or b == "Y":
	print
	print " [+] Oke Kita Lanjutkan Prosesnya "
	time.sleep(3.5)
	os.system('clear')
	os.system('pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
	os.system('./start-kali.sh')
