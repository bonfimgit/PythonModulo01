'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''
from math import radians,sin,cos,tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print ('O seno de {} temm o SENO de: {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O cosseno de {} tem o COSSENO de: {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de: {:.2f}'.format(angulo, tangente))