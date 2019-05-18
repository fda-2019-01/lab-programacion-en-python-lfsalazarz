##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    group = [[key, len(list(group))] for key, group in groupby(sorted(file, key=itemgetter(0)), itemgetter(0))]
    
    for element in group:
        print(f'{element[0]},{element[1]}')
