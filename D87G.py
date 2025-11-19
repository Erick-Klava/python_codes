matriz=[[0,0,0],[0,0,0],[0,0,0]]
spar=0
ster=0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor para [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            spar=spar+matriz[l][c]

ster=matriz[0][2]+matriz[1][2]+matriz[2][2]
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {ster}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
