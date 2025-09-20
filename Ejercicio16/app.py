#Desarrolle una app que calcule el porcentaje que representa un valor por sobre 
#otro (ingresado por el user)

print("=== CALCULADORA DE PORCENTAJES ===")

total = float(input("\nIngrese el total: "))
porcentaje = float(input("Ingrese el porcentaje: "))

calculo = porcentaje*total/100

print(f"\n El {porcentaje}% de {total} es {calculo}")