
fib = [1,1]
x=0
while x < 100:
    fib.append(fib[-1] +fib[-2])
    x += 1
print(fib)

