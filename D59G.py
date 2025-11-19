n1=float(input('Digite um numero : '))
n2=float(input('Digite um numero : '))
op=0
while op!=5:
    op=int(input('''Digite sua opção
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR NUMERO
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA
    QUAL SUA ESCOLHA? '''))

    if op==1:
        print(n1+n2)
    elif op==2:
        print(n1*n2)
    elif op==3:
        print(f'o maior numero é {max(n1,n2)}')
        #podia fazer com um comparador de if n1>n2 logo n1 maior e else n2 maior tb
    elif op==4:
        n1 = float(input('Digite um numero : '))
        n2 = float(input('Digite um numero : '))
    elif op==5:
        print('PROGRAMA FINALIZADO')
    else:
        print('Opção invalida')
