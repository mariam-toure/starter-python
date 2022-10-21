def mySort(liste):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0,len(liste) - passage):
            if liste[en_cours] > liste[en_cours + 1]:
                permutation = True
                # on echange les deux elements 
                liste[en_cours], liste[en_cours + 1] = \
                liste[en_cours + 1], liste[en_cours]
    return liste


def myDisplay(liste2):
    print(liste2)


myDisplay(mySort([18, 23, 52, 16, 45]))