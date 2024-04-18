lista = [1, 2, 3, 4, 5]

print(*lista)

lista2 = [6, 7]

lista3 = [*lista, *lista2]
print(lista3)


usuarios = {"ID": 1}
usuarios2 = {"nombre": "Rulito"}
nuevo_usuarios = {**usuarios, **usuarios2}
print(nuevo_usuarios)
