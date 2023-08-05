import random

print("we're both bored, let's play some rock paper scissors :)")

userChoice = input('what do you choose?: ')
choices = ('rock', 'paper', 'scissors')
aiChoice = random.choice(choices)

if aiChoice == userChoice:
    print(f'i chose {aiChoice}')
    print("oh, it's a draw :/")
elif aiChoice == 'rock' and userChoice == 'paper':
    print(f'i chose {aiChoice}')
    print("you win :)")
elif aiChoice == 'paper' and userChoice == 'scissors':
    print(f'i chose {aiChoice}')
    print("you win :)")
elif aiChoice == 'scissors' and userChoice == 'rock':
    print(f'i chose {aiChoice}')
    print("you win :)")
elif aiChoice == 'paper' and userChoice == 'rock':
    print(f'i chose {aiChoice}')
    print("i win >:D")
elif aiChoice == 'scissors' and userChoice == 'paper':
    print(f'i chose {aiChoice}')
    print("i win >:D")
elif aiChoice == 'rock' and userChoice == 'scissors':
    print(f'i chose {aiChoice}')
    print("i win >:D")