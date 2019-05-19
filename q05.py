##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    for key, group in groupby(sorted(file, key=itemgetter(0)), itemgetter(0)):
        g = list(group)
        max_g = max(int(x[1]) for x in g)
        min_g = min(int(x[1]) for x in g)
        print(f'{key},{max_g},{min_g}')
