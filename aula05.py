import os
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#atividade da nota
#replace("valor1", "valor2") -> subsitui o valor 1 pelo valor 2

# nota1 = float(input("nota da primeira avaliaçao: ").replace(",","."))
# nota2 = float(input("nota da segunda avaliação: ").replace(",","."))

# media = (nota1+nota2)/2
# #: .2F -> foimata para duas casas decimais apenas no fstring
# print(f"media : {media:.2f}")

# if media <5:
#     print("reprovado")
# elif media >=5 and media<=7:
#     print("em recuperacao")

# else:
#     print("aprovado")

#ativ3
# peso = int(input("digite o seu peso: ").replace(",","."))
# altura = float(input("digite sua altura: ").replace(",","."))

# imc = peso/(altura*altura)

# if imc <17 :
#     print("muito abaixo do peso com" + imc )
# elif imc >= 17 and imc <= 18.49:
#     print("abaixo do peso com" + imc )
# elif imc >= 18.5 and imc <= 24.99:
#     print("peso normal de " + imc )
# elif imc >= 25 and imc <= 29.99:
#     print("acima do peso com" + imc )
# elif imc >= 30 and imc <= 34.99:
#     print("foi identificado obesidade tipo 1 com" + imc )
# elif imc >= 35 and imc <= 39.99:
#     print("foi identificado obesidade tipo 2 com" + imc)
# elif imc <40:
#     print("voce foi identificado com obesidade morbida com" + imc)

#atividade do carro

salario = float(input("digite seu salario: ").replace(","+"."))
if salario >= 2799.99:
    aumento = salario * 20/100
    print(" o aumento sera de 20%, com o salário de", aumento)
elif salario == 2000.00 and salario == 6999.99:
    aumento = salario * 15/100
    print("o aumento sera de ")



