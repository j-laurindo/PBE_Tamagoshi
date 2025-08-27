from tamagoshi import *

def main():
    ##############################################################
    #  MENU ENTRADA | Nome do usuário + Criação do Tamagoshi
    ##############################################################
    print("\n-------------------------------------------------")
    print("|   BEM VINDO(A)! BRINQUE COM O SEU TAMAGOSHI   |")
    print("-------------------------------------------------")
    nomeUsuario = input("Digite o seu nome: ")
    print(f"----- Seja muito bem vindo(a), {nomeUsuario}! -----\n")
    resposta = int(input("Gostaria de criar um tamagoshi para você?    \n1 = SIM  |  2 = NÃO \nResposta: "))
    print("-------------------------------------------------")

    ##############################################################
    #  MENU ENTRADA | Resposta = Não
    ##############################################################
    if(resposta == 2):
        print("\n-------------- FINALIZANDO JOGO --------------")
        exit()
    
    ##############################################################
    #  MENU ENTRADA | Resposta = Sim
    ##############################################################
    else:
        ##############################################################
        #  MENU DE CRIAÇÃO DO TAMAGOSHI
        ##############################################################
        print("\n -> Ótimo! Escolha qual tamagoshi deseja adotar: ")
        escolhaTamagoshi = int(input("1 = Targaryen 🐉\n2 = Garfield 🐱\n3 = Vampiro 🧛\n-> Qual será sua escolha: "))

        ## Opção 1 = Criar o Tamagoshi Targaryen ##
        if(escolhaTamagoshi == 1):
            time.sleep(1)
            print("\n--- CRIANDO SEU TAMAGOSHI TARGARYEN ---")
            time.sleep(1)
            nomeTamagoshi = input("-> Digite o nome do seu tamagoshi: ")
            tamagoshi = Targaryen(nomeTamagoshi)
            print(f"-> Tamagoshi {nomeTamagoshi} criado com sucesso! Tipo: Targaryen ")

            time.sleep(1)
            print("\n------ INICIANDO JOGO ------")
            time.sleep(1)
            print("---")
            time.sleep(1)
            print("-------")
            time.sleep(1)
            print("---------------")

        ## Opção 2 = Criar o Tamagoshi Garfield ##
        elif(escolhaTamagoshi == 2):
            time.sleep(1)
            print("\n--- CRIANDO SEU TAMAGOSHI GARFIELD ---")
            time.sleep(1)
            nomeTamagoshi = input("-> Digite o nome do seu tamagoshi: ")
            tamagoshi = Garfield(nomeTamagoshi)
            print(f"-> Tamagoshi {nomeTamagoshi} criado com sucesso! Tipo: Garfield ")

            time.sleep(1)
            print("\n------ INICIANDO JOGO ------")
            time.sleep(1)
            print("---")
            time.sleep(1)
            print("-------")
            time.sleep(1)
            print("---------------")
        
        ## Opção 3 = Criar o Tamagoshi Vampiro ##
        elif(escolhaTamagoshi == 3):
            time.sleep(1)
            print("\n--- CRIANDO SEU TAMAGOSHI VAMPIRO ---")
            time.sleep(1)
            nomeTamagoshi = input("-> Digite o nome do seu tamagoshi: ")
            tamagoshi = Vampiro(nomeTamagoshi)
            print(f"-> Tamagoshi {nomeTamagoshi} criado com sucesso! Tipo: Vampiro ")

            time.sleep(1)
            print("\n------ INICIANDO JOGO ------")
            time.sleep(1)
            print("---")
            time.sleep(1)
            print("-------")
            time.sleep(1)
            print("---------------")
        
        ## Opção Errada = Finalização do jogo ##
        else:
            time.sleep(1)
            print("\n-> Nenhuma opção correta foi selecionada, devido a isso o programa será finalizado")
            print("....")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n----- FIM DO JOGO -----")
        
        opcao = 1

        ##############################################################
        #  JOGO DO TAMAGOSHI
        ##############################################################
        while(opcao != 0):
            ## Verificação da vida do Tamagoshi ##
            if(tamagoshi.saude <= 0):
                print(f"------- {nomeTamagoshi} está morrendo! -------")
                time.sleep(1)
                print("----------------------------------")
                time.sleep(1)
                print("-------- Foi muito bom enquanto durou, né? ---------")
                time.sleep(1)
                print("----------------------------------")
                time.sleep(1)
                print(f"------- {nomeTamagoshi}: Obrigado por cuidar de mim...  --------")
                time.sleep(1)
                print(f"\n{nomeTamagoshi} faleceu :(")
                break
            
            ##############################################################
            #  Menu | JOGO DO TAMAGOSHI 
            ##############################################################
            tamagoshi.vida()
            print("\n1 -> Alimentar")
            print("2 -> Brincar")
            print("3 -> Ações específicas do meu Tamagoshi")
            print("4 -> Status de Vida")
            print("0 -> Sair do Jogo")

            opcao = int(input("\n- Digite sua opção: "))

            #### Opção | Alimentar ####
            if(opcao == 1):
                comida = int(input(f"\n-- O quanto de comida você dará ao {nomeTamagoshi}? -- \n-> Resposta: "))
                tamagoshi.alimentar(comida)
                print(f"\n-> {nomeTamagoshi}: Hummmmm, que delícia! Muito obrigada, {nomeUsuario}!")
                print()
                tamagoshi.status()

            #### Opção | Brincar ####
            elif(opcao == 2):
                xp = int(input(f"\n-- O quanto de xp você dará ao {nomeTamagoshi} durante a brincadeira? -- \n-> Resposta: "))
                tamagoshi.brincar(xp)
                print(f"\n-> {nomeTamagoshi}: Obrigado pela brincadeira, {nomeUsuario}!")
                print()
                tamagoshi.status()
            
            #### Opção | Ações Específicas ####
            elif(opcao == 3):
                ################################################
                # Escolha = Tamagoshi Targaryen
                ################################################
                if(escolhaTamagoshi == 1):
                    print(f"\n-- ESCOLHA SUA AÇÃO PARA {nomeTamagoshi} TARGARYEN --")
                    print("-> 1 = Nomear Dragão")
                    print("-> 2 = Voar com Dragão")
                    print("-> 3 = Treinar Valiriano")
                    print("-> 4 = Lutar pelo Trono de Ferro")
                    escolha = int(input("\n---> Resposta: "))
                    if(escolha == 1):
                        print()
                        tamagoshi.nomearDragao()
                        print()
                        tamagoshi.status()
                    elif(escolha == 2):
                        tempo = int(input(f"-> Digite por quanto tempo {nomeTamagoshi} Targaryen voou com {tamagoshi.dragao}"))
                        tamagoshi.voarDragao(tempo)
                        print()
                        tamagoshi.status()
                    elif(escolha == 3):
                        print()
                        tamagoshi.treinarValiriano()
                        print()
                        tamagoshi.status()
                    elif(escolha == 4):
                        print()
                        tamagoshi.lutarTrono()
                        print()
                        tamagoshi.status()
                    else:
                        print("-> Valor Inválido! Escolha uma opção existente")
                ################################################
                # Escolha = Tamagoshi Garfield
                ################################################
                elif(escolhaTamagoshi == 2):
                    print(f"\n-- ESCOLHA SUA AÇÃO PARA {nomeTamagoshi} GARFIELD --")
                    print("-> 1 = Roubar Lasanha")
                    print("-> 2 = Irritar o Tod")
                    print("-> 3 = Brincar com o Odie")
                    escolha = int(input("\n---> Resposta: "))
                    if(escolha == 1):
                        print()
                        tamagoshi.roubarLasanha()
                        print()
                        tamagoshi.status()
                    elif(escolha == 2):
                        print()
                        tamagoshi.irritarTod()
                        print()
                        tamagoshi.status()
                    elif(escolha == 3):
                        tempo = int(input(f"-> Digite por quanto tempo {nomeTamagoshi} Garfield brincou com o Odie"))
                        tamagoshi.brincarOdie(tempo)
                        print()
                        tamagoshi.status()
                    else:
                        print("-> Valor Inválido! Escolha uma opção existente")
                ################################################
                # Escolha = Tamagoshi Vampiro
                ################################################
                elif(escolhaTamagoshi == 3):
                    print(f"\n-- ESCOLHA SUA AÇÃO PARA {nomeTamagoshi} VAMPIRO --")
                    print("-> 1 = Tomar Sangue")
                    print(f"-> 2 = Hipnotizar {nomeUsuario}")
                    print("-> 3 = Transformar em Morcego")
                    escolha = int(input("\n---> Resposta: "))
                    if(escolha == 1):
                        qtd_sangue = int(input(f"-> Digite a quantidade de sangue que {nomeTamagoshi} vampiro irá tomar: "))
                        print()
                        tamagoshi.alimentar(qtd_sangue)
                        print()
                        tamagoshi.status()
                    elif(escolha == 2):
                        print()
                        tamagoshi.hipnose()
                        print()
                        tamagoshi.status()
                    elif(escolha == 3):
                        print()
                        tamagoshi.transformarMorcego()
                        print()
                        tamagoshi.status()
                    else:
                        print("-> Valor Inválido! Escolha uma opção existente")
            
            #### Opção | Status de Vida ####
            elif(opcao == 4):
                tamagoshi.status()
            
            #### Opção | Sair do jogo ####
            elif(opcao == 0):
                print(f"\n{nomeTamagoshi}: Muito obrigado por jogar comigo, {nomeUsuario}!")
                time.sleep(1)
                print("..............")
                time.sleep(1)
                print("...........")
                time.sleep(1)
                print(".......")
                time.sleep(1)
                print("....")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("\n------ JOGO ENCERRADO ------")
            
            #### Opção Errada ####
            else:
                print("-> Valor inválido! Escolha a opção correta")
            
            ## Função do tempo passando ##
            tamagoshi.tempoPassando()
            

main()

