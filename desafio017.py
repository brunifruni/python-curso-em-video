from math import hypot
x = float(input('Digite o cateto oposto: '))
y= float(input('Digite o cateto adjacente: '))
print(f'A hipotenusa do triangulo retângulo é de {hypot(x,y):.2f}')
