#{ }'"\[ ] >maior <menor
valor=float(input('Entre com a quantidade de valor: '))
print('''SELECIONE A FORMA DE PAGAMENTO.
[1]A vista dinheiro/pix 10% de desconto
[2]A vista cartão 5% de desconto
[3]2x cartão sem juro
[4]3x cartão com juros de 20%
''')
pag=int(input('Qual a sua decisão ? '))
if pag==1:
    print(f'O valor fica {valor-valor*0.10} com desconto de 10%')
elif pag == 2:
    print(f'O valor fica {valor - valor * 0.05} com desconto de 5%')
elif pag == 3:
    print(f'O valor fica 2x {valor/2} sem juros total = {valor}')
elif pag == 4:
    print(f'O valor fica 3x {(valor*0.20+valor)/3} com juros de 20%')
else:
    print('invalido.')


