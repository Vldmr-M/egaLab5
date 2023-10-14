import random
import numpy as np

def findMin():
    minrange=1000
    index=0
    for i in range(len(matrix[0])):
        if (matrix[S[-1]][i] < minrange) and (i in X):
            minrange= matrix[S[-1]][i]
            index=i
    return index



file = open('matrix.txt','r')
matrix=[]
for line in file:
    print(line.split())
    matrix.append([float(x) for x in line.split()])

X=[i for i in range(len(matrix[0]))]
S=[]


nextTown=random.choice(X)
X.remove(nextTown)
S.append(nextTown)
currange = 0

for i in range(len(X)):
    print(f"///////////////////////\nШаг {i+2}")
    print(f"текущий обход - {[x+1 for x in S]}")
    nextTown=findMin()
    currange += matrix[S[-1]][nextTown]
    print(f"Выбран город {nextTown+1}")
    print(f"Расстояние от города {S[-1]+1} до города {nextTown+1} - {matrix[S[-1]][nextTown]}")
    print(f"длина текущего обхода - {currange}")
    X.remove(nextTown)
    S.append(nextTown)

print([x+1 for x in S])
print(f"итоговая длина цикла - {currange}")