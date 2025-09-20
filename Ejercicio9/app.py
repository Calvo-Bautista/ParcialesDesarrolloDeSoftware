#Consola concatenar dos palabras


def main():
    print("--- CONCATENAR 2 PALABRAS ---")
    palabra1 = input("Ingrese una palabra: ")
    palabra2 = input("Ingrese una palabra: ")
    palabrafinal = palabra1 + palabra2
    print(f"La palabra concatenada es {palabrafinal}")


if __name__ == "__main__":
    main()