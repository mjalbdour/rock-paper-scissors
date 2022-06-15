# Write your code here
import random

msg_loss = 'Sorry, but the computer chose'
msg_draw = 'There is a draw'
msg_win_1 = 'Well done. The computer chose'
msg_win_2 = 'and failed'
msg_invalid = 'Invalid input'
msg_bye = 'Bye!'

game_options = {'paper': 'rock',
                'rock': 'scissors',
                'scissors': 'paper'}

exit_option = '!exit'

random.seed()

while True:
    user_choice = input()
    if user_choice == exit_option:
        print(msg_bye)
        break
    computer_choice = random.choice(list(game_options.values()))

    if user_choice not in game_options:
        print(msg_invalid)
    else:
        if user_choice == computer_choice:
            print(f'{msg_draw} ({computer_choice})')
        elif game_options[user_choice] == computer_choice:
            print(f'{msg_win_1} {computer_choice} {msg_win_2}')
        else:
            print(f'{msg_loss} {computer_choice}')
