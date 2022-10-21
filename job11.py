count = 0

fichier = open("domains.xml", "r")
for ligne in fichier:
    if 'domain' in ligne:
        count += 1

print(count)

