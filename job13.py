var = int(input("ecrivez un entier naturell Madame, Monsieur lecteur : "))

with open("data.txt", "r") as file:
    lignes = file.read()

liste = lignes.split()

nb_words = 0

for elt in liste:
    #print(elt)
   
    #print(lignes)
    #for elt in liste:
    if len(elt) == var:
        nb_words = nb_words + 1 
print(nb_words)