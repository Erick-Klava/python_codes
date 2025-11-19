from random import randint
def sorteio(lista):
    for cont in range(0,5):
        lista.append(randint(1,10))
    print(f'A lista sorteada foi {lista}')

def somapar(lista):
    soma=0
    par=list()
    for num in lista:
        if num % 2 == 0:
            par.append(num)
            soma+= num
    print(f'A soma dos numeros pares é {soma}')

numeros=list()
sorteio(numeros)
somapar(numeros)