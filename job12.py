import re 

count = 0
fichier = open("data.txt", "r")
texte = fichier.read()

mots = re.findall('[a-zA-Z]+', texte)

nombre_de_mots = len(mots)

fichier.close()

print(nombre_de_mots)