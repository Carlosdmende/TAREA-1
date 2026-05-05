print("Bienvenido a la tienda. Por favor, ingrese los detalles de su compra")
print("recuerde ingresar el tipode producto, la cantidad y el precio unitaritario")
print("")


cate = input("Ingrese la categoría del producto: ")
cant = int(input("ponga la cantidad del producto que lleva: "))
precio = float(input("ponga el precio unitaria: "))
print("")

total= cant * precio

if cate in ["Electrónica", "electronica", "ELECTRONICA"] and cant >= 3:
    total = total - total * 0.10
elif cate in ["Ropa", "ropa", "ROPA"] and cant >= 5:
    total = total - total * 0.15
else:
    print("No se aplican descuentos para esta compra.")

print(f"El total de su compra es: ${total}")
