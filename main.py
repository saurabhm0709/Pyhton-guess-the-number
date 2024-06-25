import random

highest_score = 0

def play_again():
  again = input('Want to play again ?Enter Y or N: ').lower()
  print()
  return again == 'y'

def guess_number():

  current_score = 20
  secret_number = random.randint(1,20)

  global highest_score

  while current_score > 0:       
    
    guess = int(input("Enter a number between 1 and 20: "))
    print()
    if guess == secret_number:
      print("Congrats! your guess is correct.")
      print()
      if current_score > highest_score:
        highest_score = current_score
      print('score: ',current_score)
      print('Highest score: ',highest_score)
      print()
      if play_again():
        current_score = 20
        secret_number = random.randint(1,20)
        continue
      else:
        break
    elif guess!= secret_number and guess > secret_number:
      print("Too high!")
      current_score -= 1
      print('Current Score: ',current_score)
      print()
    elif guess != secret_number and guess < secret_number:
      print("Too low!")
      current_score -= 1
      print('Current Score: ',current_score)
      print()
  if current_score <= 0:
    print('You lost all the chances!')
    if play_again():
      guess_number()
    print()

guess_number()
