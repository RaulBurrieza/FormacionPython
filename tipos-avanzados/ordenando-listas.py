numeros = [1, 4, 8, 7, 3, 9, 0]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

# NO AFECTA A LA ANTERIOR LISTA SOLO DEVUELVE UNA NUEVA LISTA
numeros2 = sorted(numeros)


usuarios = [["Hola", "BCVX", 4], ["zzzz", "DSHFHSAD", 1],
            ["xxx", "dhfas", 2], ["yyy", "dfsadf", 3]]


def ordena(elemento):
    return elemento[2]


usuarios.sort(key=ordena)
# EN ESTE CASO NECESITAMOS  CREAR UNA FUNCION QUE DEVUELVA PRIMERO EL ELEMENTO ITERABLE DE LA FUNCION PARA QUE PUEDA FUNCIONAR EL SORT
print(usuarios)


usuarios.sort(key=ordena, reverse=True)
# EN ESTE CASO NECESITAMOS  CREAR UNA FUNCION QUE DEVUELVA PRIMERO EL ELEMENTO ITERABLE DE LA FUNCION PARA QUE PUEDA FUNCIONAR EL SORT
print(usuarios)


usuarios2 = [["Hola", "BCVX", 4], ["zzzz", "DSHFHSAD", 1],
             ["xxx", "dhfas", 2], ["yyy", "dfsadf", 3]]


usuarios2.sort(key=lambda el: el[2])
# Funcion lambda es decir le pasamos el parametro y el valor de retorno
# para ahorrarnos hacer una funcion que se ejecuta una unica vez como en el ejemplo anterior
print(usuarios2)
