contp=0
cont=0
barato=''
total=0
while True:
    produto=str(input('Digite o nome do produto: '))
    preco=float(input('Digite o valor do produto: '))
    resp=0
    total+=preco
    cont+=1
    if cont==1:
        barato=produto
        menor=preco
    else:
        if preco<menor:
            menor=preco
            barato=produto
    if preco >1000:
        contp+=1

    resp=int(input('Quer continuar? [0-SIM,1-NÃO] '))
    if resp==1:
        break

print(f'Total da compra é {total}')
print(f'A quantidade de produtos mais caros que 1000 reais é {contp}')
print(f'O produto mais barato foi {barato} custando {menor}')
