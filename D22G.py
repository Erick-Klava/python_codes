#{}'"\[]

nome=str(input('Escreva seu nome: ')).strip()

print(f'Seu nome maiusculo é : {nome.upper()}')
print(f'Seu nome minusculo é : {nome.lower()}')
print(f'seu nome inteiro tem isso de letras:  {len(nome)-nome.count(' ')}')
print(f'seu 1° nome tem isso de letras :  {len(nome.split()[0])}')