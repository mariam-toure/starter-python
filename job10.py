texte = input("texte.:")
fichier = open("output.txt","w")
fichier.write(texte)
fichier.close()

fichier = open("output.txt")
print(fichier.read())
fichier.close()