from random import choice
print('''=====================================================================
                Rock ✊, Paper ✋ n Scissors ✌
=====================================================================
''')

player_wins = 0
npc_wins = 0

# score = print(f'''
# P1: {player_wins}
# PC: {npc_wins}
# ''')

while player_wins < 3 and npc_wins < 3:

    npc = choice(['rock', 'paper', 'scissors'])

    player_1 = input(
        'Select a choice \n 1. rock \n 2. paper \n 3. scissors \n').lower()

    if player_1 == npc:
        print(f'PC chooses {npc} \n Its a Draw!!! ')
    elif player_1 == 'rock' and npc == 'paper':
        print(f'PC chooses {npc} \n You Lose!!! ')
        npc_wins += 1
    elif player_1 == 'rock' and npc == 'scissors':
        print(f'PC chooses {npc} \n You Win!!! ')
        player_wins += 1
    elif player_1 == 'paper' and npc == 'rock':
        print(f'PC chooses {npc} \n You Win!!! ')
        player_wins += 1
    elif player_1 == 'paper' and npc == 'scissors':
        print(f'PC chooses {npc} \n You Lose!!! ')
        npc_wins += 1
    elif player_1 == 'scissors' and npc == 'rock':
        print(f'PC chooses {npc} \n You Lose!!! ')
        npc_wins += 1
    elif player_1 == 'scissors' and npc == 'paper':
        print(f'PC chooses {npc} \n You Win!!! ')
        player_wins += 1
    else:
        print('Something go wrong')

    print(f'''
                                P1: {player_wins}
                                PC: {npc_wins}
''')
