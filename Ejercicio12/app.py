#Desarrollar una aplicación donde dado dos valores, el primero sea el porcentaje del otro. Ejemplo: ingreso 5 , ingreso 20 y me tiene que decir 25% (Se podía desarrollar como aplicación de consola o como una página web. Como una web api no porque los datos eran ingresados por el usuario y como con la web api interactuamos con el Swagger no se puede)

print("=== CALCULADORA DE PORCENTAJES ===")
total = float(input("Ingrese el total: "))
porcentaje = float(input("Ingrese el porcentaje: "))

calculo = porcentaje*total/100

print(f"Dados estos numeros, el {porcentaje}% de {total} es {calculo}")
