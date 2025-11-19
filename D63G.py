n=int(input('Digite quantidade de termos da fibonacci : '))
t1=0
t2=1
t3=0
print(f'{t1} {t2}',end=' ')
cont=3
while cont<=n:
    t3 = t1 + t2
    print(f'{t3}',end=' ' )
    t1 = t2
    t2 = t3

    cont+=1
print('FIM')

''' n = int(input('Quantos termos quer? '))
a = 0
b = 1
c = 0
cont = 0
while cont < n:
    print('{}'.format(c), end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM') '''

