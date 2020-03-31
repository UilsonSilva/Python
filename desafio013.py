#AUMENTO
n=float(input('Digite o valor R$:'))
p=float(input('Digite a porcentagem de aumento %:'))
#a= (n*1.15)
a=(n+((n/100)*p))
print('Valor de desconto é R$ {:.2f}'.format(a))