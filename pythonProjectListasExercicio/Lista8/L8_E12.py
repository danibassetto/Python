'''O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de
substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto
abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria
substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente um programa que faça
uso desse Código de César (3 posições), entre com uma string e retorne a string codificada.
Exemplo:
String: a ligeira raposa marrom saltou sobre o cachorro cansado
Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR'''

string = input("Informe uma string: ").upper()
cripto = ''
for letra in string:
    if letra == 'X':
        cripto += 'A'
    elif letra == 'Y':
        cripto += 'B'
    elif letra == 'Z':
        cripto += 'C'
    elif letra.isalpha():
        cripto += chr(ord(letra) + 3)
    else:
        cripto += letra

print(cripto)

