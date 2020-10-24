file_name = input('What is the file name?')
file_name_result = file_name.replace('.txt', '_result')

A,C,T,G = 0,0,0,0

with open(file_name) as data:
    nucleotides = data.read()
    nucleotides.upper()
    A = nucleotides.count('A')
    C = nucleotides.count('C')
    T = nucleotides.count('T')
    G = nucleotides.count('G')

with open(file_name_result, 'w') as data:
    data.write(f'{A} {C} {G} {T}')
