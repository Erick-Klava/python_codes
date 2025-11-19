import random

aluno1 = input('Entre com o nome do 1° aluno: ')
aluno2 = input('Entre com o nome do 2° aluno: ')
aluno3 = input('Entre com o nome do 3° aluno: ')
aluno4 = input('Entre com o nome do 4° aluno: ')

listaaluno = [aluno1, aluno2, aluno3, aluno4]

escolha=random.shuffle(listaaluno)
print(f'a ordem a aleatoria é: {listaaluno} ')
