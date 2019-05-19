##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    letras = [[letra, row[1]] for row in file for letra in row[3].split(',')]
    for key, group in groupby(sorted(letras, key=itemgetter(0)), itemgetter(0)):
        print(f'{key},{sum([int(g[1]) for g in group])}')
