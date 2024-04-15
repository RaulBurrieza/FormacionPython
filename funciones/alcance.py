
saludo = "Hola global"


def saludar():
    global saludo
    saludo = "HOLAAAAA"


def BurriTeSaluda():
    saludo = "KUOKA"


print(saludo)
saludar()
print(saludo)
