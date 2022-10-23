#Écrire un programme job10.py qui demande à l’utilisateur d’entrer un texte.
#le programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”.
#Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le
#terminal.

texte = str(input("ecrivez un texte monsieur ANCLAMA : "))

file = open("output.txt","w")
file.write(texte)
file.close

file = open("output.txt", "r")
print(file.read())
file.close
