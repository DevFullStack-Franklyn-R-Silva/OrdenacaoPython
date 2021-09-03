def merge_sort(lista):
	return divisao(lista)

def divisao(lista):
	#dividir a lista
	lista1 = lista2=[]
	if len(lista)>1:
		meio = len(lista)//2
		lista1 = divisao(lista[0:meio])
		lista2 = divisao(lista[meio:])
		return combinacao(lista1,lista2)
	else:
		return lista

def combinacao(lista1,lista2):
	i = j = 0
	lista = []
	for c in range(len(lista1)+len(lista2)):
		if i == len(lista1):
			lista.append(lista2[j])
			j+=1

		elif j == len(lista2):
			lista.append(lista1[i])
			i+=1

		elif lista1[i]<lista2[j]:
			lista.append(lista1[i])
			i+=1
		else:
			lista.append(lista2[j])
			j+=1
	return lista

print(merge_sort([3,9,5,8,4,0,2]))


	
