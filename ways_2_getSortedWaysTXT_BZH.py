# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:50:33 2020

@author: jmg
"""

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# consideredFolder refers to the folder containing the files obtained with ways_1_getWaysOSM_BZH.py
consideredFolder = r"D:\myFolder"
date = "20200822"

# Specify output folder
pathIndexFile = r"D:\myFolder\indexFileNodes_" + date + ".txt"

departements = ["22", "29", "35", "44", "56"]

listFileNodesBZH = []

for iIndex in departements:
    listFileNodesBZH.append(consideredFolder + r"\xmlWays" + iIndex + "_" + date + ".osm")

dictionnaireNomsDeLieux = {}

for departementIndex in listFileNodesBZH:

    print(departementIndex)
    tree = ET.parse(departementIndex)
    root = tree.getroot()
    
    for iIndex in root[2:]:
        
#        print(iIndex.attrib['id'])

        flagNameFound = False
        flagNameBRFound = False
                    
        for jIndex in iIndex:
            
            if 'k' in jIndex.attrib.keys():
    
                if jIndex.attrib['k'] == "name":
                    
                    flagNameFound = True
                    nomFR = jIndex.attrib['v']
                    
                    if jIndex.attrib['v'] not in dictionnaireNomsDeLieux.keys():
                        
                        dictionnaireNomsDeLieux[jIndex.attrib['v']] = {}
                        dictionnaireNomsDeLieux[jIndex.attrib['v']]['nboc'] = 1
                        dictionnaireNomsDeLieux[jIndex.attrib['v']]['listBZH'] = []
                        dictionnaireNomsDeLieux[jIndex.attrib['v']]['listID_notTranslated'] = []
                        dictionnaireNomsDeLieux[jIndex.attrib['v']]['listID_alreadyTranslated'] = []
                                                
                    else:
                    
                        dictionnaireNomsDeLieux[jIndex.attrib['v']]['nboc'] += 1                        
            
                if jIndex.attrib['k'] == "name:br":
                    
                    flagNameBRFound = True                    
                    
                    dictionnaireNomsDeLieux[nomFR]['listID_alreadyTranslated'].append(iIndex.attrib['id'])
                                                            
                    if jIndex.attrib['v'] not in dictionnaireNomsDeLieux[nomFR]['listBZH']:
                    
                        dictionnaireNomsDeLieux[nomFR]['listBZH'].append(jIndex.attrib['v'])
                        
        if (flagNameFound == True) and (flagNameBRFound == False):
                    
            dictionnaireNomsDeLieux[nomFR]['listID_notTranslated'].append(iIndex.attrib['id'])
                                    
#        print("---")
        
# Sort dictionary
sortedList = sorted(dictionnaireNomsDeLieux.items(), key=lambda t: t[1]['nboc'], reverse = True)        

fileHandle = open(pathIndexFile, 'w', encoding="utf-8")

for lineIndex in sortedList:
    
    currentStringToWrite = ""
    
    currentStringToWrite += lineIndex[0]
    currentStringToWrite += ";"
    currentStringToWrite += str(lineIndex[1]['nboc'])
    currentStringToWrite += ";"

    if len(lineIndex[1]['listBZH']) == 0:
        
        currentStringToWrite += "???"
        
        currentStringToWrite += (";" + str(len(lineIndex[1]['listID_notTranslated'])) + ";")
       
        for counter in range(len(lineIndex[1]['listID_notTranslated'])):
            
            if counter == 0:

                currentStringToWrite += lineIndex[1]['listID_notTranslated'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listID_notTranslated'][counter])        
        
    elif len(lineIndex[1]['listBZH']) == 1:
        
        currentStringToWrite += lineIndex[1]['listBZH'][0]
        
        currentStringToWrite += (";" + str(len(lineIndex[1]['listID_alreadyTranslated'])) + ";")
       
        for counter in range(len(lineIndex[1]['listID_alreadyTranslated'])):
            
            if counter == 0:

                currentStringToWrite += lineIndex[1]['listID_alreadyTranslated'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listID_alreadyTranslated'][counter])                
        
        currentStringToWrite += (";" + str(len(lineIndex[1]['listID_notTranslated'])) + ";")
       
        for counter in range(len(lineIndex[1]['listID_notTranslated'])):
            
            if counter == 0:

                currentStringToWrite += lineIndex[1]['listID_notTranslated'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listID_notTranslated'][counter])        

    else:
                                            
        for counter in range(len(lineIndex[1]['listBZH'])):
        
            if counter == 0:
                
                currentStringToWrite += lineIndex[1]['listBZH'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listBZH'][counter])
        
        currentStringToWrite += (";" + str(len(lineIndex[1]['listID_alreadyTranslated'])) + ";")
       
        for counter in range(len(lineIndex[1]['listID_alreadyTranslated'])):
            
            if counter == 0:

                currentStringToWrite += lineIndex[1]['listID_alreadyTranslated'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listID_alreadyTranslated'][counter])                
        
        currentStringToWrite += (";" + str(len(lineIndex[1]['listID_notTranslated'])) + ";")
       
        for counter in range(len(lineIndex[1]['listID_notTranslated'])):
            
            if counter == 0:

                currentStringToWrite += lineIndex[1]['listID_notTranslated'][counter]
                
            else:
                
                currentStringToWrite += ("," + lineIndex[1]['listID_notTranslated'][counter])         
        
    currentStringToWrite += "\n"
    
    fileHandle.write(currentStringToWrite)
        
fileHandle.close()