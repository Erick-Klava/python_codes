#{ }'"\[ ]
num=int(input('Entre com um numero inteiro: '))
print(''' Escolha uma base para conversão:
1 PARA BINARIOS
2 PARA OCTAL
3 PARA HEXADECIMAL''')
op=int(input('SUA OPÇÃO? '))
if op==1:
    print(f'ele em binario ficaria: {bin(num)[2:]} ')
elif op==2:
    print(f'ele em octal ficaria: {oct(num)[2:]} ')
elif op==3:
    print(f'ele em hexadecimal ficaria: {hex(num)[2:]}')
