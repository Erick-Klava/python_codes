#{}'"\[]
a=float(input('entre com o 1° numero : '))
b=float(input('entre com o 2° numero : '))
c=float(input('entre com o 3° numero : '))

menor=a
maior=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f' o menor numero é o {menor}')
print(f' o maior numero é o {maior}')