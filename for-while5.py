while True:
    confirmar = input("Deseja calcular a soma de 1 a 100? (s/n): ").lower()

    if confirmar == 's':
        soma = 0
        for i in range(1, 101):
            soma += i
        print(f"Soma de 1 a 100: {soma}")
    elif confirmar == 'n':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite 's' ou 'n'.")


