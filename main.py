
import random


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.play = None

    def vitoria(self):
        self.vitorias += 1

    def derrota(self):
        self.derrotas += 1


jogadas = ['pedra', 'papel', 'tesoura']


def validate_play(player_1, player_2):
    play_player_1 = player_1.play
    play_player_2 = player_2.play
    if play_player_1 == play_player_2:
        return "Empate"
    elif (play_player_1 == "pedra" and play_player_2 == "tesoura") or (play_player_1 == "papel" and play_player_2 == "pedra") or (play_player_1 == "tesoura" and play_player_2 == "papel"):
        player_1.vitoria()
        player_2.derrota()
        return "Vitória"

    else:
        player_1.derrota()
        player_2.vitoria()
        return "Derrota"


voce = Jogador("João")
computador = Jogador("Computador")

while (True):
    print(f"Bem vindo ao jogo \"Pedra, papel e tesoura\"")
    print("\n")
    print("1 - Pedra | 2 - Papel | 3 - Tesoura")
    print("\n")
    jogada_escolhida = int(input("Qual sua jogada? "))
    jogada = jogadas[jogada_escolhida - 1]
    jogada_computador = random.choice(jogadas)
    voce.play = jogada
    computador.play = jogada_computador
    print(
        f"Você jogou {jogada} e o computador jogou {jogada_computador}\n")
    print("Resultado:")
    print(f"{validate_play(voce, computador)}\n")
    print("Placar \n")
    print("Você:")
    print("Vitórias | Derrotas")
    print(f"      {voce.vitorias} | {voce.derrotas}\n")
    print("Computador:")
    print("Vitórias | Derrotas")
    print(f"      {computador.vitorias} | {computador.derrotas}\n")
    print("Deseja jogar novamente? (s/n)")
    choice = input()
    if choice == "n":
        break
    else:
        pass
