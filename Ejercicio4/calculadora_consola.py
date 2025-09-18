import operaciones_matematicas as ops

print("=== Calculadora de Consola ===")

num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

print("\nOperaciones disponibles:")
print("1. Sumar")
print("2. Restar") 
print("3. Multiplicar")

opcion = input("\nElegí una opción (1-3): ")

if opcion == "1":
    resultado = ops.sumar(num1, num2)
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif opcion == "2":
    resultado = ops.restar(num1, num2)
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif opcion == "3":
    resultado = ops.multiplicar(num1, num2)
    print(f"Resultado: {num1} * {num2} = {resultado}")
else:
    print("Opción inválida")