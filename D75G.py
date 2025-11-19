num = (int(input('Entre com o primeiro valor: ')),
       int(input('Entre com o segundo valor: ')),
       int(input('Entre com o terceiro valor: ')),
       int(input('Entre com o quarto valor: ')))
n=0
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na posição {num.index(3)+1}')
print(f'Os numeros pares foram {n}')
for n in num:
    if n%2==0 and n!=0:
        print(n,end=' ' )
