ficha = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp in 'Nn':
        break

print('--' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('--' * 35)
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
