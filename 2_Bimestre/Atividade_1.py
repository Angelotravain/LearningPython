# Exercicio 1
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

while True:
    print("----- MENU -----")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = soma(num1, num2)
        print("Resultado da soma:", resultado)
        print()
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = subtracao(num1, num2)
        print("Resultado da subtração:", resultado)
        print()
    elif opcao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = multiplicacao(num1, num2)
        print("Resultado da multiplicação:", resultado)
        print()
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = divisao(num1, num2)
        print("Resultado da divisão:", resultado)
        print()
    elif opcao == "0":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        print()
## --------------------------------------------------
## Exercicio 2
def realizar_operacao(operacao, a, b):
    if operacao == "1":
        return a + b
    elif operacao == "2":
        return a - b
    elif operacao == "3":
        return a * b
    elif operacao == "4":
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não é permitida"

while True:
    print("----- MENU -----")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa finalizado.")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        print()
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = realizar_operacao(opcao, num1, num2)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        print("Resultado:", resultado)
    
    print()
## -----------------------------------------------
## Exercicio 3
def trocar_valores(a, b):
    return b, a

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

print("Valores originais - X:", x, "Y:", y)

x, y = trocar_valores(x, y)

print("Valores trocados - X:", x, "Y:", y)

## -------------------------------------------
## Exercicio 4
def verificar_sinal(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Neutro'

valor = float(input("Digite um número: "))

resultado = verificar_sinal(valor)

print("Resultado:", resultado)
## ---------------------------------------------
## Exercicio 5
def reverso(numero):
    reverso = 0
    while numero > 0:
        ultimo_digito = numero % 10
        reverso = reverso * 10 + ultimo_digito
        numero = numero // 10
    return reverso

numero = int(input("Digite um número inteiro: "))
resultado = reverso(numero)
print("Reverso:", resultado)

