#{ }'"\[ ] >maior <menor
soma=0
for c in range (1,501):
    if  c % 3 ==0:
        if c % 2 ==1:
            print(c)
            soma  +=c


print(f'O total da soma é {soma}')