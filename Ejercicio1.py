####Ejercicio 1####
def clasificar(numero):
    return numero%2==0

clasificar2 = lambda numero: numero%2==0

print(clasificar(100))
print(clasificar2(100))

if (clasificar2(100)):
    print("Es multiplo")
else:
    print("No es multiplo")