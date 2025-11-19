pessoa={'nome':'',
        'idade':'',
        'ctps':'',
        'contratação':'',
        'salario':''}
nome=str(input('Qual o seu nome? '))
idade=int(input('Qual ano de nascimento? '))
idade=2025-idade
ctps=int(input('Qual a carteira de trabalho[0 NÃO TEM]? '))
if ctps!=0:
    contratação=int(input('Ano de contratação: '))
    contratação=2025-contratação
    salario=float(input('Qual seu salario? '))
    if contratação>35:
        print(contratação)
        print('pode se aposentar')
    else:
        print(contratação)
        print('não pode se aposentar')
print('-='*30)


