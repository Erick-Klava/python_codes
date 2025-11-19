temp=[]
princ=[]
mai=men=0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len (princ)==0:
        mai=men=temp[1]
    else:
        if temp[1] > mai:
            mai=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'nN':
        break

print(f'foram cadastradas {len(princ)} pessoas')
print(f'o maior peso foi de {mai}kg,peso de ', end='')
for p in princ:
    if p[1]==mai:
      print(f'{p[0]} ',end='')
print(f'\nO menor peso foi de {men}kg')
for p in princ:
    if p[1]==men:
      print(f'{p[0]} ',end='')



