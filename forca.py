import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    palavra_acertada = inicializa_letras_acertadas(palavra_secreta)
    print(palavra_acertada)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_acertada, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in palavra_acertada
        print(palavra_acertada)

    if acertou:
        imprime_mensagem_acertada()
    else:
        imprime_mensagem_perderdor()
    print("Fim de jogo!!!")

def imprime_mensagem_abertura():
    print("*******************")
    print("***Jogo da forca***")
    print("*******************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra_acertada[index] = letra
        index += 1

def imprime_mensagem_acertada():
    print("Vocé acertou!!!")

def imprime_mensagem_perderdor():
    print("Vocé perdeu!!!")

if __name__ == "__main__":
    jogar()
