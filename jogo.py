import random
# Personagem: classe mae
class Personagem:
    def __init__(self, nome, nivel, vida):
        self.__nome = nome
        self.__nivel = nivel
        self.__vida = vida
    
    def get_nome(self):
        return self.__nome
    
    def get_nivel(self):
        return self.__nivel
    
    def get_vida(self):
        return self.__vida
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) 
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

# Heroi
class Heroi(Personagem):
    def __init__(self, nome, nivel, vida, habilidade):
        super().__init__(nome, nivel, vida)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade {self.get_habilidade()} e causou {dano} de dano!")

# Inimigo
class Inimigo(Personagem):
    def __init__(self, nome, nivel, vida, tipo):
        super().__init__(nome, nivel, vida)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
    
class Jogo:
    """ Classe orquestradora do jogo """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", nivel=5, vida=100, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel= 5, tipo="Voador")

    def iniciar_batalha(self):
        """ Fazer gestão da batalha em turnos """
        print("Iniciando batalha!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pessione enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida escolha novamente")

            if self.inimigo.get_vida() > 0:
                # Inimigo atacando o heroi
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha")
        else:
            print("\nVocê foi derrotado")

# Instancia do Jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()