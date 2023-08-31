#matriz 5x5
import random

matriz=[
    
]
soma_linha4=0
soma_col2=0
soma_d1=0
soma_d2=0
soma_geral=0
linhas= 5 
col=5
for i in range (0,linhas,1):
    linha=[]
    for j in range(0,col,1):
        valor = int(random.randint(10,30))
        linha.append(valor)
        soma_geral+=valor
    matriz.append(linha[:])
print(matriz)
#somando elementos da matriz linha 4
for i in matriz[3]:
    soma_linha4+=i
print(soma_linha4)

#somando a segunda coluna da matriz
for i in range(0,len(matriz)):
    soma_col2+= matriz[i][1]
print(soma_col2)

#somando d principal
for i in range (0,(len(matriz))):
    soma_d1+= matriz[i][i]
print(soma_d1)

#somando d secundaria
for i in range (0,(len(matriz))):
    soma_d2+= matriz[i][-(i+1)]
print(soma_d2)

#somando todos os valores
print(soma_geral)