#atividade 3

#1)

while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota < 0 or nota > 10:
        print("Valor inválido. Digite uma nota entre zero e dez.")
    else:
        break

print("A nota informada é:", nota)

#2)

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha == usuario:
        print("A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        break

print("Usuário:", usuario)
print("Senha:", senha)

#3)

populacao_a = 80000
populacao_b = 200000
anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a * 1.03 # taxa de crescimento de 3% ao ano
    populacao_b = populacao_b * 1.015 # taxa de crescimento de 1.5% ao ano
    anos += 1

print("Serão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a do país B")

#4)

num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

#5)

while True:
    print("Selecione uma opção:")
    print("1 - Somar dois números")
    print("2 - Calcular a potência de um número")
    print("3 - Sair do programa")
    
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:
        # Código para a opção 1
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite o segundo número: "))

        soma = num1+num2
        
        print(f"A soma do {num1} e do {num2} é: {soma}")
        
    elif opcao == 2:
        # Código para a opção 2
        print("Você escolheu a opção 2")
        
    elif opcao == 3:
        # Saída do loop e encerramento do programa
        print("Encerrando o programa...")
        break
        
    else:
        # Opção inválida
        print("Opção inválida. Por favor, digite novamente.")

#6)

notas = []
nota = float(input("Digite a nota do aluno (ou 120 para sair): "))
while nota != 120:
    notas.append(nota)
    nota = float(input("Digite a nota do aluno (ou 120 para sair): "))

media = sum(notas) / len(notas)
print("A média das notas é:", media)