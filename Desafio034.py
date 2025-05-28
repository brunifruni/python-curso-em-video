sal = float(input('Digite o salário do funcionário: R$ '))
if sal <= 1.250:
    nsal = sal + (sal * 15 / 100) #para aumentar 15%
else:
    nsal = sal + (sal * 10 / 100) #para descontar só substituir o + pelo -
print(f'O novo salário do funcionário com o aumento é de {nsal}')
