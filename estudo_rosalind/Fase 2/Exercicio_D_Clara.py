'''
Calcular a média de decendentes com fenotipo dominante. As posições no vetor e as chances são:

1 - AA-AA - 1.00
2 - AA-Aa - 1.00
3 - AA-aa - 1.00
4 - Aa-Aa - 0.75
5 - Aa-aa - 0.50
6 - aa-aa - 0.00

'''
pop = "17005 17293 16715 18015 19287 18826".split()
chance = [2, 2, 2, 1.5, 1, 0]

print(sum(x*int(y) for x,y in zip(chance, pop)))
