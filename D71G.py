valor=int(input('Digite o valor a ser sacado: '))
total=valor
ced=50
totalced=0
while True:
    if total>=ced:
        total-=ced
        totalced+=1
    else:
        if totalced>0:
            print(f'O numero de cedulas é {totalced} de {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        totalced=0
        if total==0:
            break
