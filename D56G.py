#{ }'"\[ ]  menor<   >maior
mediaida=0
mj=0
velho=0
nomevelho=0

for c in range(1,6):
    print(f'------{c}° Pessoa------')
    nome=str(input('Digite seu nome: ')).strip()
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo [M/F]: ')).strip()
    mediaida+=idade
    if sexo in'Ff' and idade <20:
        mj+=1
    elif c==1 and sexo in 'Mm':
        nomevelho=nome
        velho=idade
    elif sexo in 'Mm' and idade>velho:
        nomevelho=nome
        velho=idade





mediaida=mediaida/4
print(f'A media do grupo é {mediaida} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nomevelho}')
print(f'Ao todo são {mj} mulheres com menos de 20 anos')

