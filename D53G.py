#{ }'"\[ ]  menor<   >maior
#SOLUÇÃO PROFESSOR
'''
frase=str(input('Digite uma frase: ')).strip().upper()
pal=frase.split()
junto=''.join(pal)
inv=''
for letra in range(len(junto)-1,-1,-1):
    inv+=junto[letra]

if inv==junto:
    print('A frase digitada é um palidnromo')
else:
    print('A frase digitada não é um palindromo')'''

#SOLUÇÃO COMENTARIO,achei mais simples
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
