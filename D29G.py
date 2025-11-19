#{}'"\[]
velo=float(input('Quanto vc estava km/h vc estava andando? '))
multa=(velo-80)*7
if velo<=80:
    print('vc não tomou multa,parabens!Continue assim...')
else:
    print(f'Voce vai ter que pagar {multa} reais...na proxima nao acelere tanto')