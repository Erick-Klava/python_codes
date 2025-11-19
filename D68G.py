import random
import time
escolha=0
n1=0
n2=0
print('--==BEM VINDO AO PAR OU IMPAR==--')
while True:
    escolha=int(input('Digite 0 para par e 1 para impar: '))
    if escolha==0:
        n1=int(input('Digite um numero:'))
        n2=random.randint(1,10)
        print('Do')
        time.sleep(0.5)
        print('Lá')
        time.sleep(0.5)
        print('Si')
        time.sleep(0.5)
        print('JÁ')
        print(f'O computador jogou {n2}')
        if(n1 + n2) % 2 == 0:
            print('Par,voce ganhou,jogue novamente!')
        else:
            print('voce infelizmente perdeu desa vez...\nBoa sorte nas proximas!')
            break
    elif escolha==1:
        n2=int(input('Digite um numero:'))
        n1=random.randint(1,10)
        print('Do')
        time.sleep(0.5)
        print('Lá')
        time.sleep(0.5)
        print('Si')
        time.sleep(0.5)
        print('JÁ')
        print(f'O computador jogou {n1}')
        if (n1 + n2) % 2 == 1:
            print('Impar,voce ganhou,jogue novamente!')
        else:
            print('voce infelizmente perdeu desa vez...\nBoa sorte nas proximas!')
            break
