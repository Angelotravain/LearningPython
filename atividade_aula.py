
#while True:
 #   palavraPalindrome = input('Digite uma palavra:');

  #  if (palavraPalindrome == palavraPalindrome[::-1]):
   #     print('A palavra é palindrome!');
   # else:
   #     print('A palavra não é palindrome!');

palavraSecreta = input('Digite uma palavra:');
vogais = "aeiou";
saida = "";
for letra in palavraSecreta:
    if( letra in vogais ):
        saida = saida + "*";
    else:
        saida = saida + letra;

print(saida);