#{ }'"\[ ]  menor<   >maior
pm=0
pmi=0
for c in range(1,8):
    ano=int(input('Digite seu ano de nascimento: '))
    idade=2025-ano
    if idade>18:
            pm+=1
            print('vc é de maior')
    else:
            pmi+=1
            print('vc é de menor')
print(f'Existem {pm} pessoas de maior e {pmi} pessoas de menor')




