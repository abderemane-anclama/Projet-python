'''Créer un programme job19.py. Le programme devra contenir une seule fonction qui
prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Trier par ordre croissant la liste sans la fonction sort 
- Afficher la liste dans un terminal'''



def myfunction(*param_indefini):
    myList =[]
    
    for x in param_indefini:
        if isinstance(x, (int)):
            myList.append(x)
            
        else:
            print("une des parametre n'est pas un entier")

    permutation = True
    passage = 0

    while permutation == True:

        permutation = False
        passage = passage + 1

        for y in range(0, len(myList) - passage):
            if myList[y] > myList[y + 1]:
                permutation = True

                myList[y], myList[y + 1] = \
                myList[y + 1], myList[y]
        
    print(myList)

myfunction(3, 6, 7, 9, 0, 2, -1, -3, 6)


















