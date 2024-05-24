file = []
count = 0
this = 0
addition = 0
done = 'no'
print ("please enter a number to get the avrage and sum and average of the numbers")
while this ==0 :
    print(" enter a number")
    try:
        num = float(input())
        file.append(num)
        count += 1
        addition += file[-1]
        print("do you want to enter another number enter yes or no")
        done = input()
        if done == 'no':
            this =+1
    except:
        print('unexpected input please enter a number')
        
    
print( "your number were:", file, "the addition of these numbers: ", addition, "the avraage: ", addition/count)
print(count)
print(addition)
