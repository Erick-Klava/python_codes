#{ }'"\[ ] >maior <menor
idade=int(input('Entre com a idade,atlteta: '))
if idade<=9:
    print('Vc é um atleta mirim!')
elif idade>9 and idade<=14:
    print('Vc é um atleta infantil!')
elif idade>14 and idade<=19:
    print('Vc é um atleta junior!')
elif idade>19 and idade<=20:
    print('Vc é um atlteta senior!')
else:
    print('Vc é um atleta master!')