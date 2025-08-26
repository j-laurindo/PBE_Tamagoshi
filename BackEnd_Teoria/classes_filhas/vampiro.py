import time
import random
from tamagoshi import Tamagoshi

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

edward = Vampiro("Edward")