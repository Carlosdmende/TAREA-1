print("juego de piedra, papel o tijeras")
print("reglas")
print("tijera le gana a papel")
print("papel le gana a piedra")
print("piedra le gana a tijera")
print("y si son iguales es empate")

p1 = input("P1, elija piedra, papel o tijera: ")
p2 = input("P2, elija piedra, papel o tijera: ")

if p1 in["piedra", "Piedra", "PIEDRA"] and p2 in["tijera", "Tijera", "TIJERA"]:
    print("P1 gana")
elif p2 in["piedra", "Piedra", "PIEDRA"] and p1 in["tijera", "Tijera", "TIJERA"]:
    print("P2 gana")
elif p1 in["papel", "Papel", "PAPEL"] and p2 in["piedra", "Piedra", "PIEDRA"]:
    print("P1 gana")    
elif p2 in["papel", "Papel", "PAPEL"] and p1 in["piedra", "Piedra", "PIEDRA"]:
    print("P2 gana")
elif p2 in["tijera", "Tijera", "TIJERA"] and p1 in["papel", "Papel", "PAPEL"]:
    print("P1 gana")
elif p1 in["tijera", "Tijera", "TIJERA"] and p2 in["papel", "Papel", "PAPEL"]:
    print("P2 gana")
elif p1 in["piedra", "Piedra", "PIEDRA"] and p2 in["piedra", "Piedra", "PIEDRA"]:
    print("empate")
elif p1 in["papel", "Papel", "PAPEL"] and p2 in["papel", "Papel", "PAPEL"]:
    print("empate")
elif p1 in["tijera", "Tijera", "TIJERA"] and p2 in["tijera", "Tijera", "TIJERA"]:
    print("empate") 
else:
    print("comando no vaido vuelva a intentarlo")