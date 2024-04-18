letras = ["A", "B", "C", "D", "E"]


letras.insert(0, "Z")
print(letras)

letras.append("Y")
print(letras)


letras.remove("C")

letras.pop()
letras.pop(2)
print(letras)

del letras[0]

print(letras)


letras.clear()

print(letras)
