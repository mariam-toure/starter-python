def myfunction( *params ):
    mylist = []

    for param in params:
        if isinstance(param,(int)):
            mylist.append(param)
            mylist.sort()
        else:
            print("attention un des paramétres n'est pas numérique")

    print(mylist)



        
            
            


myfunction(6, 3, 8, 15, 19, 49, 34)