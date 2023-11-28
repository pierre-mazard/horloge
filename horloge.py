# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 2023

@author: Mazard Pierre

#horloge
"""

#Importation de fonctions externes (librairies) :

import time    
    
#Définition locale de fonctions : 

def afficher_heure(heure_tuple): 
    heures, minutes, secondes = heure_tuple
    print (""" 

 Voici l'heure définie au format hh:mm:ss
         
         """)  
    while True:
        print(f"""              Il est actuellement : {heures:02d}h:{minutes:02d}m:{secondes:02d}s""", end="\r")
        time.sleep(1)
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
        if heures == 24:
            heures = 0
    
#Déclaration des variables : 


#Corps principal du programme : 

regler_heure = input("""
Souhaitez-vous afficher l'heure locale ou définir une heure ?

=>  Entrez Y pour afficher l'heure locale.

=>  Entrez N pour définir une heure.                     

====> : """)

#Affichage de l'heure locale au format hh:mm:ss      
if regler_heure == "Y":
    print (""" 

Voici l'heure locale au format hh:mm:ss
        
        """)  
    while True:
        t = time.localtime()
        current_time = time.strftime("%Hh:%Mm:%Ss", t)
        print("""              Il est actuellement :""", current_time, end="\r")
        #Actualisation à chaque secondes 
        time.sleep(1)
#Définir l'heure au format hh:mm:ss
if regler_heure == "N":
    #appel fonction
   afficher_heure((int(input("""Veuillez entrez une valeur pour l'heure :
=> """)), int(input("""Veuillez entrer une valeur pour les minutes :
=> """)), int(input("""Veuillez entrer une valeur pour les secondes :
=> """))))
   