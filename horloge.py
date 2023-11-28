# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 2023

@author: Mazard Pierre

#horloge
"""

#Importation de fonctions externes (librairies) :

import time    
    
#Définition locale de fonctions : 

    

#Déclaration des variables : 


#Corps principal du programme : 



print (""" 
           Voici l'heure locale au format hh:mm:ss
""")    
while True:
    t = time.localtime()
    current_time = time.strftime("%Hh:%Mm:%Ss", t)
    print("""Il est actuellement :""", current_time, end="\r")
    #Actualisation à chaque secondes 
    time.sleep(1)
 