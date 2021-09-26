"""
    Exemple de code permettant de lancer une radio, ici RTL2. 
"""

from frdomoticz import lib # Import de la librairie

code = 123456789 # Ajout du code de la télécommande

lib.init(code) # Initialisation du player sur le premier menu
lib.radio(code) # Lancement du menu radio
lib.button(code,"down",4) # Appui sur la touche "Bas" 4 fois
lib.button(code,"right") #  Appui sur la touche "Droite"
lib.button(code,"down",14) #  Appui sur la touche "Bas" 14 fois
lib.button(code,"right") #  Appui sur la touche "Droite"
lib.button(code,"down",4) #  Appui sur la touche "Bas" 4 fois
lib.button(code,"right",3) #  Appui sur la touche "Droite" 3 fois
lib.button(code,"ok") #  Appui sur la touche "Ok"