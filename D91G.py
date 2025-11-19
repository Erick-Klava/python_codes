from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador1':randint(1,6),
      'jogador2':randint(1,6),
      'jogador3':randint(1,6),
      'jogador4':randint(1,6)}
ranking=list()
print('VALORES SORTEADOS')
for k,v in jogo.items():
    print(f'O jogador{k} tirou {v} nos dados')
    sleep(0.5)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° para o jogador {v[0]} q tirou {v[1]} nos dados')
