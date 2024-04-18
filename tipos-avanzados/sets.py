set1 = {1, 2, 2, 2, 3, 4, 5, 6}

set2 = [3, 3, 4, 5]

segundo = set(set2)
print(segundo)

print(set1 | segundo)  # une los dos set a traves del operador |
print(set1 & segundo)  # Imprime unicamente los valores que coinciden
# Imprime unicamente los datos que solo se encuentran en el set que se indica a la izquierda
print(set1-segundo)
# Imprime los unicamente los valores que solo estan en uno de los dos set
print(set1 ^ segundo)
