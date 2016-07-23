from operator import itemgetter

log = True

produtos = ['sushi1', 'sushi2', 'sushi3', 'sushi4', 'sushi5', 'sushi6', 'sushi7', 'sushi8', 'sushi9']
## essa é a lista de produtos (input)

compras = [[0,2,3], [0,1,3], [0,3,4], [0,2,8]] 
## Esse é o dicionário com a relação de compras anteriores (As compras contiveram os produtos 0,2,3 e 0,1,3 e 0,3,4 e 0,2,8)
## os números corresponde ao índice da lista produtos, exemplo [0,2,3] = ['sushi1', 'sushi3', 'sushi4']


i = 0
ii = 0
dicionario = {}


for compra in compras:
	for c in compra:
		i = c
		if i not in dicionario:
			dicionario[i] = 0
		for cc in compra:
			ii = cc
			if(i == ii):
				dicionario[i] += 1
				if(log):
					print('\n# Combinação: || i =', i, '|| ii =', ii, '||') 
					print('## Dicionário Atualizado: ', dicionario)
				
print(sorted(dicionario.items(), key=itemgetter(1), reverse=True))
