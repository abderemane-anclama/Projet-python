'''Créer un programme job21.py. Reprenez l’exercice 19, mais modifiez le de façon à
utiliser deux fonctions :
- Une fonction mySort, qui prendra en paramètre une liste. Elle retourne une liste
avec les valeurs de celle passée en paramètre, triés par ordre croissant.
- Une fonction myDisplay qui prendra en paramètre une liste. Elle affichera dans le
terminal le contenu de cette liste.'''

def mySort(list):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False 
        passage = passage + 1
        for y in range(0, len(list) - passage):
            if list[y] > list[y + 1]:
                permutation = True
                list[y], list[y + 1] = \
                list[y + 1], list[y]
    return list

def myDisplay(liste):
    print(liste)


myDisplay(mySort([10, 9, 5, 1, 2, -1, -2]))