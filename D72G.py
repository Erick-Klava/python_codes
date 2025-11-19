num='Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Decesseis','Dezessete','Dezoito','Dezenove','Vinte'

while True:
    cont=int(input('Digite um numero de 0 a 20 para ve-lo de forma extensa: '))
    if cont>=0 and cont<=20:
        break
    else:
        print('tente novamente')
print(num[cont])