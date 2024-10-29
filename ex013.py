#calculo reajuste salarial
sal = float(input('Qual salario do funcionario? '))
novosal = sal *15 /100
reajuste = novosal + sal
print ('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a ganhar {:.2f}\nO reajuste foi de: {}'.format(sal, reajuste,novosal))