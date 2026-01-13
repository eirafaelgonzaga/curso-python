### Calculadora de IMC utilizando fundamentos iniciais de Python.

nome = input('Digite seu nome: ')
altura = input('Digite sua altura: ')
peso = input('digite seu peso: ')

altura_real = float(altura)
peso_real = float(peso)

imc = peso_real / (altura_real * altura_real)

linha_1 = f'{nome} tem {altura_real}cm de altura, ' 
linha_2 = f'pesa {peso}kg e seu imc é, '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

if imc <= 18.5:
  print('Abaixo do peso.')
elif imc <= 24.9:
  print('Peso saudável.')
elif imc <= 29.9:
  print('Sobrepeso')
elif imc <= 34.9:
  print('Obesidade grau I')
elif imc <= 39.9:
  print('Obesidade grau II Severa') 
else:
  print('Obesidade grau III Mórbida') 