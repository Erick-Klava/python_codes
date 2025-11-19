#{}'"\[]
km=float(input('Digite a distancia em km da viagem: '))

if km<=200:
    print(f'o preço da sua passagem é {km*0.5}reais')
else:
    print(f'o preço da sua passagem é {km*0.45}reais')