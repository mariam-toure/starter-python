import re 

nombre = int(input("entrez un nombre:"))
# ouverture du fichier en lecture
f = open("data.txt", "r")
# tri du fichier 
regex = re.findall(r"/b[a-zA-Z]{%d}/b" % (nombre), f.read())
#Nombres de mots triés
print("il y a {} mot de {} caractères".format(len(regex), nombre))