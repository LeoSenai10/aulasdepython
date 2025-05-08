import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH -> (match case) escolha caso (a partir da versão 3.10)
#match valor:
#case valor:

# linguagem = 100

# match linguagem:

#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "Roitman":
#         print("massa")
#     case "lady":
#         print("nasce uma estrela")

#atividade dias da semana

# print("="*8, "DISCOVER WHAT DAY IS TODAY ", "="*8)

# dia = int(input("Digite o dia da semana: "))

# match dia:
    
#     case 1:
#         print("hoje é segunda-feira")
#     case 2:
#         print("hoje é terça-feira")
#     case 3:
#         print("hoje é quarta-feira")
#     case 4:
#         print("hoje é quinta-feira queridinho")
#     case 5:
#         print("hoje é sexta-feira")
#     case 6:
#         print("hoje é sabado")
#     case 7:
#         print("hoje é domingo")
#     case _:
#         print("não queridinho, reveja ou feche")

#atividade do iphone

# print("="*5, "store cerri felipe ", "="*5)

# print("""
# 1 - iphone 15 - R$ 5000.00
# 2 - motorola - R$ 2500.00
# 3 - samsung - R$ 3900.00
      
# fretes por estado
# sp = 10.00
# rj = 15.00
# mg = 20.00
# """)

# print("="*7)

# celular = float(input("digite o número do produto: "))
# estado = float(input("digite a sigla do estado: "))

# print("="*7)

# match celular:
#     case 1:
#         print(f" preço total: {5000.00 + 10.00}")
#     case 2:
#         print(f" preço total: {2500.00 + 15.00 }")
#     case 3:
#         print(f" preço total: {3900.00 + 20.00 }")
#     case 4:
#         print(f" preço total: {5000.00 + 10.00 }")
#     case 5:
#         print(f" preço total: {2500.00 + 15.00 }")
#     case 6:
#         print(f" preço total: {3900.00 + 20.00 }")


# print("="*7)

#correção

# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete

import random

#ativity pedra, papel e teoura

# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


# Desenhos pedra papel tesoura

# papel = """
# #      _______
# # ---'    ____)____
# #            ______)
# #           _______)
# #          _______)
# # ---.__________)
# # """

# pedra = """
# #     _______
# # ---'   ____)
# #       (_____)
# #       (_____)
# #       (____)
# # ---.__(___)
# # """


# tesoura = """
# #     _______
# # ---'   ____)____
# #           ______)
# #        __________)
# #       (____)
# # ---.__(___)

# # """

# print("jogo pedra papel e tesoura")

# jogador = input("digite um item: ")

# match jogador:

#     case _ if jogador == "papel":
#         print("voce escolheu papel")
#         print(f"{papel}")

#     case _ if jogador == "pedra":
#         print("voce escolheu pedra")
#         print(f"{pedra}")

#     case _ if jogador == "tesoura":
#         print("voce escolheu tesoura")
#         print(f"{tesoura}")

#     case _ :
#         print("comando errado")

# sistema = random.randint(1,3)

# match sistema:
#     case _ if sistema == 1:
#         print("a maquina escolheu papel")
#         print(f"{papel}")

#     case _ if sistema == 2:
#         print("a maquina escoheu pedra")
#         print(f"{pedra}")

#     case _ if sistema == 3:
#         print("a maquina escolheu tesoura")
#         print(f"{tesoura}")

# match jogador:
#     case _ if jogador == "pedra" and sistema == 3:
#         print("a maquina venceu")
#     case _ if jogador == "tesoura" and sistema == 3:
#         print("houve empate")
#     case _ if jogador == "tesoura" and sistema == 2:
#         print("a maquina venceu")
#     case _ if jogador == "pedra" and sistema == 2:
#         print("houve empate")
#     case _ if jogador == "pedra" and sistema == 1:
#         print("o jogador venceu")
#     case _ if jogador == "tesoura" and sistema == 1:
#         print("o jogador venceu")
#     case _ if jogador == "papel" and sistema == 1:
#         print("houve empate")
#     case _ if jogador == "papel" and sistema == 2:
#         print("a maquina venceu")
#     case _ if jogador == "papel" and sistema == 3:
#         print("a maquina venceu")
 
 #correção da atividade
#  print("JOGO PEDRA PAPEL TESOURA")

# papel = """
# PAPEL
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
# PEDRA
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
# TESOURA
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

# jogador = input("Escolha entre pedra, papel ou tesoura: ")
# match jogador:
#     case "pedra":
#         jogador=pedra
#     case "tesoura": 
#         jogador =tesoura
#     case "papel":
#         jogador = papel

# #1-> pedra , 2-> papel , 3->tesoura

# maquina = random.randint(1,3)

# match maquina:
#     case 1:
#         maquina=pedra
#     case 2: 
#         maquina =papel
#     case 3:
#         maquina =tesoura


# print(f"voce escolheu  {jogador}")
# print(f"maquina escolheu {maquina}")

# match jogador:
#     case _ if jogador == maquina:
#         print("empate")
#     case _ if jogador==pedra and maquina ==tesoura:
#         print("Voce ganhou")
#     case _ if jogador == tesoura and maquina ==papel:
#         print("Voce ganhou")
#     case _ if jogador == papel and maquina ==pedra:
#         print("voce ganhou")
#     case _ :
#         print("voce perdeu")


# print("2 MODO - PEDRA PAPEL TESOURA")


# print("JOGO PEDRA PAPEL TESOURA ")

# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

# #pedra=1 papel=2 tesoura=3
# mao = input("Digite pedra ou papel ou tesoura :")
# maquina = random.randint(1,3)

# match maquina :
#     case 1:
#         maquina = "pedra"
#     case 2:
#         maquina = "papel"
#     case 3 :
#         maquina ="tesoura"

# match mao:

#     case _ if mao== "pedra" and maquina=="pedra" :
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {pedra}")
#         print("EMPATOU!")
    
#     case _ if mao== "pedra" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {pedra}")
#         print("PERDEU!")
#     case _ if mao== "pedra" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {pedra}")
#         print("GANHOU!")
#     case _ if mao== "papel" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {papel}")
#         print("EMPATOU!")
#     case _ if mao== "papel" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {papel}")
#         print("GANHOU")
#     case _ if mao== "papel" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {papel}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {tesoura}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {tesoura}")
#         print("GANHOU!")
#     case _ if mao== "tesoura" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {tesoura}")
#         print("EMPATOU!")
#     case _:
#         print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")









