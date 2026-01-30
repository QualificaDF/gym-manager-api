def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso ideal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
