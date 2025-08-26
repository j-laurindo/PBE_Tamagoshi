from tamagoshi import *

def main():
    print("\n-------------------------------------------------")
    print("|   BEM VINDO(A)! BRINQUE COM O SEU TAMAGOSHI   |")
    print("-------------------------------------------------")
    nomeUsuario = input("Digite o seu nome: ")
    print(f"----- Seja muito bem vindo(a), {nomeUsuario}! -----\n")
    resposta = int(input("Gostaria de criar um tamagoshi para você?    \n1 = SIM  |  2 = NÃO \nResposta: "))
    print("-------------------------------------------------")

    if(resposta == 2):
        print("\n-------------- FINALIZANDO JOGO --------------")
        exit()
    else:
        print("\n -> Ótimo! Escolha qual tamagoshi deseja adotar: ")
        escolhaTamagoshi = int(input("1 = Targaryen 🐉\n2 = Garfield 🐱\n3 = Vampiro 🧛\n-> Qual será sua escolha: "))

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
        while(opcao != 0):
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

            tamagoshi.vida()
            print("\n1 -> Alimentar")
            print("2 -> Brincar")
            print("3 -> Ações específicas do meu Tamagoshi")
            print("4 -> Status de Vida")
            print("0 -> Sair do Jogo")

            opcao = int(input("\n- Digite sua opção: "))
            

main()

