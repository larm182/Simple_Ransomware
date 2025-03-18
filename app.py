#!/usr/bin/env python
import random, os
from flask import Flask
from cryptography.fernet import Fernet
import re
import json
from urllib.request import urlopen

app = Flask(__name__)

profile = 100000
ip = 100000

ruta = os.getcwd() + "/output/"

@app.route("/")

def inicio():

	global profile, ip
	ip = ip + 1
	profile = profile + 1
	
	url = "https://ipinfo.io/json"
	response = urlopen(url)
	data = json.load(response)
	#print("addr %s: %s\n" % (addr, data))
	f = open(ruta + "ip"+ str(ip) + ".txt", "w")
	f.write(str(data))
	f.close()

	key = Fernet.generate_key()
	f = open(ruta + "key" + str(profile) + ".txt", "w")
	f.write(str(key))
	f.close()
	return key 

if __name__ == '__main__':
	app.run(host='0.0.0.0')