numeros = [0, 1, 2]
primero, segundo, tercero = numeros
print(primero, segundo, tercero)

numeros = [1, 3, 4]

primerNumero, *siguientes = numeros

print(primerNumero)
print(siguientes)

numeros = [1, 3, 4, 5, 6, 7, 8, 9]

n1, n2, *otros = numeros
print(n1, n2, otros)


n1, *otros, ultimo = numeros
print(n1, otros, ultimo)
