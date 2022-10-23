var1 = int(input("Valeur 1 : "))
var2 = int(input("Valeur 2 : "))

for var1 in range(var1+1,var2):
    print(var1)
    
for var2 in reversed(range(var2+1,var1)):
    print(var2)

if var1 == var2:
    print("Valeur egales")