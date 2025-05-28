vel = float(input('Digite a velocidade do veículo: '))
multa = 0
if vel > 80:
    print(f'Você foi multado!')
    multa = (vel - 80) * 7
    print(f'A multa é de R$ {multa:.2f}')
#CONDIÇÃO SIMPLES NÃO PRECISA DO ELSE! PODE DEIXAR SÓ O IF E UM PRINT NO FINAL QUE VALE PARA TODAS AS MENSAGENS
else:
    print('Você está dentro do limite de velocidade!')