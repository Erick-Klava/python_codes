
media=quant=maior=menor=0
resp='S'
while resp in 'Ss':
    num=int(input('Digite um numero: '))
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    media +=num
    quant +=1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num

media=media/quant
print(f'Vc digitou {quant} numeros e a media foi de {media}')
print(F'O maior valor foi {maior} e o menor foi {menor}')
print('FIM')