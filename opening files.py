file = open('cheese.txt')
for line in file:
    if line.startswith('cheese'):
        print(line)
        
