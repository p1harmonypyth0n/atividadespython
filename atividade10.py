autonomia_km_por_litro = 12
tanque_litros = 40
distancia_viagem = 450

autonomia_total = autonomia_km_por_litro * tanque_litros

mensagens = {
    True: "O carro consegue fazer a viagem sem reabastecer.",
    False: "O carro **não** consegue fazer a viagem sem reabastecer."
}

print(mensagens[autonomia_total >= distancia_viagem])
