from random import choice
npc = choice(['rock', 'paper', 'scissors'])

player_1 = input('Select a choice \n 1. rock \n 2. paper \n 3. scissors \n').lower()

if player_1 == npc:
    print(f'PC chooses {npc} \n Its a Draw!!! ')
elif player_1 == 'rock' and npc == 'paper':
    print(f'PC chooses {npc} \n You Lose!!! ')
elif player_1 == 'rock' and npc == 'scissors':
    print(f'PC chooses {npc} \n You Win!!! ')

elif player_1 == 'paper' and npc == 'rock':
    print(f'PC chooses {npc} \n You Win!!! ')
elif player_1 == 'paper' and npc == 'scissors':
    print(f'PC chooses {npc} \n You Lose!!! ')

elif player_1 == 'scissors' and npc == 'rock':
    print(f'PC chooses {npc} \n You Lose!!! ')
elif player_1 == 'scissors' and npc == 'paper':
    print(f'PC chooses {npc} \n You Win!!! ')


else:
    print('Something go wrong')
