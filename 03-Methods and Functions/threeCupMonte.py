#example = list(range(1,11))
from random import shuffle
#shuffle(example)

def shuffleList(mylist):
    shuffle(mylist)
    return mylist
#print(shuffleList(example))
taList = ["0","X", "0"]
#shuffleList(taList)

def player_guess():
    guess=''
    while guess not in ['1','2','3']:
        guess = input("give me a number 1,2 or 3: ")
    return int(guess)
#player_guesis()

def check_guess(mylist, guess):
    if mylist[guess-1] == "X":
        print('Correct!')
    else:
        print('No Dice, Vato Loco')
        print(mylist)

mixList = shuffleList(taList)
guess = player_guess()
check_guess(mixList, guess)
