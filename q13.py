##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    filas = [[row[0], sum([int(col.split(':')[1]) for col in row[4].split(',')])] for row in file]
    for letra, suma in filas:
        print(f'{letra},{suma}')
