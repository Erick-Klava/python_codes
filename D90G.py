aluno={'nome':'','media':''}
nome=str(input('Digite o nome do aluno: '))
media=float(input('Digite a media do aluno:'))
if media>7:
    print('Aluno aprovado')

if media<5:
    print('reprovado')

if media<7 and media>=5:
    print('recuperação')

