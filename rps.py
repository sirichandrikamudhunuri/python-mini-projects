import random
def play():
    user = input("'What's your choice?','r for rock','p for paper','s for scissors'")
    computer = random.choice(['r','p','s'])
    print(computer)
    if user == computer:
        return 'It is a tie'
    if win(user,computer):
        return 'You Win!'
    return 'You Lost!'
def win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
       return True
print(play())