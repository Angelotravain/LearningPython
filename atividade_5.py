
#EXERCICIO 1

#ENTRADA DE DADOS DO USUÁRIO
entradaNome1 = input("Digite o primeiro nome/String:");
entradaNome2 = input("Digite o segundo nome/String:");

#SAIDA DE INFORMAÇÃO DIGITADA PELO USUÁRIO COM VALOR DIGITADO E TAMANHO DO VALOR
print(f'Conteúdo da primeira string: {entradaNome1}');
print(f'tamanho da primeira string: {len(entradaNome1)}');
print(f'Conteúdo da segunda string: {entradaNome2}');
print(f'tamanho da segunda string: {len(entradaNome2)}')

#VALIDAÇÃO DE TAMANHO DA STRING E SE OS VALORES DA STRING SÃO IGUAIS
if len(entradaNome1) == len(entradaNome2) and entradaNome1 == entradaNome2:
    print(f'O conteúdo das duas string tem o mesmo tamanho e são iguais!');
elif len(entradaNome1) == len(entradaNome2) and entradaNome1 != entradaNome2:
    print(f'O conteúdo das duas strings tem o mesmo tamanho e não são iguais!');
else:
    print(f'O conteúdo das duas strings não tem o mesmo tamanho e não são iguais!');



# EXERCICIO 2

#ENTRADA DE DADOS 
nomeUsuario = input("Digite seu nome(Maiusculo/minúsculo):");

#RECEBE OS DADOS INVERTE ELES E COLOCA TUDO EM MAÍUSCULO
inverteNome = nomeUsuario[::-1].upper();

#IMPRIME NA TELA O DADO TO_DO MAÍUSCULO E INVERTIDO 
print(inverteNome);


#EXERCICIO 3

#ENTRADA DE DADOS 

texto = """The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. 
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."""

#PASSAGEM DO TEXTO COM O METODO SPLIT PARA DIVIDIR ELE EM PALAVRAS 
palavras = texto.split()

#GUARDA A LISTA DE ITENS 
palavras_python = [p for p in palavras if p[0].lower() in 'python' or p[-1].lower() in 'python']

#IMPRIME A LISTA DE ITENS 
print(palavras_python)


# EXERCICIO 4

#ENTRADA DE DADOS 
nome = input("Digite o seu nome: ")

#LAÇO DE REPETIÇÃO PARA IMPRIMIR AS LETRAS UMA A UMA 
for letra in nome:

#IMPRESSAO DAS LETRAS
    print(letra)

#EXERCICIO 5

#VALIDAÇÃO ENQUANTO NÃO FOR VERDADEIRO VAI CONTINUAR RODANDO
while True:
    #ENTRADA DE DADO PELO USUÁRIO
    cpf = input("Digite o número do CPF (formato: xxx.xxx.xxx-xx): ")

#VALIDAÇÃO SE O TAMANHO DO CPF É DIFERENTE DE 14 CARACTERES, CASO FOR EMITE UMA MENSAGEM
#CASO NÃO FOR VALIDA A PONTUAÇÃO, SE ESTIVER CORRETA ELE VALIDA, SE NÃO REPETE A EXECUÇÃO ATÉ ESTAR CORRETO

    if len(cpf) != 14:
        print("O CPF deve ter 11 dígitos e estar no formato xxx.xxx.xxx-xx")
    elif cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        print("O CPF deve estar no formato xxx.xxx.xxx-xx")
    else:
        print("CPF válido!")
        break

