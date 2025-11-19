#{ }'"\[ ]
casa=float(input('Qual o valor da casa? '))
sal=float(input('Quanto é o seu salario? '))
anos=int(input('Quantos anos de financiamento? '))
prest= casa/(anos*12)
print(f'pra pagar uma casa de {casa:.2f} em {anos} anos ,a prestação seria de {prest:.2f} reais')
if prest>(sal*0.30):
    print('Seu emprestimo foi NEGADO!')
else:
    print('Seu emprestimo foi APROVADO!')