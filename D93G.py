jogador=dict()
partidas=list()
jogador['nome']=str(input('Qual o nome do jogador? '))
tot=int(input('Quantas partidas tem o jogador? '))
for c in range(1,tot+1):
    partidas.append(int(input(f'Quantos gols na {c}° partida ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v} ')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {tot} partida ')
for i,v in enumerate(jogador['gols']):
    print(f'na partida {i} fez {v} gols')
print(f'total de {jogador["total"]} gols')
print('-='*30)