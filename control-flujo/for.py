# for numero in range(5):
#     print(numero, numero * " Hola Mundo ")

buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print(f"encontrado {buscar} ")
        break


for numero in range(2):
    print(numero)
    if numero == buscar:
        print(f"encontrado {buscar} ")
        break
else:
    print("No encontrado :(")
