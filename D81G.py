

list=[]
while True:
    n=int(input('Digite um numero: '))
    list.append(n)
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
list.sort(reverse=True)
print(f'{len(list)} numeros na lista')
print(list)
if 5 in list:
    print('O numero 5 está na lista')
else:
    print('O numero 5 não esta na lista')
