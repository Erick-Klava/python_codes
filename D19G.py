import random

aluno1=str(input('entre com o nome do 1° aluno: '))
aluno2=str(input('entre com o nome do 2° aluno: '))
aluno3=str(input('entre com o nome do 3° aluno: '))
aluno4=str(input('entre com o nome do 4° aluno: '))

listaluno=[aluno1,aluno2,aluno3,aluno4]
escolha=random.choice(listaluno)
print(f'VC FOI SORTEADO(A) {escolha} PARABENS!')
