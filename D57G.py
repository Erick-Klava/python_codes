#{ }'"\[ ]  menor<   >maior



sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo=str(input('Opção invalida,tente novamente [M/F]:')).strip().upper()[0]
print(f'Sexo registrado {sexo}')
