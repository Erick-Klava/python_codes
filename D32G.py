#{}'"\[]
num=int(input('entre com seu ano: '))
if num%4==0 and num%100 !=0 or num%400==0:
    print('SEU ANO É BISSEXTO!')
else:
    print('seu ano não é bissexto!')