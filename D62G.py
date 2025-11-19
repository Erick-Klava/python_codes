prt=int(input('Digite o numero q começa a PA : '))
razao=int(input('Digite a razao PA : '))
c=0
total=0
mais=10
while mais!=0:
    total+=mais
    while c!=total:
        print(f'{prt} ',end='')
        prt+=razao
        c += 1
    mais=int(input('''\nDeseja continuar essa sequencia em quantos numeros?\n(0=SAIR): '''))



print('FIM')