import time, random

class Tamagoshi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0 and quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)
        elif (self.fome == 0):
            print(f"{self.nome} já está cheio!")
    
    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)
    
    def getHumor(self):
        return 100 - ((self.fome + self.tedio) / 2)
    
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 80)) or ((self.tedio > 60 and self.tedio <= 80)):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 90)):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print("Estou morrendo.... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu T_T")
    
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5

    def status(self):
        print(f"-> Vida: {self.saude}")
        print(f"-> Idade: {self.idade}")
        print(f"-> Tedio: {self.tedio}")
        print(f"-> Fome: {self.fome}")

#### GARFIELD ###################

class Garfield(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.saude = 200
        self.fome = 20
        self.tedio = 30
        self.sono = 30

    def roubarLasanha(self):
        if(self.tedio > 20):
            print("-----------")
            print("-> O Tamagoshi Garfield está entediado, ele tá afim de bater uma boquinha")
            print("-----------")
            time.sleep(1)
            print("\n-> Escolha uma comida para dar uma 'animada' no Tamagoshi Garfield")
            print("\n-> 1 - Lasanha 🥘")
            print("\n-> 2 - Churrasco 🍖")
            print("\n-> 3 - Maçã 🍎")
            
            escolha = int(input("\nResposta: "))

            if(escolha == 1):
                self.fome -= 60
                self.tedio -= 30
                print(f"\n-> O Tamagoshi Garfield achou massa esse lanchinho! <3")
            elif(escolha == 2):
                self.fome -= 40
                self.tedio -= 20
                print(f"\n-> O Tamagoshi Garfield até achou legalzinho esse petisco")
            elif(escolha == 3):
                self.fome += 30
                self.tedio += 30
                print(f"\n-> TÁ MALUCO? O Tamagoshi Garfield quase passou mal, ele >>>odeia<<< maçã!!!!!!😤😤")
            else:
                print("-> Valor inválido")
        else:
            print("O Garfield tá de boa!")
    
    def irritarTod(self):
        print("-> O Tamagoshi Garfield está entediado, o Tod dormindo parece tãaaao tranquilo...")
        time.sleep(2)
        print("-> Bem tranquilo mesmo...")
        time.sleep(2)
        print("-> Tãaaaaaaaao irritante...")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print("-> 🤦‍♂️ AAAAU")
        print("-> Tamagoshi Garfield arranhou 'acidentalmente' o braço de Tod :D")
        print("-> Tamagoshi Garfield se sente mais feliz")
        
        self.getHumor += 10

    def brincar(self, quantidade):
        print("-> O cachorro Odie chama o Tamagoshi Garfield para brincar")
        escolha = int(input("1 - SIM  |  2 - NÃO  \n -> Resposta: "))

        if(escolha == 1):
            self.tedio -= self.tedio * (quantidade / 100)
            self.fome += 15
            
            print("-> O Tamagoshi Garfield brincou (um pouco)")
        elif(escolha == 2):
            print("-> O Tamagoshi Garfield fingiu que não ouviu")

#### TARGARYEN ##################

class Targaryen(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.dragao = ""
        self.saude = 300
        self.valiriano = 0
        self.montaria = 0
        self.luta = 0
    
    def nomearDragao(self):
        print("Seu ovo de dragão finalmente rachou, revelando um lindo filhote de dragão. Gostaria de nomea-lo?")
        resposta = int(input("1 = SIM  |  2 = NÃO \nResposta: "))

        if(resposta == 1):
            self.dragao = input("\n-> Digite o nome do seu dragãozinho: ")
            print(f"-> Seja bem-vindo, {self.dragao} 🐉")
        elif(resposta == 2):
            print("-> Seu dragão não foi nomeado")
        else:
            print("-> Digite um valor válido")
    
    def voarDragao(self, tempo):
        print(".........")
        time.sleep(0.3)
        print("........")
        time.sleep(0.3)
        print(".......")
        time.sleep(0.3)
        print("......")
        time.sleep(0.3)
        print(".....")
        time.sleep(0.3)
        print(f"{self.nome} Targaryen está voando... 🐉")
        print(".....")
        time.sleep(0.3)
        print("......")
        time.sleep(0.3)
        print(".......")
        time.sleep(0.3)
        print("........")
        time.sleep(0.3)
        print(".........")

        if(tempo > 0 and tempo <= 2):
            self.montaria += tempo / 0.8
            self.tedio = self.tedio - self.tedio * ((tempo * 0.8) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 2 and tempo <= 4):
            self.montaria += tempo / 0.6
            self.tedio = self.tedio - self.tedio * ((tempo * 0.6) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 4 and tempo <= 10):
            self.montaria += tempo / 0.4
            self.tedio = self.tedio - self.tedio * ((tempo * 0.4) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
        elif(tempo > 10):
            self.montaria += tempo / 0.2
            self.tedio = self.tedio - self.tedio * ((tempo * 0.2) / 100)
            print(f"{self.nome} voaram por {tempo} hora(s)")
            print(f"Seu tedio diminuiu para: {self.tedio}")
        else:
            print(f"{self.dragao} não voou muito, ele(a) ficou triste :(")

    def treinarValiriano(self):
        estudo = int(input("-> Adicione o tempo de estudo de conhecimento [1 - 100]: "))
        print("\n--------")
        time.sleep(2)
        print("Estudando valíriano...📖")
        time.sleep(2)
        print("--------\n")

        self.valiriano += (estudo / 10)

        print(f"-> {self.nome} Targaryen está falando {self.valiriano}% de valiriano! ")
    
    def lutarTrono(self):
        dano = random.randint(0, 300)
        print("\n>>>>>> Uma batalha pelo trono de ferro está começando! <<<<<<")
        escolha = int(input("1 - Recuar  |  2 - LUTAR! \nResposta: "))
        
        if(escolha == 1):
            print("\n-----------------")
            time.sleep(1)
            print(f"{self.nome} Targaryen recuou da batalha, preservando sua saude!")
            time.sleep(1)
            print("-----------------\n")
        elif(escolha == 2):
            print("\n-----------------")
            time.sleep(1)
            print(f"{self.nome} Targaryen foi à luta! DRACARYS {self.dragao} 🐉🔥")
            print("-----------------\n")
            time.sleep(1)

            self.saude -= dano

            if(self.saude <= 0):
                print("-----------------")
                time.sleep(1)
                print(f"{self.nome} Targaryen morreu...")
                print("........")
                time.sleep(0.7)
                print(".......")
                time.sleep(0.7)
                print("......")
                time.sleep(0.7)
                print(".....")
                time.sleep(0.7)
                print("....")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print(".")
                time.sleep(3)
                exit()
            else:
                print(f"{self.nome} Targaryen está com {self.saude} de vida")
        else:
            print("-> Digite um valor válido")

#### VAMPIRO ####################

class Vampiro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.saude = 1000
        self.transformacao = 0
        self.conhecimento_vampirico = 80

    def alimentar(self, quantidade):
        if (quantidade >= 0 and quantidade <= 100):
            print(f"-> O Tamagoshi {self.nome} está bebendo sangue")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("🩸")

            self.fome -= self.fome * (quantidade / 100)
        elif (self.fome == 0):
            print(f"{self.nome} já está cheio!")

    def hipnose(self):
        if(self.conhecimento_vampirico <= 20):
            print(f"-> {self.nome} tentou hipnotizar você, mas aparentemente não funcionou!")
            self.transformacao += 5
        elif(self.conhecimento_vampirico <= 70):
            print("...")
            time.sleep(1)
            print("......")
            time.sleep(1)
            print("........")
            time.sleep(1)
            print(f"-> {self.nome} tentou hipnotizar você, percebeu sua consciência sumindo?")
        elif(self.conhecimento_vampirico <= 100):
            print("...")
            time.sleep(1)
            print("......")
            time.sleep(1)
            print("........")
            print(f"-> {self.nome} hipnotizou você! Assista Crepusculo imediatamente")  
        else:
            print("-> Valor inválido")
    
    def transformarMorcego(self, horario):
        if(horario > 18):
            print(f"{self.nome} se tranformou em morcego!! 🦇")
            tempo = int(input(f"-> Por quanto tempo o vampiro {self.nome} se transformou em morcego? \n-> Resposta: "))
            
            if(tempo > 0 and tempo <= 2):
                self.conhecimento_vampirico += self.conhecimento_vampirico + tempo * 0.8
                self.transformacao += 3
            elif(tempo > 2 and tempo <= 4):
                self.conhecimento_vampirico += self.conhecimento_vampirico + tempo * 0.6
                self.transformacao += 4
            elif(tempo > 4 and tempo <= 8):
                self.conhecimento_vampirico += self.conhecimento_vampirico + tempo * 0.2
                self.transformacao += 4
            elif(tempo > 8 and tempo <= 12):
                self.conhecimento_vampirico += self.conhecimento_vampirico + tempo * 2
                self.transformacao += 5
            else:
                print("Valor inválido, já deve ser de manhã")
        else:
            print(f"-> O sol ainda está lá fora, não tem como {self.nome} se tranformar! :(")
            print(f"-> {self.nome} se queimou no processo!")
            self.saude -= self.saude * 0.2



    

