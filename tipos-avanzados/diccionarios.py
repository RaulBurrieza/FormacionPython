punto = {"x": 25, "y": 39}

print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

if "lala" in punto:
    print("encontre lala", punto["lala"])


print(punto.get("x"))

# Si lala no es una llave valida en el diccionario punto el valor por defecto sera 97
print(punto.get("lala", 97))


del punto["x"]

punto["x"] = 45

for v in punto:
    print(v, punto[v])

for valor in punto.items():
    print(valor)

for key, value in punto.items():
    print(f"{key}: {value}")


usuarios = [
    {"ID": 1, "nombre": "Raul"},
    {"ID": 2, "nombre": "Raulito"},
    {"ID": 3, "nombre": "Rulito"},
]

for usuario in usuarios:
    print(usuario["nombre"])
