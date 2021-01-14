# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020-2023 Luna Rosé                                           #
#                                                                         #
#	This file is part of a two step verification script similar to google.  #
#                                                                         #
# Advanced Hash is free software: you can redistribute                    #
#	it and/or modify it under the terms of the GNU General Public License   #
#	as published by the Free Software Foundation, either version 3 of the   #
#	License, or (at your option) any later version.                         #
#                                                                         #
# Advanced Hash is distributed in the hope that it                        #
#	will be useful, but WITHOUT ANY WARRANTY; without even the implied      #
#	warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See    #
#	the GNU General Public License for more details.                        #
#                                                                         #
# You should have received a copy of the GNU General Public License along #
# with Advanced Hash.  If not, see <http://www.gnu.org/licenses/>.        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import all libraries
import re
import time
import json
import socket
import random
import decimal
import datetime
from tkinter import *
from tqdm import tqdm
from twilio.rest import Client
from urllib.request import urlopen

#IPinfo.io database variables
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

#IP variables
IP = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

# getting the date by datetime.datetime.now() method
x = datetime.datetime.now()

# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# defining locationinfo for log.txt
locinfo = 'IP : {4} Region : {1} Country : {2} City : {3} Org : {0}'.format(org,region,country,city,IP)

# on start generate key to file
rand_num = decimal.Decimal(str(random.uniform(1000, 10000)))

# write randomized XXXX key to file
f = open("gen_code.txt", "w+")
if f.mode == 'w+':
    contents = f.read()
    if contents == "":
      f.write("%d" % rand_num)
      f.close()
    else:
      f.close()
      print("Code is already generated")
else:
  print("File did not open correctly, please try again")
  time.sleep(1)
  print("Shutdown in 3")
  time.sleep(1)
  print("Shutdown in 2")
  time.sleep(1)
  print("Shutdown in 1")
  time.sleep(1)
  exit()

# ask for number which number will be sent to
print("Before we start, what is your number?")
int_num = input("Remember +XX in front of the number: ")

# twilio Cloud service etc.
client = Client("AC136ebf4a0dc4a917ff1fa0b3ed8895d4", "fbd57c3387c3692c3dc556dcff427c3e")
client.messages.create(to=int_num, 
                       from_="+3197010253003", 
                       body="Your encryped code is - %d" % rand_num)

# Welcoming user categorized by ip_address
print("§ Welcome ip: %r" % (ip_address))
time.sleep(1)

print("§ Please login with given access-key")
print("............................................")

# verifying that given key is correct and granting access
encrypkey = input("Key: ")

f = open("gen_code.txt", "r")
if f.mode == 'r':
    contents = f.read()
    if contents == encrypkey:
      time.sleep(2)
      print("............................................")
      print("#### Uploading and verifying key ####")
      print("............................................")
      print("Running key-verification: ")
      f.close()
    else:
      f.close()
      l = open("log.txt", "w+")
      l.write("## Failed attempt ##\n")
      l.write("Time:%r[GMT]\n" % x.strftime("%A %D %X"))
      l.write("Ip_address:%r\n" % ip_address)
      l.write("Key:%r\n" % encrypkey)
      l.write("\n")
      l.write("MiscData: %r\n" % locinfo)
      l.write("\n")
      time.sleep(2)
      print("............................................")
      print("Wrong key! This incident will be reported.")
      time.sleep(3)
      l.close()
      exit()
else:
  print("An error occured when trying to read file")

myList = [
    'Uploading key..',
    'Uploaded key §',
    'Key recieved..',
    'Key verified',
    'Verifying ip-adress..',
    'Ip-adress secure',
    'Sending confirmation..',
    '...',
    '..',
    '.',
    'Verification complete..',
    'Granting root access to user..',
    'Access granted, end of intermission',
]

for i in tqdm(myList):
    time.sleep(0.2)
    print(i)

print("............................................")
print("Welcome, you have logged in with key %r" % (encrypkey))
time.sleep(5)

print("............................................")
print("You can proceed to the database by typing $")
answer = input("§: ")

correct_ans = "$"

# start gui script to access recovery code
if (answer == "$"):
  class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Code verifier script")
        self.pack(fill = BOTH, expand = 1)

        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)

        edit = Menu(menu)
        edit.add_command(label = "Show Code", command = self.showTxt)
        menu.add_cascade(label = "Edit", menu = edit)
    
    def showTxt(self):
        text = Label(self, text = "XXXX-XXXX-XXXX-XXXX-XXXX-XXXX")
        text.pack()
    
    def client_exit(self):
        exit()

# define dimentions and root variables for GUI
  root = Tk()
  root.geometry("300x30")
  app = Window(root)
  root.mainloop()
else:
    print("That is not a command")
    exit()
