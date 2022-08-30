B = '\u0040\u006C\u0061\u006D\u0065\u0072\u0031\u0031\u0032\u0033\u0031\u0031' #blue
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

from datetime import datetime
import getpass
import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp
from shutil import which
from colorama import init 
from colorama import Fore, Back, Style
import time
import smtplib
import multiprocessing
from os import system
import re
version = '1.1'
time.sleep(3)
print(G + '[+]' + C + ' Проверка обновлений.....', end='')
ver_url = 'https://raw.githubusercontent.com/pashokkok/DeClient/main/version.txt'
try:
	ver_rqst = requests.get(ver_url)
	ver_sc = ver_rqst.status_code
	if ver_sc == 200:
		github_ver = ver_rqst.text
		github_ver = github_ver.strip()

		if version == github_ver:
			print(C + '[' + G + ' Актуально ' + C +']' + '\n')
		else:
			print(C + '[' + G + ' Доступно : {} '.format(github_ver) + C + ']' + '\n')
			print(R + '[-] Пожалуйста, обновите DeClient до актуальной версии \n')
			newver = input(G + '[1]' + C + 'Как мне обновить DeClient до новой версии? \n' + G + '[2]' + C + 'Выйти' + G + '\nMe4Sploit ==> ')
			if newver == "1" :
				print(Fore.MAGENTA)
				print('Пункт 1: Зайдите в наш телеграм канал')
				time.sleep(3)
				print('Пункт 2: Удалите папку Me4Sploit')
				time.sleep(3)
				print('Пункт 3: Скачайте новый Me4Sploit командой: "git clone https://github.com/pashokkok/Me4sploit"')
				time.sleep(3)
				print('Пункт 4: Зайдите в папку Me4Sploit командой: "cd Me4Sploit"')
				time.sleep(3)
				print('Пункт 5: Запустите инсталлер командой: "bash install.sh", последующие запуски проводятся командами: "python Me4Sploit.py"')
				time.sleep(3)
				print('Удачи! Мы вас ждем с новой версией!')
				time.sleep(5)
				exit()
			if newver == "2":
				exit()
			
	else:
		print(C + '[' + R + ' Статус : {} '.format(ver_sc) + C + ']' + '\n')
except Exception as e:
	print('\n' + R + '[-]' + C + ' Исключение : ' + W + str(e))

def choice():
	print('█▀▄ █▀▀ █▀▀ █░░ █ █▀▀ █▄░█ ▀█▀')
	print('█▄▀ ██▄ █▄▄ █▄▄ █ ██▄ █░▀█ ░█░')
	print("DeClient@" + getpass.getuser() + "          |  Support  |        ")
	print("DeClient@" + getpass.getuser() + "   Termux |   Linux   | Windows")
	print("DeClient@" + getpass.getuser() + "          |    1.0    |        ")
	print("DeClient@" + getpass.getuser() + "          |  DeClient |        ")
	print(G + '[1]' + C + ' ActiveKey')
	print(G + '[2]' + C + ' Cracker')
	print(G + '[3]' + C + ' Exit')
	print('\n')
	print(Fore.GREEN)
	option = input('Me4Sploit ==>  ')
	if option == "1":
		key = input ("Syst-Key: ")
		
		if key == "DeClientFree":
			print( Fore.GREEN )
			print('Active')
			time.sleep(2)
			lists = input ('[Exit] Exit \n[1] Gemail-hack \n[2] B0mb3r \n[3] Mail-Spammer \n[4] Brute_Force \n[5] Grab-Cam \n[6] Shark \n[7] CrossFire Ddos \n[8] FaceBook_Brute \n[9] AresBomb \n[10] Track-Em \n[11] Cardesc \n[12] Insanity-Framework \n[13] Entropy Toolkit \n[14] Airgeddon \n[15] ISniff-GPS \n[16] Trape \n[17] Kali Nethunter \n[18] XAttacker \n[19] WordSteal \n[20] SpiderFoot \nMe4Sploit ==>  ')
			
			if lists == "Exit":
				exit()
				
			if lists == "exit":
				exit()
				
			if lists == "1":
				os.system('git clone https://github.com/Ha3MrX/Gemail-Hack')
				
			if lists == "2":
				os.system('git clone https://github.com/Denishnc/b0mb3r')
				
			if lists == "3":
				os.system('git clone https://github.com/pashokkok/Mail_Smmp')
			
			if lists == "4":
				os.system('git clone https://github.com/Tim55667757/pwd_brut')
				
			if lists == "5":
				os.system('git clone https://github.com/noob-hackers/grabcam')
			
			if lists == "6":
				os.system('git clone https://github.com/Bhaviktutorials/shark')
				
			if lists == "7":
				os.system('git clone https://github.com/crossfireTeam/crossfireMSDOS')
				os.system('cd crossfireMSDOS')
				os.system('cmake CMakeLists.txt')
				os.system('chmod +x Makefile')
				
			if lists == "8":
				os.system('git clone https://github.com/pashokkok/FB')
				
			if lists == "9":
				os.system("pkg install git")
				os.system("pkg install python")
				os.system("pip install requests")
				os.system("git clone https://github.com/MaksPV/AresBomb")
				
			if lists == "10":
				os.system("git clone https://github.com/LiNuX-Mallu/Track-Em.git")
				
			if lists == "11":
				os.system("git clone https://github.com/escdroid/cardesc.git")
				
			if lists == "12":
				os.system("git clone https://github.com/4w4k3/Insanity-Framework")
			
			if lists == "13":
				os.system("pip install tailer")
				os.system("git clone https://github.com/evildevill/entropy")
				
			if lists == "14":
				os.system("git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git")
				
			if lists == "15":
				os.system("git clone https://github.com/hubert3/iSniff-GPS.git")
			
			if lists == "16":
				os.system("git clone https://github.com/jofpin/trape.git")
				
			if lists == "17":
				os.system("pkg install wget")
				os.system("termux-setup-storage")
				os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
				os.system("chmod 777 install-nethunter-termux")
				os.system("./install-nethunter-termux")
				
			if lists == "18":
				os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git")
				
			if lists == "19":
				os.system("git clone https://github.com/0x09AL/WordSteal.git")
				
			if lists == "20":
				os.system("git clone https://github.com/smicallef/spiderfoot")
				
			else:
				print('ERROR: 102' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Tool')
		
		else:
			print( Fore.RED )
			print('ERROR: 101' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Syst-Key')

	if option == "2" :
		os.system('clear')
		print('Tipo Xaker :3')
		time.sleep(2)
		print(Fore.GREEN)
		print('Openning Matrix')
		time.sleep(1)
		print('Starting Tools')
		time.sleep,(3)
		print('Starting Cracker.py')
		time.sleep(3)
		os.system('pkg install cmatrix')
		os.system('cmatrix')

	if option == "3" :
		exit()
try:
	choice()
	
	
except:
	print("end")

