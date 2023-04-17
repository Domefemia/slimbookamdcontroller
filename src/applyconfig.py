#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#This file just reads and applies ryzen configuaration info from .config
import os
import sys
import gi
import subprocess
import configparser
import utils
from time import sleep

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

USER_NAME = utils.get_user()
HOMEDIR = subprocess.getoutput(f"echo ~{USER_NAME}")

config_file = f'{HOMEDIR}/.config/slimbookamdcontroller/slimbookamdcontroller.conf'
print(f"Reading {config_file}")
config = configparser.ConfigParser()


if config.read(config_file):
    print("File detected!\n")
else:
    print("File not detected!\n")

call=''      

#READING VARIABLES
modo_actual = config.get('CONFIGURATION', 'mode')
print(f"Current mode: {modo_actual}")
parameters = config.get('USER-CPU', 'cpu-parameters').split('/')
print(f"Parameters: {str(parameters)}")

mode = -1

if modo_actual == "low":
    mode = 0    
    
if modo_actual == "medium":
    mode = 1

if modo_actual == "high":
    mode = 2

try:
    set_parameters = parameters[mode].split('-')
    sleep(3)
    print(f'Setting {modo_actual} to : {set_parameters[0]} {set_parameters[1]} {set_parameters[2]}' + '.\n')
    call = os.system('sudo /usr/share/slimbookamdcontroller/ryzenadj --tctl-temp=95'+' --slow-limit='+set_parameters[0]+' --stapm-limit='+set_parameters[1]+' --fast-limit='+set_parameters[2]+'')

    print('--------------------------------------------')
    print(f'Exit: {str(call)}')
    print('--------------------------------------------')

    #print(str('sys.exit('+str(call)+')'))
    if call != 0:
        (sys.exit(1))

except Exception as e:
    print(f'ERROR: {e}')
       