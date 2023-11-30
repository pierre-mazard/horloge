# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 2023

@author: Mazard Pierre

#horloge
"""

#                      Importation de fonctions externes (librairies) :

import time  
from datetime import datetime  
import threading    
#                          Définition locale de fonctions : 
        
                                    #Heure Locale
def heure_locale():
    if mode_affichage == "No":
        print (""" 
    
    Voici l'heure locale au format hh:mm:ss
            
            """)  
        while True:
            t = time.localtime()
            current_time = time.strftime("%Hh:%Mm:%Ss", t)
            print("""              Il est actuellement :""", current_time, end="\r")
            #Actualisation à chaque secondes 
            time.sleep(1)
    if mode_affichage == "Yes":
        print ("""
               
Voici l'heure définie au format hh:mm:ss AM/PM

""")  

        while True:
            now = datetime.now()
            current_time = now.strftime("%I:%M:%S %p")
            print(f"""             Il est actuellement : {current_time}""", end="\r")
            time.sleep(1)
                                    #Heure définie
def afficher_heure(heure_tuple): 
    heures, minutes, secondes = heure_tuple
    if mode_affichage == "No":
        print (""" 
    
    Voici l'heure définie au format hh:mm:ss
             
             """)  
        while True:
            print(f"""             Il est actuellement : {heures:02d}h:{minutes:02d}m:{secondes:02d}s""", end="\r")
            #Actualisation à chaque secondes
            time.sleep(1)
            secondes += 1
            if secondes >= 60:
                secondes = 0
                minutes += 1
            if minutes >= 60:
                minutes = 0
                heures += 1
            if heures >= 24:
                heures = 0
        
    if mode_affichage == "Yes":
           print (""" 
    
       Voici l'heure définie au format hh:mm:ss AM/PM
                
                """)  
           while True and heures <= 12 :
               print(f"""             Il est actuellement : {heures:02d}h:{minutes:02d}m:{secondes:02d}s AM""", end="\r")
               #Actualisation à chaque secondes
               time.sleep(1)
               secondes += 1
               if secondes >= 60:
                   secondes = 0
                   minutes += 1
               if minutes >= 60:
                   minutes = 0
                   heures += 1
               if heures >= 12:
                   heures = 0                            
           while True and heures >= 12 :
                print(f"""             Il est actuellement : {heures:02d}h:{minutes:02d}m:{secondes:02d}s PM""", end="\r")
                #Actualisation à chaque secondes
                time.sleep(1)
                secondes += 1
                if secondes >= 60:
                    secondes = 0
                    minutes += 1
                if minutes >= 60:
                    minutes = 0
                    heures += 1
                if heures >= 12:
                    heures = 0                                 #Alarme
                                    
def regler_alarme(heure_alarme):
    def alarme():
        while regler_heure == "Yes":
            t = time.localtime()
            heure_locale = (t.tm_hour, t.tm_min, t.tm_sec)
            if heure_locale >= heure_alarme:
                print("""
                      
                      ==> ! ALARME ! <==
                      """)
                break
            time.sleep(1) 
    # Crée un nouveau thread pour exécuter la fonction d'alarme
    thread_alarme = threading.Thread(target=alarme)
    # Démarre le thread
    thread_alarme.start()    

#                             Corps principal du programme : 
regler_heure = input("""
Souhaitez-vous afficher l'heure locale ou définir une heure ?

=>  Entrez 'Yes' pour afficher l'heure locale.

=>  Entrez 'No' pour définir une heure.                     

====> : """)

alarme = input("""
Souhaitez-vous définir une alarme ?

=>  Entrez 'Yes' pour définir une alarme.

=>  Entrez 'No' pour passer cette étape.                     

====> : """)

mode_affichage = input(f"""
Souhaitez-vous l'heure au format 12 ou 24 ?

=>  Entrez 'Yes' pour un format 12h.

=>  Entrez 'No' pour un format 24h.                     

====> : """)

#Affichage de l'heure locale au format hh:mm:ss avec alarme
if regler_heure == "Yes" and alarme == "Yes":
    
    print ("""
    Entrez les paramètres afin de définir l'heure de l'alarme :""")
        #appel fonction
    regler_alarme((int(input("""
     Veuillez entrer une valeur pour l'heure :
     => """)), int(input("""
     Veuillez entrer une valeur pour les minutes :
     => """)), int(input("""
     Veuillez entrer une valeur pour les secondes :
     => """))))   
    #appel fonction
    heure_locale()
    
#Affichage de l'heure locale au format hh:mm:ss sans alarme
if regler_heure == "Yes" and alarme == "No":   
    #appel fonction
    heure_locale()    

#Définir l'heure au format hh:mm:ss avec alarme 
if regler_heure == "No" and alarme == "Yes":
    #appel fonction
   print ("""
    Entrez les paramètres afin de définir l'heure de l'alarme :""")
        #appel fonction
   regler_alarme((int(input("""
     Veuillez entrer une valeur pour l'heure :
     => """)), int(input("""
     Veuillez entrer une valeur pour les minutes :
     => """)), int(input("""
     Veuillez entrer une valeur pour les secondes :
     => """))))
   print ("""
Entrez les paramètres afin de définir l'heure désirée :""")  
   afficher_heure((int(input("""
Veuillez entrez une valeur pour l'heure :
=> """)), int(input("""
Veuillez entrer une valeur pour les minutes :
=> """)), int(input("""
Veuillez entrer une valeur pour les secondes :
=> """))))
   

#Définir l'heure au format hh:mm:ss sans alarme
if regler_heure == "No" and alarme == "No":
   print ("""
Entrez les paramètres afin de définir l'heure désirée :""")
    #appel fonction
   afficher_heure((int(input("""
Veuillez entrez une valeur pour l'heure :
=> """)), int(input("""
Veuillez entrer une valeur pour les minutes :
=> """)), int(input("""
Veuillez entrer une valeur pour les secondes :
=> """))))
    

