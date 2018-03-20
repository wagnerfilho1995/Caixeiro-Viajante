#-*- coding: utf-8 -*-
from random import shuffle
from random import randrange
import copy

rota = [i for i in range(0, 10)]

visitados = [0]*10

partida = -1

def partida():
	print("Qual a sua cidade natal?")
	for i in range (0, 10):
		print("Cidade: {}".format(i))
	partida = int(input())
	return partida

# TABELA DE DISTANCIAS ENTRE AS CIDADES
H = [
#	 C0  C1   C2   C3   C4  C5   C6   C7   C8  C9  
	( 0, 30,  84,  56,  -1, -1,  -1,  75,  -1, 80), # C0
	(30,  0,  65,  -1,  -1, -1,  70,  -1,  -1, 40), # C1
	(84, 65,   0,  74,  52, 55,  -1,  60, 143, 48), # C2
	(56, -1,  74,   0, 135, -1,  -1,  20,  -1, -1), # C3
	(-1, -1,  52, 135,   0, 70,  -1, 122,  98, 80), # C4
	(70, -1,  55, -1,   70,  0,  63,  -1,  82, 35), # C5
	(-1, 70,  -1, -1,   -1, 63,   0,  -1, 120, 57),	# C6
	(75, -1, 135, 20,  122, -1,  -1,   0,  -1, -1), # C7
	(-1, -1, 143, -1,   98, 82, 120,  -1,   0, -1), # C8
	(80, 40,  48, -1,   80, 35,  57,  -1,  -1,  0)  # C9
]

L = [
#	C0  C1  C2   C3  C4  C5  C6  C7  C8  C9  
	(0,  1,  1,  1,  0,  0,  0,  1,  0,  1), # C0
	(1,  0,  1,  0,  0,  0,  1,  0,  0,  1), # C1
	(1,  1,  0,  1,  1,  1,  0,  1,  1,  1), # C2
	(1,  0,  1,  0,  1,  0,  0,  1,  0,  0), # C3
	(0,  0,  1,  1,  0,  1,  0,  1,  1,  1), # C4
	(1,  0,  1,  0,  1,  0,  1,  0,  1,  1), # C5
	(0,  1,  0,  0,  0,  1,  0,  0,  1,  1), # C6
	(1,  0,  1,  1,  1,  0,  0,  0,  0,  0), # C7
	(0,  0,  1,  0,  1,  1,  1,  0,  0,  0), # C8
	(1,  1,  1,  0,  1,  1,  1,  0,  0,  0)  # C9
]

def avaliar(aux, x, filho):
	if(aux != -1 and aux < x):
		rota = filho
		print("... Mudou a rota para {} ...".format(rota))
		return aux
	else:
		return x

def swap_rota(a, x, y):
	
	filho = copy.copy(a)
	temp = filho[x]
	filho[x] = filho[y]
	filho[y] = temp
	
	return filho

def tour(rota):
	if len(rota) == 11:
		del rota[10]
	shuffle(rota)
	rota.append(partida)
	for j in range(0, 10):
		if rota[j] == rota[10]:
			temp = rota[0]
			rota[0] = rota[j]
			rota[j] = temp
			break

def rota_possivel(a):
	km = 0
	for i in range (0, len(a)-1):
		if L[a[i]][a[i+1]] == 0:
			#print("Invalido: {}".format(a))
			return -1
		km += H[a[i]][a[i+1]]
	return km

# MAIN

partida = partida()
tour(rota)

# ACHAR PRIMEIRO CAMINHO VÁLIDO ( INÍCIO ALEATÓRIO )
x = rota_possivel(rota)
k = 0
while x == -1 and k < 10000:
	tour(rota)
	x = rota_possivel(rota)
	k += 1
print("Procurou, achou!")
print("Em exatas {} tentativas".format(k))

print("A rota é: {}".format(rota))
print("Serão percorridos: {} km".format(rota_possivel(rota)))

# PRONTO, AGORA VOCÊ CONHECE UM CAMINHO RANDOMICO POSSÍVEL, QUE FAZ UM TOUR VISITANDO TODAS AS CIDADES, PARTINDO 
# DE UM PONTO INICIAL E VOLTANDO ATÉ ELE NO FINAL

print("PERMUTAR 2 A 2")

filho1 = filho2 = filh3 = copy.copy(rota)
i = 0

#	TROQUE DUAS POSIÇÕES ALEATÓRIAS
while i < 50000:
	#	TROQUE DUAS POSIÇÕES ALEATÓRIAS
	p = randrange(1, 10)
	q = randrange(1,10)
	filho1 = swap_rota(filho1, p, q)
	custo_filho1 = rota_possivel(filho1)
	x = avaliar(custo_filho1, x, filho1)

	r = randrange(1, 10)
	s = randrange(1,10)
	filho2 = swap_rota(filho1, r, s)
	custo_filho2 = rota_possivel(filho2)
	x = avaliar(custo_filho1, x, filho2)

	t = randrange(1, 10)
	u = randrange(1,10)
	filho3 = swap_rota(filho1, t, u)
	custo_filho3 = rota_possivel(filho3)
	x = avaliar(custo_filho1, x, filho3)

	i += 1

print("Achei uma melhor rota e ela é: {}".format(rota))
print("Serão percorridos: {} km".format(x))
