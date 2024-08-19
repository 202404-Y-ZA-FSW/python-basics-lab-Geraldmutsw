import random
# Number guessing game function
def number_guessing_game():

  number = random.randint(1, 100)
  attempts = 0

  while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess == number:
      print(f"Congratulations! You guessed the number in {attempts} attempts.")
      break
    elif guess < number:
      print("Too low.")
    else:
      print("Too high.")

if __name__ == "__main__":
  number_guessing_game()