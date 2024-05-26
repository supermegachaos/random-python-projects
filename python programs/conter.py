import time
def countName():
    print ( 'hi what is your name?')
    yourName = input()
    time.sleep(2)
    print ( yourName + ' has ' + str(len(yourName)) + ' letters.')
    
