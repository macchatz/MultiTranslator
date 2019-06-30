#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
import threading
import os,sys
import os.path
import json
from crontab import CronTab
import subprocess
import requests
import selenium
import tldextract
from selenium import webdriver
import unittest 
import contextlib
import selenium.webdriver as webdriver
import numpy as np
import Gnuplot
from shutil import copyfile
import hashlib
import cPickle as pickle
import socket
import time
from random import randint
import robotparser
#This translator gets multiple words, translates them in 92 languages, and stores them in a file : LastResort.txt 

#You shoud put the words you want to translate in  a file Called Checks.txt (Words should be sorted line by line)

file = open("LastResort.txt","w+")
file.close()
#make the profile
profile = webdriver.FirefoxProfile()

print "Proxy setted,profile ready!"
options = Options()
# make the search headless
# options.add_argument("--headless")
elista = []
childs = []
childs2 = []
checko = []
ulili = []
n = []
i=0
driver = webdriver.Firefox(firefox_profile = profile,firefox_options=options)
driver.set_page_load_timeout(randint(35, 45))
j=0
#Using translatr
driver.get("https://translatr.varunmalhotra.xyz")
with open("Checks.txt","r") as file:
	for line in file:
		for l in line.split("."):
			i+=1
			ulili[:]=[]
			elista[:] = []
			childs[:] = []

			print l.strip()
			childs = driver.find_elements_by_id('text')
			print len(childs)
			childs[0].click()
			childs[0].send_keys(l.strip())
			if i == 1:
				clicking = driver.find_element_by_class_name('ng-binding')
				clicking.click()
				driver.implicitly_wait(30)
			#submit click
			checko[:] = []
			checko = driver.find_elements_by_xpath("//button")
			for cc in checko:
				try:
					cc.click()
					break
				except:
					continue
			print "How many :",len(checko)
			driver.implicitly_wait(30)
			
			
			elista = driver.find_elements_by_id('output')
			print "El lista is:",len(elista)
			driver.implicitly_wait(5)
			with open("LastResort.txt","a+") as file:
				for e in elista:
					try:
						childs2[:] = []
						childs2 = e.find_elements_by_xpath(".//*")
						for c in childs2:
							try:
								if c.text:
									
									file.write((c.text).encode('utf-8'))
									
							except:
								continue
						file.write("\n")
					except:
						continue
			print "El numero esta: ",i
			childs[0].clear()
			with open("LastResort.txt","a+") as file:
				file.write("\n-----------------------------\n\n")
			

driver.quit()

print "Begining the clearence"
