from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
user = int(input("Qual você escolheu? "))

#Animação
print("-=" * 11)
print("{:^22}".format("JO"))
sleep(1)
print("{:^22}".format("KEN"))
sleep(1)
print("{:^22}".format("PÔ!"))
sleep(1)
print("-=" * 11)

#Mostrando para o usuário
print("O computador jogou {}".format(itens[computador]))
print("Você jogou {}\n".format(itens[user]))

#Pedra
if computador == 0:
  if user == 0:
    print("EMPATE")
  elif user == 1:
    print("VOCÊ GANHOU, PARABÉNS")
  elif user == 2:
    print("VOCÊ PERDEU")

# Papel
elif computador == 1:
  if user == 0: 
    print("VOCÊ PERDEU")
  elif user == 1:
    print("EMPATE")
  elif user == 2:
    print("VOCÊ GANHOU, PARABÉNS!")

#Tesoura
elif computador == 2:
  if user == 0: 
    print("VOCÊ GANHOU, PARABÉNS!")
  elif user == 1:
    print("VOCÊ PERDEU")
  elif user == 2:
    print("EMPATE")
