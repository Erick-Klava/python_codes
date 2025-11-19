def contador(i, f, p):
    if i<f:
        for c in range(i,f+1,p):
            print(c)
        print('FIM')
    elif i>f:
        for c in range(i,f-1,-p):
            print(c)
        print('FIM')
    else:
        print('**Função desnecessaria,programa encerrado**')


contador(1,10,1)
contador(10,0,2)
i=int(input('Diga o primeiro numero da PA: '))
f=int(input('Diga ate que numero voce quer essa PA : '))
p=int(input('Diga a razao da PA : '))

contador(i, f, p)
