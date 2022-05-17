'''
AVALIAÇÃO 05 - TRIÂNGULO DE PASCAL

Gabriel Barros de Melo Amorim - RA: 574015
Cesar Augusto de Almeida - RA: 626848
Danielle Barros Bassetto - RA: 629391
João Vitor Adonis - RA: 590428
Marllon Silva Araujo Coelho - RA: 627021
Matheus Henrique de Lima - RA: 626732
'''

n = int(input())

t = []
for i in range(n):
    t.append([])
    for j in range(i+1):
        if j == 0 or i == j:
            t[i].append(1)
        else:
            t[i].append(t[i-1][j-1] + t[i-1][j])

for i in range(n):
    for j in range(i+1):
        print(f"{(t[i][j]):2}", end=" ")
    print()


