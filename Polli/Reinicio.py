from dataset_alunas import dataset

dataset

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")

    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1:
            incluir_nova_aluna()
        elif cod_opcao == 2:
            consultar_lista_alunas()
        elif cod_opcao == 3:
            consultar_faltas_aluna()
        elif cod_opcao == 4:
            consultar_notas_aluna()
        elif cod_opcao == 5:
            consultar_status_aprovacao()
        elif cod_opcao == 6:
            print("Encerrando o programa...")
            break

def obter_opcao():
    codigo_opcao = 0

    while codigo_opcao not in [1, 2, 3, 4, 5, 6]:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
                
            if codigo_opcao not in [1, 2, 3, 4, 5, 6]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
    return codigo_opcao

    
def incluir_nova_aluna():
    print("Insira os seguintes dados: ")
    nome = str(input("Nome da aluna: ")) #Recebo nome da aluna
    sobrenome = str(input("Sobrenome da aluna: ")) #Recebo sobrenome da aluna
    turma = input("Turma da aluna (nº): ") #Recebo nome a turma
    lista_notas = obter_notas()
    
def obter_notas():
    quantidade_notas = int(input('Quantas notas serão calculadas?: '))
    notas = []
    for contador in range(quantidade_notas):
        while True: 
            entrada = input(f'Nota do #{contador + 1}: ')
            try:
                nota = float(entrada)
                notas.append(nota)
                break
            except ValueError:
                print('Erro em processar o valor. Insira um número válido')

    return notas
    
    
    lista_presenca = obter_presença()

def obter_presença():
    quantidade_aulas = int(input('Digite quantas aulas houveram: '))
    lista_presença = []

    for contador in range(quantidade_aulas):
        while True:
            entrada = input(f'Presença na aula #{contador +1} (True/False): ')
            if entrada in ['True', 'False']:
                lista_presença.append(eval(entrada))
                break
            else:
                print('Informação inválida. Insira apenas True ou False')

    return lista_presença
    nota_participacao = float(input("Participação da aluna: ")) #Recebo nota de participação
    print('Aluna adicionada com sucesso!' )
    
    
    # Armazeno os dados da aluna no dicionário dataset
    chave_aluna = (nome, sobrenome)
    dataset[chave] = {
        'sobrenome': sobrenome,
        "Turma": turma,
        "Notas": lista_notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao
    }
    print('Aluna adicionada com sucesso!')

def consultar_lista_alunas():
    lista_alunas = dataset
    print(lista_alunas.keys())
    return lista_alunas

def consultar_faltas_aluna():
    nome = str(input("Nome da aluna: ")) #Recebo nome da aluna
    sobrenome = str(input("Sobrenome da aluna: ")) #Recebo sobrenome da aluna
    
    if (nome, sobrenome) in dataset:
        faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
        total_aulas = len(dataset[(nome, sobrenome)]["Presença"])
        percentual_presenca = faltas / total_aulas * 100      
        print(f'Faltas de {nome}: {faltas}')
        return percentual_presenca
    else:
        print('Aluna não encontrada')   
   
def consultar_notas_aluna():
    nome = str(input('Nome da aluna: '))
    sobrenome = str(input('Sobrenome da aluna: '))    
    if (nome, sobrenome) in dataset:
        notas = dataset[(nome, sobrenome)]['Notas']
        media = sum(notas) / len(notas)       
        print(f'Notas da {nome}: {notas}')
        return media
    else:
        print('Aluna não encontrada')   
    
def consultar_status_aprovacao():
    nome = str(input('Nome da aluna: '))
    sobrenome = str(input('Sobrenome da aluna: '))
    if (nome, sobrenome) in dataset:
        notas = dataset[(nome, sobrenome)]['Notas']
        media = (sum(notas)) / len(notas)     
        faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
        total_aulas = len(dataset[(nome, sobrenome)]["Presença"])
        percentual_presenca = faltas / total_aulas * 100    
        participacao = dataset[(nome, sobrenome)]['Participação']
        if media >= 6  and participacao >= 6:                     
            print(f'Media: {media:.2f}\nFaltas: {percentual_presenca}\nParticipação: {participacao}\nSituação da aluna {nome}: APROVADA!!!')
        else:
            print(f'Media: {media:.2f}\nFaltas: {percentual_presenca}\nParticipação: {participacao}\nSituação da aluna {nome}: Reprovada.')
        
      

main()