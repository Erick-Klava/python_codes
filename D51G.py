#{ }'"\[ ]  menor<   >maior
p1=int(input('Digite um numero: '))
razao=int(input('Digite a razão: '))
dez=p1 +(10)*razao

for c in range(p1,dez,razao):
    print(c)
