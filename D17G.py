from math import pow,sqrt
cat1=float(input('entre com o cateto oposto: '))
cat2=float(input('entre com o cateto adjacente: '))
cat1=pow(cat1,2)
cat2=pow(cat2,2)
hipotenusa=sqrt(cat1+cat2)

print(f'sua hipotenusa é {hipotenusa}')