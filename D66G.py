n=0
soma=0
cont=0
n=int(input('Digite um numero [999 pra sair]: '))
while True:
    if n==999:
        break
    soma += n
    cont += 1
    n=int(input('Digite um numero [999 pra sair]: '))

print(f'Voce digitou {cont} numeros e a soma foi de {soma}\nFIM')
