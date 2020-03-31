# ALUGUEL DE CARRO
print('')
d= int(input('Digite quantidade de dias alugou o carro:'))
k= float(input('Digite quantidade de Km percorrido o carro:'))
v= (60 * d) + (k * 0.15)
print('Dias de locação do carro: {}, KM {} rodado, total a pagar R${:.2f}'.format(d,k,v))