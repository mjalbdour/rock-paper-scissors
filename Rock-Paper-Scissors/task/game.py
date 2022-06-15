# Write your code here
user_choice = input()
msg = 'Sorry, but the computer chose'
computer_choice = None
if user_choice == "rock":
    computer_choice = "paper"
elif user_choice == "paper":
    computer_choice = "scissors"
elif user_choice == "scissors":
    computer_choice = "rock"

print(f'{msg} {computer_choice}')
