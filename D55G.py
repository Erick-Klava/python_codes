#{ }'"\[ ]  menor<   >maior
maior=0
menor=0
for p in range (1,6):
    peso=float(input(f'digite o da peso {p}° pessoa:  '))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        elif peso<menor:
            menor=peso
print(f'o mairo peso foi de {maior}')
print(f'o menor peso foi de {menor}')