file_name = input('What is the file name?')
file_name_result = file_name.replace('.txt', '_result')

with open(file_name) as data:
    nucleotides_DNA = data.read()
    nucleotides_DNA.upper()
    nucleotides_DNA = nucleotides_DNA.replace('T', 'U')
    print(nucleotides_DNA)
    
#criando arquivo resultado
with open(file_name_result, 'w') as data:
    data.write(nucleotides_DNA)
