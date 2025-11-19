listnum=[]
for c in range(0,5):
    listnum.append(int(input(f"Digite um numero na posição {c} :")))
print(f'menor valor na posição {listnum.index(min(listnum))} e é {min(listnum)}')
print(f'maior valor na posição {listnum.index(max(listnum))} e é {max(listnum)}')

print(listnum)
