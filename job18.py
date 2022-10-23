'''Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Trier par ordre croissant la liste à l’aide de la fonction sort
- Afficher la liste dans un terminal'''

def myfunction(*param_indefini):
    myList =[]
    
    for x in param_indefini:
        if isinstance(x, (int)):
            myList.append(x)
            myList.sort()
        else:
            print("une des parametre n'est pas un entier")

    print(myList)

myfunction(3, 6, 7, 9, 0, 3, 2, -2, -1)