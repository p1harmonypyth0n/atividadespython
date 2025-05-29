continuar = True

while continuar:
    print("Imprimindo os números de 1 a 10:")
    for i in range(1, 11):
        print(i)

    resposta = input("Deseja repetir? (s/n): ").lower()
    if resposta != 's':
        continuar = False
        print("Programa encerrado.")
