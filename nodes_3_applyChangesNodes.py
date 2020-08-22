# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:50:33 2020

@author: jmg
"""

import osmapi

def translatePlaceName(currentSearchToponyme, currentBretonEquivalent, idsToUpdate, osm_api):
    
    currentChangeSetComment = u"Add name:br tag to way: " + currentSearchToponyme
    
    # Update using osmapi
    for nodeIndex in idsToUpdate:
        
        node = osm_api.NodeGet(nodeIndex)
            
        # Supplementary check
        if node["tag"]["name"] == currentSearchToponyme:
            
            if "name:br" not in node["tag"].keys():
                
                if 'place' in node["tag"].keys():
                
                    if node["tag"]["place"] == "isolated_dwelling" or node["tag"]["place"] == "hamlet" or node["tag"]["place"] == "locality" or node["tag"]["place"] == "neighbourhood":
            
                        osm_api.ChangesetCreate({u"comment": currentChangeSetComment})        
                
                        # Dictionary modification :
                        node["tag"]["name:br"] = currentBretonEquivalent
                        node["tag"]["source:name:br"] = "proper translation"
                
                        osm_api.NodeUpdate(node)
                        
                        print(nodeIndex)
                        print(node["tag"]["name"])
                        print(node["tag"]["name:br"])
                        print("--")
                
                        osm_api.ChangesetClose()


# Programme principal
# -------------------

# User your OSM credentials
osm_api = osmapi.OsmApi(api = "https://api.openstreetmap.org", username = "XXX", password = "XXX")

# Specify the location of the file obtained with nodes_2_getSortedNodesTXT_BZH.py
fichierNomsPoints = r"D:\myFolder\indexFileNodes_20200822.txt"
fileHandle = open(fichierNomsPoints, 'r', encoding = 'utf-8')

# Specify starting index
indexStart = 0

counter = 0

while True:
    
    listeIDs = []
    
    currentLine = fileHandle.readline()
    
    if counter < indexStart:
        pass
    else:
        splitLine = currentLine.split(";")
        print("> " + splitLine[0])
        currentSearchToponyme = splitLine[0]
        
        if splitLine[2] == "???":
            
            proposedTranslation = input("Traduction proposée : (0 pour passer) ")
            
            if proposedTranslation == "STOP":
                break
            
            elif proposedTranslation == "0":
                continue
            
            else:
                listePoints = splitLine[4]
                listePointsSplit = listePoints.split(",")
                
                for elem in listePointsSplit:
                    listeIDs.append(int(elem))
                    
                translatePlaceName(currentSearchToponyme, proposedTranslation, listeIDs, osm_api)
                
        else:
            
            alreadyPresentTranslations = splitLine[2]
            alreadyPresentTranslationsSplit = alreadyPresentTranslations.split(",")
            dictAlreadyPresentTranslations = {}
            
            counterTranslations = 1
            print("Propositions : ")
            
            for transIndex in alreadyPresentTranslationsSplit:
                
                dictAlreadyPresentTranslations[str(counterTranslations)] = alreadyPresentTranslationsSplit[counterTranslations - 1]
                print(str(counterTranslations) + " : " + alreadyPresentTranslationsSplit[counterTranslations - 1])
                
                counterTranslations += 1
                
            proposedTranslation = input("Traduction proposée : (0 pour passer, numéro ou entrée nouvelle) ")
            
            if proposedTranslation == "STOP":
                break
            
            elif proposedTranslation == "0":
                continue
            
            else:

                if splitLine[5] == "0":
                    pass
                
                else:
                    
                    listePoints = splitLine[6]
                    listePointsSplit = listePoints.split(",")
                                    
                    for elem in listePointsSplit:
                        listeIDs.append(int(elem))
                        
                    if proposedTranslation in dictAlreadyPresentTranslations.keys():
                        translatePlaceName(currentSearchToponyme, dictAlreadyPresentTranslations[proposedTranslation], listeIDs, osm_api)
                        
                    else:
                        translatePlaceName(currentSearchToponyme, proposedTranslation, listeIDs, osm_api)
            
    counter += 1
