tim=('Palmeiras','Flamengo','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','São Paulo','Vasco','Corinthians',
     'Atlético-MG','Bragantino','Ceará','Grêmio','Internacional','Vitória','Santos','Juventude','Fortaleza','Sport')

print(f'A lista de Times na ordem é {tim}')
print(f'Os 5 primeiros da lista são: {tim[:5]}')
print(f'Os 5 ultimos da lista são {tim[-5:]}')
print(f'Os times em ordem alfabetica são{sorted(tim)}')
print(f'O Fluminense está na posição de {tim.index("Fluminense")+1}')
print(f'Chapecoense está fora da serie A')