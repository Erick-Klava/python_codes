#{ }'"\[ ]
anon=int(input('Entre com o ano de seu nascimento: '))
anoa=int(input('Entre com o ano atual: '))
idade=anoa-anon
if idade<18:
    print(f'Falta {18-idade} anos pra vc se alistar.')
elif idade==18:
    print('Vc deve se alistar esse ano. ')
else:
    print(f'Já se passaram {idade-18} desde seu alistamento')