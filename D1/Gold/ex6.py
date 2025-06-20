import random

games_won = 0
games_lost = 0

while True:
    user_guess = input("Guess a number (1-9) or type 'quit' to exit: ").strip()
    
    if user_guess.lower() == 'quit':
        break
    
    user_guess = int(user_guess)
    random_num = random.randint(1, 9)
    
    if user_guess == random_num:
        print("Winner!")
        games_won += 1
    else:
        print(f"Better luck next time. The number was {random_num}.")
        games_lost += 1

print(f"Total games won: {games_won}")
print(f"Total games lost: {games_lost}")