def determinar_nivel_urgencia(graus_soma):
    if graus_soma <= 1:
        return 'Baixo'
    elif graus_soma == 2:
        return 'Médio'
    else:
        return 'Alta'

nome = input("Nome Do Paciente: \n")
data_nascimento = int(input("\nAno De Nascimento Do Paciente (YYYY): \n"))
grau_de_urgencia = int(input("\n[0] Dor - [1] Febre - [2] Vomito: "))
grau_de_urgencia2 = int(input("\n[0] Baixo - [1] Média - [2] Alta: "))

if data_nascimento > 2006:
    print("\nvocê está sendo encaminhado para o pediatra\n\n")
    nome_responsavel = input("\nNome do Responsável: ")
    rg = int(input("\nRG Do Responsável: "))
    data_nascimento_responsavel = int(input("\nAno De Nascimento Do Responsável (YYYY): \n"))
    
    # Exibir informações
    print("\nInformações do Paciente e Responsável:")
    print(f"Nome do Paciente: {nome}")
    print(f"Ano de Nascimento do Paciente: {data_nascimento}")
    print(f"Nome do Responsável: {nome_responsavel}")
    print(f"RG do Responsável: {rg}")
    print(f"Ano de Nascimento do Responsável: {data_nascimento_responsavel}")

while True:
    print("\n\n\n=======================================")
    print("Menu")
    print("1. Opção A")
    print("2. Sair")
    print("=======================================")

    escolha = input("Escolha uma opção:\n R. ")

    if escolha == "1":
        print("Você escolheu a opção A")
    elif escolha == "2":
        break
    else: 
        print("Opção inválida")
