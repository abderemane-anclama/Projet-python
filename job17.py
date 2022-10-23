'''Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.'''

def myfunction(*paramIndefini):
    
    myList = []
    
    for x in paramIndefini:
        if isinstance(x,(int)):
            myList.append(x)
            
        else:
            print("Attention un des parametres n'est pas numerique")
    for i in myList:
        if i % 2 == 0:
            print(i)

myfunction(2, 4, 3, -1, 6, 8)