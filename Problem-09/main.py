import random
random_number = random.randint(1, 9)
playing = True
tries = 0

while (playing):
  user_input = input('Guess the number I have chosen between 1 and 9\n')
  if user_input == 'exit':
    playing = False
  else: 
    print('You chose ', str(user_input))
    if int(user_input) < random_number:
      print('Too low! Try again\n')
    if int(user_input) > random_number:
      print('Too high! Try again\n')
    if int(user_input) == random_number:
      print('Your guess is right!\n')
      playing = False
    tries += 1

print('You tried ' + str(tries) + ' times')
