#{ }'"\[ ] >maior <menor
alt=float(input('Entre com a altura utilizando ponto ex(1.95): '))
peso=float(input('Entre com o peso: '))
imc=peso/(alt**2)
print(f'Seu imc é {imc:.2f}')
if imc<18.5:
    print('Abaixo do peso saudavel ')
elif imc>18.5 and imc<25:
    print('Peso ideal')
elif imc>25 and imc<30:
    print('Sobrepeso')
elif imc>30 and imc<40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

