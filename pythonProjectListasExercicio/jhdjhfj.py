N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')

for nota in notas:
    num_nota = N // nota
    N -= nota*num_nota
    print(f'{int(num_nota)} nota(s) de R$ {nota:.2f}')


print('MOEDAS:')
for moeda in moedas:
    num_moeda = N // moeda
    N -= moeda*num_moeda
    print(f'{int(num_moeda)} moeda(s) de R$ {moeda:.2f}')