usuarios = [["Hola", "BCVX", 4], ["zzzz", "DSHFHSAD", 1],
            ["xxx", "dhfas", 2], ["yyy", "dfsadf", 3]]


nombres = [usuario[0] for usuario in usuarios]

nombres2 = [usuario[0]
            for usuario in usuarios if usuario[2] > 2]  # MAP Y FILTER A LA VEZ

print(f"{nombres}\n {nombres2}")


usuarios2 = [["Hola", "BCVX", 4], ["zzzz", "DSHFHSAD", 1],
             ["xxx", "dhfas", 2], ["yyy", "dfsadf", 3]]

nombres = list(map(lambda usuario: usuario[0], usuarios))

print(nombres)

nombresReducidos = list(filter(lambda usuario: usuario[2] > 2, usuarios))

print(nombresReducidos)
