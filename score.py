print('please enter a score between 0.0 and 1.0')
count = 0
while count == 0:
    try:
        score = float(input())
    
        if score > 1.0 or score < 0: 
            print("invalid entry scores values must be beween 0 and 1")
            print()
            print("Please enter a valid entry")
        elif score >= 0.9 and socre <=1.0:
            print( "Good job A+ ", "your score was", (score*100))
            count += 1
        elif score >=0.8:
            print("Not bad B+ I know you can do better", "your score was", (score*100))
            count += 1
        elif score >=0.7:
            print("A C+ is passing but try a little harder next time", "your score was", (score*100))
            count += 1
        elif score >=0.6:
            print(" D+ I know you can do better than this you were so close", "your score was", (score*100))
            count += 1
        elif score >=0 and score < 0.6:
            print("F you need more practice", "your score was", (score*100//1))
            count += 1
    except:
        print("the score entered needs to be between 0 and 1.0 and a valid number")
        
