import random
# number = random.randint(1, 6)

# print(number)

# options = ("Rock", "paper",  "Scissors")
# option = random.choice(options)

# print(option)

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

    if guess < lowest_num or guess > highest_num:
        print("That number is out of range")
        print(f"Please enter a number between {lowest_num} and {highest_num}")

    elif guess < answer:
        print("Too low! Try again!")
    elif guess > answer:
        print("Too high! Try again!")
    else:
        print(f"Congratulations you guessed the number correctly!{answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False

    # else:
    #     print("Invalid guess")
    #     print(f"Please enter a number between {lowest_num} and {highest_num}")
