"""
texto = 'Python'

novo_texto = ''
for letra in texto:
  novo_texto += f'*{letra}'
  print(letra)

print(f'{novo_texto}*')

"""

## range + for para usar intervalos de números

numeros = range(0, 15, 2)

for numero in numeros:
  print(numero)