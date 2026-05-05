pago = 0
total = 0
extra = 1.20
cobrar = 0


print("Bienvido al sistema del peaje")
print("Recuerde que si es hora pico se cobrara un 20 porciento extra en el pago del peaje")
print("Vehiculos permitidos en el peaje: 1.Automovil 2.Motocicleta 3.Camion")

vehi = input("ingrese su tipo de vehiculo: ")
hora = input("es hora pico? (si/no): ")

if vehi in["automovil", "Automovil", "AUTOMOVIL"] and hora in["si","Si","SI","yes","Yes","YES"]:
    pago = 5.00
    cobrar = pago * extra
    print(f"el pago del peaje es de: {cobrar}")

elif vehi in["automovil", "Automovil", "AUTOMOVIL"] and hora in["no","NO"]:
    pago = 5.00
    print(f"el pago del peaje es de: {pago}")

elif vehi in["motocicleta", "Motocicleta", "MOTOCICLETA"] and hora in["si","Si","SI","yes","Yes","YES"]:
    pago = 2.00
    cobrar = pago * extra
    print(f"el pago del peaje es de: {cobrar}")

elif vehi in["motocicleta", "Motocicleta", "MOTOCICLETA"] and hora in["no","NO"]:
    pago = 2.00
    print(f"el pago del peaje es de: {pago}")

elif vehi in["camion", "Camion", "CAMION"] and hora in["si","Si","SI","yes","Yes","YES"]:
    pago = 10.00
    cobrar = pago * extra
    print(f"el pago del peaje es de: {cobrar}")

elif vehi in["camion", "Camion", "CAMION"] and hora in["no","NO"]:
    pago = 10.00
    print(f"el pago del peaje es de: {pago}")

else: 
    print("vehiculo no permitido en el peaje")