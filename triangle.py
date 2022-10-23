#Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
#‘\’ et des ‘/’
#en fonction de l’input entré, qui représentera la hauteur.
#Exemple si l’input entré est 5

H = 10

base = "__"
pente1 = "/"
pente2 = "\\"

for i in range(H):
    print((H - i) * " " + pente1 + ((i * 2) * " ") + pente2)
    if i == H - 1:
        print(pente1 + base * H + pente2)
   
    
