import time  
from datetime import datetime  
import threading 

def heure_locale(mode_affichage):
    while True:
        if mode_affichage == "No":
            current_time = time.strftime("%H:%M:%S", time.localtime())
        else:
            current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Il est actuellement : {current_time}", end="\r")
        time.sleep(1)

def afficher_heure(heure_tuple, mode_affichage): 
    heures, minutes, secondes = heure_tuple
    while True:
        if mode_affichage == "No":
            print(f"Il est actuellement : {heures:02d}:{minutes:02d}:{secondes:02d}", end="\r")
        else:
            period = "AM" if heures < 12 else "PM"
            heures %= 12
            if heures == 0:
                heures = 12
            print(f"Il est actuellement : {heures:02d}:{minutes:02d}:{secondes:02d} {period}", end="\r")
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

def regler_alarme(heure_alarme):
    def alarme():
        while True:
            t = time.localtime()
            heure_locale = (t.tm_hour, t.tm_min, t.tm_sec)
            if heure_locale >= heure_alarme:
                print("\n==> ! ALARME ! <==")
                break
            time.sleep(1) 
    thread_alarme = threading.Thread(target=alarme)
    thread_alarme.start()    

regler_heure = input("Souhaitez-vous afficher l'heure locale ou définir une heure ? (Yes/No): ")
alarme = input("Souhaitez-vous définir une alarme ? (Yes/No): ")
mode_affichage = input("Souhaitez-vous l'heure au format 12 ou 24 ? (Yes/No): ")

if regler_heure == "Yes":
    if alarme == "Yes":
        heure_alarme = tuple(map(int, input("Entrez l'heure de l'alarme (hh mm ss): ").split()))
        regler_alarme(heure_alarme)
    heure_locale(mode_affichage)
else:
    if alarme == "Yes":
        heure_alarme = tuple(map(int, input("Entrez l'heure de l'alarme (hh mm ss): ").split()))
        regler_alarme(heure_alarme)
    heure_tuple = tuple(map(int, input("Entrez l'heure désirée (hh mm ss): ").split()))
    afficher_heure(heure_tuple, mode_affichage)
