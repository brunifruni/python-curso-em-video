nome = input('Digite seu nome completo: ')
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {(nome.upper())}')
print(f'Seu nome em minúsculas é {(nome.lower())}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
#ou podemos fazer o ultimo assim::
#sep = nome.split()
#print(f'Seu primeiro nome é {sep[0]} e ele tem {len(sep[0])} letras.)