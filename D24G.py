#{}'"\[]
cidade=str(input('digite seu cidade ')).strip()

print(cidade[:5].upper()=='SANTO')

#pegou as letras pra comparar se com santo da certo,bota tudo pra maisculo pra ficar sem certo
#pensei em inicalmente usar um split pra dividr as palavras da cidade mas esse metodo se mostrou mais eficaz