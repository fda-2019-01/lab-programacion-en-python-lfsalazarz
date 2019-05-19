##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
from itertools import groupby
from operator import itemgetter


with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    data_col5 = [y.split(':')[0] for row in file for y in row[4].split(',')]
    keys = sorted(list(set(data_col5)))
    tabla = [(key, data_col5.count(key)) for key in keys]

    for k,c in tabla:
        print(f'{k},{c}')
