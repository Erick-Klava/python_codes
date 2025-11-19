#{ }'"\[ ] >maior <menor
import random
import time

print('''PEDRA PAPEL E TESOURA
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
joga=int(input('Qual a sua jogada: '))
bot=random.randint(1,3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print('=-='*8)
print(f'JOGADOR JOGOU {joga}')
print(f'BOT JOGOU {bot}')
print('=-='*8)
if bot == joga:
    print('EMPATE')
elif bot == 1 and joga == 2:
    print('JOGADOR GANHOU')
elif bot == 2 and joga ==3:
    print('JOGADOR GANHOU')
elif bot == 3 and joga == 1:
    print('JOGADOR GANHOU')
else:
    print('JOGADOR PERDEU')
