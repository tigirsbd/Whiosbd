#!/usr/bin/python2 
import os 
import sys
#Hi I am Tigris BD.This Is my first tool in termux.
print ('\033[1;92m')
os.system("figlet Rifat")
print('\033[1;91mEnter your url without https:// or www Exmple:example.com'


)

print ('\033[1;95mYou can find subdomain name or other information in this tool'



)


print ' \033[1;92mcontact: www.facebook.com/graymanbd71'

url=raw_input('\033[1;94m[+] Eenter your url:\033[1;92m')
os.system("whois %s" % (url))