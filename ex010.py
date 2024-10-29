#conversao de moedas para real
n = float(input('Quantos reais serao convertidos? R$ '))
d = n / 5.64
euro = n / 6.22
yen = n / 0.040
print ('COM R${:.2f} voce pode comprar \nDolares: {:.2f}\nEuros: {:.2f}\nYen: {:.2f}'.format(n, d, euro, yen))


