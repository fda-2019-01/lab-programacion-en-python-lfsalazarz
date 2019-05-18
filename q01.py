##
## Imprima la suma de la segunda columna.
##
with open('data.csv', 'r') as f:
    file = f.readlines()
    
    file = [line.replace('\n', '') for line in file]
    file = [line.split('\t') for line in file]
    
    print(sum([int(row[1]) for row in file]))
