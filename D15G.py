dia=float(input('Digite dias usados com o carro alugado: '))
km=float(input('quanto foi a kilometragem rodada: '))

dia=dia*60
km=km*0.15
total=dia+km
print(f'o total a pagar é {total}')
