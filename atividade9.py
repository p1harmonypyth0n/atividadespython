salario = 3500.00
idade = 22

mensagens = {
    True: "Elegível para empréstimo.",
    False: "Não elegível para empréstimo."
}

print(mensagens[salario >= 3000 and idade >= 21])
