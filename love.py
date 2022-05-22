import os
import random
import sys
import time
os.system("clear")
os.system("pkg install figlet")
os.system("clear")
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik("hallo kamu, hari yang cerah ini saya mau menyampaikan sesuatu")

import os
import sys
def main():
	os.system("figlet LOVE YOU")
main()
print "     maukah kamu jadi pacarku??"
def menu():
     print ("""
     >maulah masa nggak kiw kiw<
	1.mau
	2.nggak
	3.prinsip
	0.exit
	""")
menu()

pilih = raw_input("nomor : ")
if pilih =="":
	os.system("clear")
	print "tidak ada pilihan??, iya terimakasih"
	os.system("python2 love.py")
	
if pilih =="0":
	os.system("clear")
	exit()
	
if pilih =="1":
	os.system("clear")
	os.system("python2 mau")
	
if pilih =="2":
	os.system("clear")
	os.system("python2 nggak")
	
if pilih =="3":
	os.system("clear")
	os.system("python2 perinsip")