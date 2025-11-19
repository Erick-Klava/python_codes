import random


bot=random.randint(0,10)

acert=int(input('ADIVINHE O NUMERO Q EU ESTOU PENSANDO DE 0-10: '))
while acert != bot:
    acert=int(input('vc errou,tente novamente um numero de 0-10: '))
print('VC ACERTOU PARABENS!')
