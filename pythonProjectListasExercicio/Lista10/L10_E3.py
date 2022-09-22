'''
A expressão em Python, m % n, resulta o resto de m ao dividir por n. Defina o máximo divisor
comum (MDC) de dois inteiros, x e y, por:
mdc(x,y) = y se (y<=x && x%y==0)
mdc(x,y) = mdc(y,x) se (x<y)
mdc(x,y) = mdc(y,x%y) caso contrário
Escreva um programa em Python com uma função recursiva para calcular mdc(x,y).
'''