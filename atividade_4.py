import random

# Exercicio 1
lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

maior = lista[0]
menor = lista[0]
for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Lista:", lista)
print("Maior valor:", maior)
print("Menor valor:", menor)

# Exercicio 2
lista = []
for i in range(20):
    lista.append(random.randint(1, 100))

pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista completa:", lista)
print("Números pares:", pares)
print("Números ímpares:", impares)

# Exercicio 3
vetor1 = []
vetor2 = []
for i in range(10):
    vetor1.append(random.randint(1, 100))
    vetor2.append(random.randint(1, 100))

vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3 intercalado:", vetor3)

# Exercicio 4

vetor = [0] * 20

for i in range(20):
    if i % 2 == 0:
        vetor[i] = 1
    else:
        vetor[i] = 0

print("Vetor preenchido de acordo com a posição:", vetor)
