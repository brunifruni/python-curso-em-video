frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra "a" apareceu {frase.count("A")} vezes')
print(f'A letra "a" aparece pela primeira vez em {frase.find("A") + 1}')
print(f'E pela última vez em: {frase.rfind("A") + 1}')
