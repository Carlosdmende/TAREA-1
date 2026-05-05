contra = input ("Ingrese una contraseña nueva: ")

if len(contra) < 8:
    print("su contraseña es muy corta, minimo debe tener 8 caracteres")

elif len(contra) > 16:
    print("su contraseña es demasiado larga, ha llegado al maximo de caracteres que son 16")

else:
    print("su contraseña es valida")

    

