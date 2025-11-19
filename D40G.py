#{ }'"\[ ] >maior <menor
m1=float(input('Entre com a 1° nota :'))
m2=float(input('Entre com a 2° nota :'))
mf=(m1+m2)/2
if mf>=7:
    print('Parabens,vc foi aprovado!')
elif mf>=5 and mf<7:
    print('Vc está na recuperação,ainda tem chance!')
else:
    print('vc está reprovado...')
