lista=[]
lista0=[]
lista1=[]
while True:
    lista=int(input('Digite um numero: '))
    if lista %2==0:
        lista0.append(lista)
    else:
        lista1.append(lista)

    p=input('Deseja continuar?[S/N]').strip().upper()[0]
    if p in 'Nn':
        break
print(lista)
print(lista1)
print(lista0)
