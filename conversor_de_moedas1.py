# Conversor de Moedas USD/BRL - Versão Simplificada para Iniciantes
def mult(valor):
    return valor* TAXA_DOLAR_PARA_REAL

def div(valor):
    return valor/TAXA_DOLAR_PARA_REAL
# Definição da taxa de câmbio fixa (1 dólar = 5 reais)

TAXA_DOLAR_PARA_REAL = 5

# Loop principal do programa

while True:

# Menu de opções

  print("\n=== Conversor de Moedas ===")
  print("1 - Converter Dólar para Real")
  print("2 - Converter Real para Dólar")
  print("0 - Sair do programa")

# Recebe a escolha do usuário

opcao = input("Digite sua opção: ")

     # Opção 1: Converter Dólar para Real
if opcao == "1":
        alor_dolar = input("Digite o valor em dólares (USD): ")
        valor_dolar = float(valor_dolar) # Converte para número decimal
        valor_real = mult(valor_dolar)
        print(f"US$ {valor_dolar:.2f} = R$ {valor_real:.2f}")

    # Opção 2: Converter Real para Dólar

elif opcao == "2":
        valor_real = input("Digite o valor em reais (BRL): ")
        valor_real = float(valor_real) # Converte para número decimal
        valor_dolar = div(valor_real)
        print(f"R$ {valor_real:.2f} = US$ {valor_dolar:.2f}")

    # Opção 0: Sair do programa

elif opcao == "0":
     print("Obrigado por usar o conversor. Até mais!")
     break # Encerra o loop while

    # Tratamento de opção inválida

else:
        print("Opção inválida! Por favor, digite 1, 2 ou 0.")