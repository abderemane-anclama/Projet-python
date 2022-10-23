#Écrire un programme rectangle.py qui attend deux inputs : la largeur puis la hauteur.
#Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
#- des “|” pour dessiner les côtés droite et gauche
#- des “-” pour dessiner le haut et le bas
#- des espaces pour remplir le rectangle

#Longueur L = 10
# l = largeur 5

l = 5 
coté = "|"
espace = "---"
for i in range(l):
    if i == 0 or i == l-1:
        espace = "---"
    else:
        espace = "   "
    print(coté + espace * l + coté)


