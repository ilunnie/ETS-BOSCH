nomeCompleto = input('Digite seu nome completo: ').lower()
nome = nomeCompleto.split(' ')

print('\n'*3)
for palavra in nome:
    print(palavra.capitalize(), end=' ')
    
caracteres = len(nomeCompleto.replace(' ', ''))
print(f'\nSeu nome possuí {caracteres} caracteres')