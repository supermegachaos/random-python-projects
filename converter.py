print('''Hi! I can convert temperature from Celsius to Fehrenheit
please enter a temperature in Celsius below''')
count =0
while count == 0:
    celsius = input('please enter a temperature in Celsius')
    try:
        fehrenheit = (float(celsius) * 9/5 +32)
        print( fehrenheit, ' degrees Fehrenheit')
    except:
        print('Please enter a number')
    print('would you like to try again?')
    print('enter yes or no')
    no= input()
    if no == 'no':
        break
