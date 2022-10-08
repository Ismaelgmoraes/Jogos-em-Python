import forca
import Adivinhar

print("***************************")
print("******Escolha seu Jogo*****")
print("***************************")

print("Escolha seu Jogo: ")
print("(1) Forca (2) Adivinhação")
Jogo = int(input("Qual Jogo? "))

if Jogo == 1:
    print("Jogando o jogo da forca")
    forca.jogar()

elif Jogo == 2:
    print("Jogando o jogo da adivinhação")
    Adivinhar.jogar()
