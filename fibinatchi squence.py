
fib = [0,1] # first 2 values in the fibinatchi sequence
number = int(input('''Hi I can calculate as many terms of the fibbanatchi sequence as you like.
how many terms would you like me to calculate?
Please enter a natral number, positive whole value.
'''))
count =0
print("Fibinati Sequence:")
if number < 0:
    print("Please enter a positive whole number.")
else:
    while number > count :
        fib.append(fib[-1] +fib[-2])
        count += 1
        print(fib[count-1])

print('All done!')
