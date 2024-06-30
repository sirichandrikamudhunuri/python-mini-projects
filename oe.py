import random
def play():
    user = input("'what's your choice?','e for even','o for odd'")
    Usernumber=int(input("What's your choice from 1 to 5?"))
    computer = random.choice([1,2,3,4,5])
    print(computer)
    result=Usernumber+computer
    if(result%2 == 0):
        if(user == 'e' or user == 'E'):
            return 'you win!'
        else:
            return 'you lost!'
    else:
        if(user == 'e' or user == 'E'):
            return 'you lost!'
        else:
            return 'you win!'
print(play())