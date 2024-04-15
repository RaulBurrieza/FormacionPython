def suma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    print(resultado)


suma(2, 5)
suma(2, 5, 4, 5)
