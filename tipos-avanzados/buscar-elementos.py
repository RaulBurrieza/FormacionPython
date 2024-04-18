abecedario = ["A", "B", "C", "D", "E"]


print(abecedario.index("C"))

if "F" in abecedario:
    print(abecedario.index("F"))
else:
    print("no encontre")


if "E" in abecedario:
    print(abecedario.index("E"))
else:
    print("no encontre")


numeros = [1, 2, 3, 4, 5, 2]

print(numeros.count("2"))

multiplicados = [num * 20 for num in numeros]

print(multiplicados)
