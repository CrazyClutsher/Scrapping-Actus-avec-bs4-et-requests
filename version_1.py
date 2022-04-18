from bs4 import BeautifulSoup
import requests
import logging

# On affecte l'URL du site web Le Monde à la variable url_1
url_1 = "https://www.lemonde.fr/" 
# On affecte l'URL du site web Les Échos à la variable url_2
url_2 = "https://www.lesechos.fr/" 

# On affecte à la variable reponse_1 la fonction get(), qui permet dans ce cas-ci de chercher sur un navigateur automatiquement le site web Le Monde
reponse_1 = requests.get(url_1) 
# On affecte à la variable reponse_2 la fonction get(), qui permet dans ce cas-ci de chercher sur un navigateur automatiquement le site web Les Échos
reponse_2 = requests.get(url_2) 
# On affecte à la variable soup_1 la fonction BeautifulSoup() avec pour argument secondaire un parsing du code HTML de la page du site web Le Monde
soup_1 = BeautifulSoup(reponse_1.text, "html.parser")
# On affecte à la variable soup_2 la fonction BeautifulSoup() avec pour argument secondaire un parsing du code HTML de la page du site web Les Échos
soup_2 = BeautifulSoup(reponse_2.text, "html.parser") 

 # On affecte à la variable Html_1 la fonction findAll(), qui va chercher une balise html en partciulier, ici <body>, dans le parsing du code HTML de la page du site web Le Monde
Html_1 = soup_1.findAll("body")
# On affecte à la variable Html_2 la fonction findAll(), qui va chercher une balise html en partciulier, ici <body>, dans le parsing du code HTML de la page du site web Les Échos
Html_2 = soup_2.findAll("body") 

# On affecte à la variable HTml_1 le premier élément de liste de la variable Html_1, c'est-à-dire la première balise <body>, qui est ouvrante, afin de prendre tous les éléments qui se trouvent entre <body> et </body> dans le code HTML du site Le Monde
HTml_1 = Html_1[0] 
# On affecte à la variable HTml_2 le premier élément de liste de la variable Html_2, c'est-à-dire la première balise <body>, qui est ouvrante, afin de prendre tous les éléments qui se trouvent entre <body> et </body> dans le code HTML du site Les Échos
HTml_2 = Html_2[0] 


# On affiche le contenu textuel qui se trouve entre les balises <main> et </main>, qui se trouvent dans entre les balises <body> et </body> du code HTML des sites web respectifs Le Monde et Les Échos
print("RÉSUMÉ DE L'ACTUALITÉ DU JOUR  SELON LE MONDE: \n" + HTml_1.main.text + "\n\n" + "RÉSUMÉ DE L'ACTUALITÉ DU JOUR SELON LES ÉCHOS : \n\t" + HTml_2.main.text) 
