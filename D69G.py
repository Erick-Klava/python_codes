hom=p18=m20=cont=0
while True:
    idade = int(input('Qual a sua idade?'))
    sexo = str(input('Qual o seu sexo?[M/F]')).upper().strip()[0]
    cont=str(input('Deseja continuar?[S/N]')).upper().strip()[0]

    if idade >= 18:
        p18+=1
    if sexo == 'M':
        hom+=1
    if sexo == 'F' and idade < 20:
        m20+=1
    if cont== 'N':
        break
print(f'Tem {p18} pessoas maiores de 18 anos. ')
print(f'Tem {hom} homens cadastrados.')
print(f'Tem {m20} mulheres menores de 20 anos cadastradas.')