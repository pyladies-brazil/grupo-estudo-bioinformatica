n = 6
m = 3
generation_rabbits = [0] * int(m+1) 
generation_rabbits[-1] = 1

for i in range(n-1):
    rabbit_puppies = sum(generation_rabbits[1:-1])
    generation_rabbits[0:-1] = generation_rabbits[1:]
    generation_rabbits[-1] = rabbit_puppies
    

print(sum(generation_rabbits[1:]))
