a = [5,10,3,2,1,20,100,25,-4]

lowestSoFar = a[0]

for low in a:
    if lowestSoFar >= low:
        print('Lowest so far:',low, 'previous low:', lowestSoFar,)
        lowestSoFar = low

