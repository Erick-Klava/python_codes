lista=[[], []]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c}° numero: '))
    if valor % 2 ==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(lista[0])
print(lista[1])
