#Créez un script job06.py
#Lorsque l’utilisateur va lancer le script, un prompteur devra s’afficher “>”, et le
#programme devra attendre un input.
#Si l’input entré est “Bonjour”, le programme devra répondre “Bonjour à toi”
#Si l’input entré est “Au revoir”, le programme devra quitter
while True:
    
    bjr = str(input(">"))

    if bjr == "Bonjour":
        print("Bonjour à toi")
    elif  bjr == "Au revoir":
        quit()                # on peut utiliser egalement exit() 
    else:
        print(bjr)