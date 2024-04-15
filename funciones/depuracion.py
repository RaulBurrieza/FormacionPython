def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
        return resultado


result = largo("hola")
print(result)
