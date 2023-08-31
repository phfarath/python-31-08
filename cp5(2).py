#matriz 5x5
import random

matriz=[
    
]
soma1=0
soma2=0
linhas= 5 
col=5
cont=0
for i in range (0,linhas,1):
    linha=[]
    for j in range(0,col,1):
        valor = int(random.randint(10,30))
        linha.append(valor)
    matriz.append(linha[:])
print(matriz)

#somando 
for i in range(0,(len(matriz))):
    while cont<4:
        soma1+=i
        cont+=1
    print(soma1)

        
    
               

