#Écrire un programme qui parcourt les nombres entiers de 1 à 100. 
# Pour les multiples de trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
#pour les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".

for i in range(1,100):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)