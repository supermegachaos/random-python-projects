import random
def random_flip():
    outcome = random.choice(["Heads","Tails"])
    return outcome
print('I will flip a coin 1000 times. guess how many times it will come up heads')
input()
heads = 0
tails = 0
flips = 0
while flips < 1000 :
    outcome = random_flip()
    if outcome == "Heads":
        heads += 1
        flips += 1
    else:
        tails += 1
        flips += 1

        if flips == 100:
            print(' 100 flips made and there have been ' + str(heads) + ' heads and '
              + str(tails) + ' tails')

        if flips == 500:
            print(' 500 flips made and there have been ' + str(heads) + ' heads and '
              + str(tails) + ' tails')

        if flips == 900:
            print(' 900 flips made and there have been ' + str(heads) + ' heads and '
              + str(tails) + ' tails')
print()
print(' 1000 flips made and there have been ' + str(heads) + ' heads and '
              + str(tails) + ' tails')
print()
print('how close where you?')
