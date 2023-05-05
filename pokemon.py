from mimetypes import init
from random import randint
import math

class Pokemon:
    def __init__(self, nome, tipo, descricao, ataque, defesa, energia, nivel):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataque = randint(0, 15)
        self.defesa = randint(0, 15)
        self.energia = randint(0, 15)
        self.nivel = randint(1,50)
        self.cp = 0
        self.hp = 0
        self.iv = 0
        self.ganha = ""
        self.perde = ""

    def __str__(self):
        return f"{self.nome}, (Tipo: {self.tipo}) (Descrição: {self.descricao}) (Ataque: {self.ataque}) (Defesa: {self.defesa}) (Energia: {self.energia}) (Nível: {self.nivel}) "

    def CalculaStatus(ataque, defesa, energia, nivel):
      if ataque < 0 or ataque > 15 or defesa < 0 or defesa > 15 or energia < 0 or energia > 15:
         return "Valores de ataque, defesa ou energia inválidos."
    
      if nivel < 1 or nivel > 50:
         return "Valor de nível inválido."
      CP = int((ataque + defesa + energia) * math.sqrt(nivel) / 10)
      HP = int((energia * 2 + defesa + ataque / 2) * nivel / 100 + nivel + 10)
      IV = int((ataque + defesa + energia) / 45 * 100)
      return CP, HP, IV
        
    def Vantagem(self):
        tipo = self.tipo
        if tipo == 'Inseto':
           return ['Planta', 'Psíquico', 'Sombrio']
        elif tipo == 'Sombrio':
           return ['Fantasma', 'Psíquico']
        elif tipo == 'Dragão':
           return ['Dragão']
        elif tipo == 'Elétrico':
           return ['Água', 'Voador']
        elif tipo == 'Fada':
           return ['Lutador', 'Dragão', 'Sombrio']
        elif tipo == 'Lutador':
           return ['Gelo', 'Pedra', 'Normal', 'Aço', 'Sombrio']
        elif tipo == 'Fogo':
           return ['Planta', 'Inseto', 'Gelo', 'Aço']
        elif tipo == 'Voador':
           return ['Planta', 'Inseto', 'Lutador']
        elif tipo == 'Fantasma':
           return ['Fantasma', 'Psíquico']
        elif tipo == 'Planta':
           return ['Água', 'Pedra', 'Terrestre']
        elif tipo == 'Terrestre':
           return ['Fogo', 'Elétrico', 'Venenoso', 'Pedra', 'Aço']
        elif tipo == 'Gelo':
           return ['Voador', 'Planta', 'Terrestre', 'Dragão']
        elif tipo == 'Normal':
           return []
        elif tipo == 'Venenoso':
           return ['Planta', 'Fada']
        elif tipo == 'Psíquico':
           return ['Lutador', 'Veneno']
        elif tipo == 'Pedra':
           return ['Fogo', 'Gelo', 'Voador', 'Inseto']
        elif tipo == 'Aço':
           return ['Gelo', 'Pedra', 'Fada']
        elif tipo == 'Água':
           return ['Fogo', 'Pedra', 'Terrestre']
        else:
           return []
        
    def desvantagem(self):
         tipo = self.tipo
         if tipo == 'Inseto':
          return ['Fogo', 'Voador', 'Pedra']
         elif tipo == 'Sombrio':
          return ['Lutador', 'Inseto', 'Fada']
         elif tipo == 'Dragão':
          return ['Gelo', 'Dragão', 'Fada']
         elif tipo == 'Elétrico':
          return ['Terrestre']
         elif tipo == 'Fada':
          return ['Venenoso', 'Aço']
         elif tipo == 'Lutador':
          return ['Voador', 'Psíquico', 'Fada']
         elif tipo == 'Fogo':
          return ['Água', 'Terrestre', 'Pedra']
         elif tipo == 'Voador':
          return ['Elétrico', 'Gelo', 'Pedra']
         elif tipo == 'Fantasma':
          return ['Fantasma', 'Sombrio']
         elif tipo == 'Planta':
          return ['Fogo', 'Gelo', 'Voador', 'Inseto', 'Venenoso']
         elif tipo == 'Terrestre':
          return ['Água', 'Planta', 'Gelo']
         elif tipo == 'Gelo':
          return ['Fogo', 'Lutador', 'Pedra', 'Aço']
         elif tipo == 'Normal':
          return ['Lutador']
         elif tipo == 'Venenoso':
          return ['Terrestre', 'Psíquico']
         elif tipo == 'Psíquico':
          return ['Inseto', 'Fantasma', 'Sombrio']
         elif tipo == 'Pedra':
          return ['Água', 'Planta', 'Lutador', 'Aço', 'Terrestre']
         elif tipo == 'Aço':
          return ['Fogo', 'Lutador', 'Terrestre']
         elif tipo == 'Água':
          return ['Elétrico', 'Planta']
         else:
          return []

#programação

pikachu = Pokemon('Pikachu', 'Elétrico', 'o melhor', '', '', '', '')
charmander = Pokemon('Charmander', 'Fogo','o pior',  '', '', '','' )

print(pikachu)
print(charmander)

