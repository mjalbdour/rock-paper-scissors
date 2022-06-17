# Write your code here
import random

user_ratings_file_name = "rating.txt"

msg_enter_name = "Enter your name: "
msg_hello = "Hello,"
msg_start = "Okay, let's start"
msg_rating = "Your rating:"
msg_loss = "Sorry, but the computer chose"
msg_draw = "There is a draw"
msg_win_1 = "Well done. The computer chose"
msg_win_2 = "and failed"
msg_invalid = "Invalid input"
msg_bye = "Bye!"

exit_option = "!exit"
rating_option = "!rating"

game_result_win = "WIN"
game_result_draw = "DRAW"

draw_score_value = 50
win_score_value = 100


def lookup_user(user):
    ratings_file = open(user_ratings_file_name, "rt")
    result = 0
    for line in ratings_file:
        current_user, rating = line.split()
        if current_user == user:
            result = int(rating)
            break

    ratings_file.close()

    return result


def update_rating(game_result, current_rating):
    if game_result == game_result_draw:
        return apply_draw(current_rating)
    elif game_result == game_result_win:
        return apply_win(current_rating)


def apply_draw(current_rating):
    return current_rating + draw_score_value


def apply_win(current_rating):
    return current_rating + win_score_value


random.seed()

print(msg_enter_name)
user_name = input()
print(f"{msg_hello} {user_name}")

user_rating = lookup_user(user_name)

plays = ['rock', 'paper', 'scissors']
plays_input = input()
if plays_input != "":
    plays = [play.lower() for play in plays_input.split(",")]
print(msg_start)

while True:
    user_choice = input()
    if user_choice == exit_option:
        print(msg_bye)
        break

    elif user_choice == rating_option:
        print(f"{msg_rating} {user_rating}")
        continue

    if user_choice not in plays:
        print(msg_invalid)
    else:
        computer_choice = random.choice(plays)
        new_plays = plays[plays.index(user_choice) + 1:] + plays[:plays.index(user_choice)]
        if user_choice == computer_choice:
            print(f"{msg_draw} ({computer_choice})")
            user_rating = update_rating(game_result_draw, user_rating)
        elif new_plays.index(computer_choice) >= len(new_plays) // 2:
            print(f"{msg_win_1} {computer_choice} {msg_win_2}")
            user_rating = update_rating(game_result_win, user_rating)
        else:
            print(f"{msg_loss} {computer_choice}")
