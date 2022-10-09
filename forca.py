import random

def jogar():
    print("*******************")
    print("***Jogo da forca***")
    print("*******************")

    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    palavra_acertada = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    palavra_acertada[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in palavra_acertada
        print(palavra_acertada)

    if acertou:
        print("Vocé acertou!!!")
    else:
        print("Vocé perdeu!!!")
    print("Fim de jogo!!!")

if __name__ == "__main__":
    jogar()
