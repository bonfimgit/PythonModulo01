""" Crie um programa que leia o nome completo de uma pessoa e mostre:maiúsculas,minúsculas,quantidades de letras do nome  """
nome = str(input('Digite seu nome completo:')).strip()
print ('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print ('Seu nome em minúsculas é {}'.format(nome.lower()))
print ('Quantidades de letras do nome {}'.format(len(nome) - nome.count(' ')))
print ('Quantidades de letras do primeiro nome nome {}'.format(nome.find (' ')))
