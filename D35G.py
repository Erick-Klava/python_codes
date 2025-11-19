#{ }'"\[ ]

a=float(input('Entre com um segmento do triangulo : '))
b=float(input('Entre com um segmento do triangulo : '))
c=float(input('Entre com um segmento do triangulo : '))

if a+b>c and a+c>b and c+b>a:
    print('VC PODE FAZER UM TRIANGULO!' )

else:
    print('vc não pode fazer um triangulo ;( ')