def calcular_porcentaje(numero, total):
    porcentaje = (numero / total) * 100
    return porcentaje


def main():
    print("=== Calculadora de Porcentajes ===")
    print("Calcula qué porcentaje representa un número de otro")

    # Solicitar los números al usuario
    numero = float(input("Ingresa el número: "))
    total = float(input("Ingresa el total: "))

    # Calcular el porcentaje
    resultado = calcular_porcentaje(numero, total)
    print(f"el {numero}% de {total} es: {resultado}%")


if __name__ == "__main__":
    main()
