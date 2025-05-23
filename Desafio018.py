from math import radians,sin,cos,tan
a = float(input('Digite o ângulo do triângulo: '))
seno = sin(radians(a))
print(f'O ângulo de {a} tem o SENO de {seno:.2f}')
cosseno = cos(radians(a))
print(f'O ângulo de {a} tem o COSSENO de {cosseno:.2f}')
tan = tan(radians(a))
print(f'O ângulo de {a} tem a tangente de {tan:.2f}')