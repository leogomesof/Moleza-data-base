##############################
#       MolezaDB v1.0        #
# Autor: Leonardo Gomes      #
# Função: Execução do CRUD   #
# com inserção de dados.     #
# Matrícula: 2022101335      #
# Útlima revisão: 27/11/2022 #
##############################

#importando a classe do arquivo MyCrud
from MyCrud import MyCrud

#variavel my_crud criada para acessar as funções dooutro arquivo
my_crud=MyCrud("moleza.sqlite3")
my_crud.criarTabela()
print("")
print("*"*34)
print("*"*5,"Bem vindo ao MolezaDB","*"*6)
print("*"*4, "Banco de dados na moleza!", "*"*3)
print("*"*34)

while True: #Usando while para o usuário sempre escolher algo
    opcao=input("\nDigite a opção desejada e pressione enter:\n\n1 - Inserir dados"
                          "\n2 - Alterar dados\n3 - Ler dados\n4 - Deletar dados\n"
                          "\nPara sair digite sair: ")
    #1 - Inserindo dados:
    if opcao=='1':
        print()
        print("*"*8,"Inserindo nome e cpf","*"*10)

        print("** Para voltar ao menu digite: voltar **\n")
        while True:
            #Inserindo valor para nome:
            voltar=0 #Variável criada para voltar ao menu principal
            if voltar<1:
                nome=input("Digite seu nome: ")
                if nome.casefold()=="voltar": #Usei casefold() caso estejam usando capslock
                    voltar=+1 #Variável incrementada para voltar ao menu principal
                    break
                elif nome.isdigit()==True or "." in nome or len(nome)<=2:
                    #Condição para que não use números em nome ou seja menor que 2 caracteres
                    print("*** ERN001: NOME INVÁLIDO ***\n")
                else:
                    while True:
                        voltar=0 #Variável criada para voltar para opção anterior
                        if voltar<1:
                            cpf=input("Digite os 11 números do seu CPF (sem traço): ")
                            #Condição para que não usem letras ou que seja diferente de 11 caracteres
                            if cpf.casefold()=="voltar":
                                #voltar=+1
                                break
                            elif cpf.isdigit()==False or len(cpf)<11 or len(cpf)>11:
                                print("*** ERCPF001: CPF INVÁLIDO ***\n")
                            else:
                                print("*** Nome e CPF inseridos com sucesso! ***")
                                my_crud.inserir(nome, cpf)
                                break
                    break

    #2 - Alterando dados
    elif opcao=='2':
        print()
        print("*"*10,"Alterando dados", "*"*12)
        print("** Para voltar ao menu digite: voltar *\n")
        while True:
            #Inserindo o valor de ID:
            voltar=0
            if voltar<1:
                id=input("Digite o valor da ID: ")
                if id.casefold()=="voltar":
                    break
                elif id.isdigit()==False:
                    #Condição para não ter letras no ID
                    print("*** ERRID001: ID INVÁLIDO\n")
                else:
                    print("*** ID {} foi selecionada ***".format(id))
                    #Trocando o nome
                    while True:
                        nome=input("\nDigite o nome para mudar: ")
                        if nome.casefold()=="voltar":
                            break
                        elif nome.isdigit()==True or "." in nome or len(nome)<=2:
                            print("*** ERN001: NOME INVÁLIDO ***")
                        else:
                            print("*** O Nome digitado foi: {}".format(nome))
                            # Trocando o CPF
                            while True:
                                cpf=input("\nDigite os 11 números do seu CPF (sem traço): ")
                                if cpf.casefold()=="voltar":
                                    break
                                elif cpf.isdigit()==False or len(cpf)<11 or len(cpf)>11:
                                    print("*** ERCPF001: CPF INVÁLIDO ***")
                                else:
                                    print("*** Alterações feitas com sucesso! ***")
                                    #Comando que insere valores no banco de dados
                                    my_crud.alterar(id, nome, cpf)
                                    break
                            break
                    break

    #3 - Mostrando a tabela de itens criados:
    elif opcao=='3':
        print("\n*** Mostrando inseridos no banco ***")
        print("*** A posição é: ID, Nome e CPF ****\n ")
        my_crud.selecionar() #Comando que dá o SELECT no programa

    #4 - Apagando dados
    elif opcao=='4':
        print()
        print("*" * 8, "Apagando dados do banco", "*" * 10)
        print("**** Para voltar ao menu digite: voltar ***\n")
        while True:
            voltar=0
            if voltar<1:
                id=input("Digite o valor da ID: ")
                if id.casefold()=="voltar":
                    voltar=+1
                    break
                elif id.isdigit() == False:
                    print("*** ERRID001: ID INVÁLIDO\n")
                else:
                    print("\n*** DESEJA REALMENTE APAGAR A ID {}? ***".format(id))
                    certeza=input("Digite sim ou não -> ")
                    if certeza.casefold()=="sim":
                        print("\n*** ID {} removida com sucesso! ***".format(id))
                        my_crud.deletar(id)
                        break
                    else:
                        print("\n!!! OPERAÇÃO CANCELADA !!!")
                        break

    #5 - Mensagem de saída
    elif opcao.casefold()=="sair":
        my_crud.fecharDB()
        print("*" * 38)
        print("*"*7," Aplicação finalizada ","*"*7)
        print("*"*3," Obrigado por usar MolezaDB ","*"*5)
        print("*" * 38)
        break
    else:
        print("\n!!! OPÇÃO INVÁLIDA !!!")