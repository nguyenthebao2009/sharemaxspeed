import requests,re,json,random,sys,os
import bs4,base64
from time import sleep
from time import sleep
from datetime import datetime
import random
from datetime import date
import requests, os, sys, re, json
from threading import Thread
import threading
import time
from random import choice, randint, shuffle
import json,requests,time
from time import strftime




os.system("cls" if os.name == "nt" else "clear")
bongoc="\033[1;37m~\033[1;31m[\033[1;32m✔\033[1;31m]\033[1;37m =>"
ngocdz="\033[1;33m──────────────────────────────────────────────────────────────────────                 "
def banner():
 banner = f"""
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)



time = datetime.now()

from random import choice, randint, shuffle
s = "\033[1;91m[\033[1;92m✔\033[1;91m] \033[1;97m=>"
def abbbabbabaaaaabbbbabbab(abbabbbabbb):
    print(abbabbbabbb)
r = "\033[1;91m[\033[1;92m✔\033[1;91m] \033[1;97m=>"
sr = "\033[1;33m[\033[1;31mNgoc\033[1;37mTool\033[1;33m]"
def dk():
   a= "\033[1;33m-"*31
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def sssh(tokenfb,linkbv):
   abbbbbababbbabababdababa = {
      'authority':'graph.facebook.com',
      'cache-control':'max-age=0',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
   requests.post(f"https://graph.facebook.com/me/feed?link="+linkbv+"&published=0&access_token="+tokenfb,headers=abbbbbababbbabababdababa).text
def aabbabababbabbababbababbbbaaabba(a):
   abbbabbabaaaaabbbbabbab(sr+"\033[1;32m Success \033[1;91m| \033[1;97m"+str(a)+" \033[1;91m| ")
def shareh(tokenfb,linkbv):
   head = {
      'authority':'graph.facebook.com',
      'cache-control':'max-age=0',
      'sec-ch-ua-mobile':'?0',
      'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36'}
   vvv = requests.post(f"https://graph.facebook.com/me/feed?link="+linkbv+"&published=0&access_token="+tokenfb,headers=head).text
   if 'id' in vvv:
     babbbdddabbaaaaabB = json.loads(vvv)['id']
     aabbabababbabbababbababbbbaaabba(babbbdddabbaaaaabB)
   else:
     abbbabbabaaaaabbbbabbab(aabbababababbbbbaaabbbbbaababb)
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()

os.system('clear')
banner()
list_token = []
for i in range(9999):
   tks = input(bongoc+"\033[1;92m Nhập Token Facebook Thứ "+str(i+1)+":\033[1;93m ")
   if tks != '':
      list_token.append(tks)
   else:
    break
linkbv = str(input(bongoc+"\033[1;92m Nhập Link Bài Viết: \033[1;93m"))

print("\033[1;31m──────────────────────────────────────────────────────────────────────  ")
while True:
   for a in range(len(list_token)):
        threading.Thread(target=shareh,args=(list_token[a],linkbv)).start()
