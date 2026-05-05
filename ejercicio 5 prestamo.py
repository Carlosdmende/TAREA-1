print("buenas noches bienvenido al sistema de prestamo del banco")
print("")
print("le indico las condiciones para obtener un prestamo")
print("")
print("Lo primero que debe de hacer es ingresar su edad si es mayor de 25 años puede solicitar un prestamo y si es menor de 25 años no puede solicitar un prestamo")
print("")
print("Lo segundo que debe de hacer es ingresar su salario mensual si es mayor de 3000 dolares puede solicitar un prestamo si su salario esta ")
print("")
print("entre 1500 y 3000 dolares puede solicitar un prestamo pero con aval y si su salario es menor de 1500 dolares no puede solicitar un prestamo")

edad = int(input("ingrese su edad: "))
salario = int(input("ingrese su salario mensual: "))

if edad >= 25 and salario > 3000:
    print("si puede solicitar un prestamo")

elif edad >= 25 and salario >= 1500 and salario <= 3000:
    print("puede solicitar un prestamo pero con aval")

else:
    print("no puede solicitar un prestamo")