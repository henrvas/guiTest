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
    print ("\nvocê está sendo encaminhado para o pediatra\n\n")
    nome_responsavel = input("\nNome do Responsável: ")
    rg = int(input("\nRG Do Responsável: "))
    data_nascimento_responsavel = int(input("\nAno De Nascimento Do Responsável (YYYY): \n"))


for nome, idade, nome_responsavel, rg, data_nascimento_responsavel in {'Nome': nome, 'Ano nascimento': data_nascimento, 'nome_responsavel': nome_responsavel, 'rg': rg, 'data_nascimento_responsavel': data_nascimento_responsavel }.items():
    print(f"{nome}, {idade}, {nome_responsavel}, {rg}, {data_nascimento_responsavel}")