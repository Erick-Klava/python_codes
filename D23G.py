#{}'"\[]
#NOTA MENTAL ZFILL SÓ FUNCIONA EM STRING NAO EM NUMEROS E COISAS DO TIPO
#poderia ser feito de forma matematica usando assim mas daria mais trabalho
#tbm nao foi a primeira coisa q passou na minha cabeça ao fazer
'''u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
ai seria só botar um format e botar cada variavel da divisão ali no print e sucesso

'''

num=input('Diga um numero de 0 a 9999: ').zfill(4)
print(f'Unidade é: {num[3]}')
print(f'Dezena é: {num[2]}')
print(f'Centena é: {num[1]}')
print(f'Milhar é: {num[0]}')
