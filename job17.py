def myfunction( *params ):
    mylist = []

    for param in params:
        if isinstance(param,(int)):
            mylist.append(param)
        else: 
            print("attention un des paramétres n'est pas numérique")

            for element in mylist:
                if element % 2 == 0:
                    print (element)


myfunction(4,7,10,5,22,"sacsedrt",2)