numeros=[]
while True:
    n=int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
     print('VALOR DUPLICAO,NAO ADICOINAREI')

    r=str(input('Deseja continuar? [S/N]'))

    if r in 'Nn':
     break
numeros.sort()
print(numeros)