import random

def shell_sort(lista):
	h = 1
	while h<len(lista):
		if 3*h+1 < len(lista):
			h = 3*h+1
		else:
			break
	print('h: ',h)
	while h!=1:
		h = h//3
		print('h: ',h)
		for i in range(h,len(lista)):
			aux = lista[i]
			j = i
			while lista[j-h]>aux:
				lista[j] = lista[j-h]
				j-=h
				if j<h:
					break
			lista[j] = aux
	return lista	

lista = []
for i in range(20):
	lista.append(random.randint(0, 100))
print(lista)
print(shell_sort(lista))