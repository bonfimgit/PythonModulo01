#pintando parede
largura= float(input('Digite a largura da parede: '))
altura= float(input('Digite a altura da parede: '))
area= largura * altura
print ('Sua parede tem a dimensão de {:.2f}X{:.2f} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print ('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))
