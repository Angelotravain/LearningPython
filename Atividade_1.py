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
        
        print(f"A soma do {num1} e do {num2} é: {soma} \n")
        
    elif opcao == 2:
        # Código para a opção 2
        num3 = int(input("Digite um número: \n\n"))

        potencia = num3**num3
        print(f"O valor da potência de {num3} é: {potencia}")
        
    elif opcao == 3:
        # Saída do loop e encerramento do programa
        print("Encerrando o programa...")
        break
        
    else:
        # Opção inválida
        print("Opção inválida. Por favor, digite novamente.")



