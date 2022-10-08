import random

def jogar():
    print("*******************")
    print("*Jogo de adivinhar*")
    print("*******************")

    Num_secreto = random.randrange(1, 101)
    print(Num_secreto)
    TotalDeTentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Facil (2) médio (3) difícil")
    nivel = int(input("Defina o nível: "))
    pontos = 1000

    if nivel == 1:
        TotalDeTentativas = 20
    elif nivel == 2:
        TotalDeTentativas = 10
    else:
        TotalDeTentativas = 5

    for Rodada in range(1, TotalDeTentativas + 1):
        print("Tentativa {} de {}".format(Rodada, TotalDeTentativas))
        _chute = input("Digite o seu numero: ")
        print("Você digitou:", _chute)
        chute = int(_chute)
        if chute < 1 or chute > 100:
            print("Você deve digitar um valor entre 1 e 100")
            continue
        acertou = Num_secreto == chute
        baixo   = Num_secreto > chute
        alto    = Num_secreto < chute

        if acertou:
            print("voce acertou e fez {} pontos.".format(pontos))
            break
        elif baixo:
            print("voce errou para baixo")
        elif alto:
            print("voce errou para cima")
        pontos_perdidos = abs(Num_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim de Jogo!!!")
if __name__ == "__main__":
    jogar()