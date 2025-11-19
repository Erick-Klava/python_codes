#{}'"\[]

import random
num=int(input('digite um numero inteiro de 0 a 5 : '))
num2=random.randint(0,5)
if num==num2:
    print('VC ACERTOU')
else:
    print('errou bonitao')
print(f'O numero certo era {num2}')