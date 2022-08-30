B = '\u0040\u006C\u0061\u006D\u0065\u0072\u0031\u0031\u0032\u0033\u0031\u0031' #blue
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

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
version = '1.0'
time.sleep(3)
print(G + '[+]' + C + ' Проверка обновлений.....', end='')
ver_url = 'https://raw.githubusercontent.com/pashokkok/Me4Sploit/main/version.txt'
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
			print(R + '[-] Пожалуйста, обновите Me4Sploit до актуальной версии \n')
			newver = input(G + '[1]' + C + 'Как мне обновить Me4Sploit до новой версии? \n' + G + '[2]' + C + 'Выйти' + G + '\nMe4Sploit ==> ')
			if newver == "1" :
				print(Fore.MAGENTA)
				os.system('clear')
				print('Пункт 1: Зайдите в каталог с папкой Me4Sploit')
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

