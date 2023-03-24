# Atividade 2

#1)

ano = int(input("Digite o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#2)

peso = float(input("Digite o peso dos peixes em kg: "))
limite = 50.0
excesso = 0.0
multa = 0.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.0

print(f"Peso dos peixes: {peso} kg")
if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a pagar: R$ {multa:.2f}")
else:
    print("Não há excesso de peso. Multa: R$ 0.00")

#3)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(f"O maior número é: {maior}")

#4)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")


#5)

import math

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = area / 3
latas = math.ceil(litros / 18) # round up to nearest integer
preco_total = latas * 80

print(f"Você precisará de {latas} latas de tinta, ao preço total de R${preco_total:.2f}.")

#6)

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("Os valores formam um triângulo!")
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")
