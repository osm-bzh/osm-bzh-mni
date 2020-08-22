# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:50:33 2020

@author: jmg
"""

import urllib.parse
import urllib.request

# Specify destination folder for osm files containing all BZH nodes 
storageFolder = r"D:\myFolder"

# Specify date
date = "20200822"

location = "Morbihan"
pathFile = storageFolder + r"\xmlNodes56_" + date + r".osm"
myURL = 'https://lz4.overpass-api.de/api/interpreter?data=[timeout:3600];area[%22name%22=%22' + urllib.parse.quote(location) + '%22]->.boundaryarea;(node(area.boundaryarea)["place"="isolated_dwelling"];node(area.boundaryarea)["place"="hamlet"];node(area.boundaryarea)["place"="locality"];node(area.boundaryarea)["place"="neighbourhood"];node(area.boundaryarea)["place"="village"];);out%20center%20tags;'	
testfile = urllib.request.urlretrieve(myURL, pathFile)

location = "Finistère"
pathFile = storageFolder + r"\xmlNodes29_" + date + r".osm"
myURL = 'https://lz4.overpass-api.de/api/interpreter?data=[timeout:3600];area[%22name%22=%22' + urllib.parse.quote(location) + '%22]->.boundaryarea;(node(area.boundaryarea)["place"="isolated_dwelling"];node(area.boundaryarea)["place"="hamlet"];node(area.boundaryarea)["place"="locality"];node(area.boundaryarea)["place"="neighbourhood"];node(area.boundaryarea)["place"="village"];);out%20center%20tags;'
testfile = urllib.request.urlretrieve(myURL, pathFile)

location = "Côtes-d'Armor"
pathFile = storageFolder + r"\xmlNodes22_" + date + r".osm"
myURL = 'https://z.overpass-api.de/api/interpreter?data=[timeout:3600];area[%22name%22=%22' + urllib.parse.quote(location) + '%22]->.boundaryarea;(node(area.boundaryarea)["place"="isolated_dwelling"];node(area.boundaryarea)["place"="hamlet"];node(area.boundaryarea)["place"="locality"];node(area.boundaryarea)["place"="neighbourhood"];node(area.boundaryarea)["place"="village"];);out%20center%20tags;'
testfile = urllib.request.urlretrieve(myURL, pathFile)

location = "Ille-et-Vilaine"
pathFile = storageFolder + r"\xmlNodes35_" + date + r".osm"
myURL = 'https://z.overpass-api.de/api/interpreter?data=[timeout:3600];area[%22name%22=%22' + urllib.parse.quote(location) + '%22]->.boundaryarea;(node(area.boundaryarea)["place"="isolated_dwelling"];node(area.boundaryarea)["place"="hamlet"];node(area.boundaryarea)["place"="locality"];node(area.boundaryarea)["place"="neighbourhood"];node(area.boundaryarea)["place"="village"];);out%20center%20tags;'	
testfile = urllib.request.urlretrieve(myURL, pathFile)

location = "Loire-Atlantique"
pathFile = storageFolder + r"\xmlNodes44_" + date + r".osm"
myURL = 'https://overpass.nchc.org.tw/api/interpreter?data=[timeout:3600];area[%22name%22=%22' + urllib.parse.quote(location) + '%22]->.boundaryarea;(node(area.boundaryarea)["place"="isolated_dwelling"];node(area.boundaryarea)["place"="hamlet"];node(area.boundaryarea)["place"="locality"];node(area.boundaryarea)["place"="neighbourhood"];node(area.boundaryarea)["place"="village"];);out%20center%20tags;'
testfile = urllib.request.urlretrieve(myURL, pathFile)