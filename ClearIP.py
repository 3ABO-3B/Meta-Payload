from os import system
from time import sleep


system ('clear')

print ('''\033[1;31m				  	    ____ _                   ___ ____  
					   / ___| | ___  __ _ _ __  |_ _|  _ \ 
					  | |   | |/ _ \/ _` | '__|  | || |_) |
					  | |___| |  __/ (_| | |     | ||  __/ 
					   \____|_|\___|\__,_|_|    |___|_|    
						                                     
''')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
ip_list = raw_input('\033[1;35m[\033[1;33m+\033[1;35m] \033[0;36mEnter Place and Name of Your IP List : \033[0;37m')
the_f3_num = raw_input('\033[1;35m[\033[1;33m+\033[1;35m] \033[0;36mEnter The First 3 Numbers in Your IP : \033[0;37m')
filtred_list_name = raw_input('\033[1;35m[\033[1;33m+\033[1;35m] \033[0;36mPut The Name of Filtred List : \033[0;37m')
						#filtring
system('cat '+ip_list+' | grep '+the_f3_num+'. | awk \'{print $1}\' | sort | grep '+the_f3_num+'. | uniq > '+filtred_list_name)
						#end-filtring
print ('						\033[1;32mThe Filtred List is Created succefully !')
sleep(3)
system('clear')
exit()
