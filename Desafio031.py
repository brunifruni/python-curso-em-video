print('-' * 10, 'CALCULADORA PREÇO DE VIAGEM', '-' * 10)
dist = float(input('Qual a distância da viagem em Km? '))
if dist <= 200:
    passagem = dist * 0.50
    print(f'O preço da passagem é de R$ {passagem}')
else:
    passagem = dist * 0.45
    print(f'O preço da passagem é de R$ {passagem}')