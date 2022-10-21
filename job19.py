
def mySort(myList):
    permutation = True
    passage = 0
    while permutation == True:

        permutation = False
        passage = + 1

        for en_cours in range(0, len(myList) - passage):
            if myList[en_cours] > myList[en_cours + 1]:
                permutation = True 
                # on echange les deux elements
                myList[en_cours], myList[en_cours + 1] = \
                    myList[en_cours + 1],myList[en_cours]

        print (myList)


mySort([1, 5, 18, 9, 14, 23, 2])