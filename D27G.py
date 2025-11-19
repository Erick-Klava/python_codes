#{}'"\[]
nome=str(input('Entre com seu nome: ')).strip()

print(f'Seu nome é :{nome.split()[0]}')
print(f'seu ultimo sobrenome é :{nome.split()[-1]}')
#-1 pega o utlimo q tiver,da pra fazer com o len de nome o nome ou com split q é mais facil
