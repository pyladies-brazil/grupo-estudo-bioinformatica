#!/usr/bin/python3

#C - Counting Point Mutations

path = './rosalind_hamm.txt'

dataset = open(path,'r')

list = []
count = 0

for line in dataset:
    line = line.strip()
    list.append(line)

for i in range(0,len(list[0])):
    if list[0][i] != list[1][i]:
        count += 1

print(count)
dataset.close()