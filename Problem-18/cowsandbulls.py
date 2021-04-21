mport random

#FUNCION 1
def valid_input(user_input):
  result_input = False
  if user_input == 'exit':
   result_input = True
  if user_input.isnumeric():
    if int(user_input) in range(1000,9999):
      result_input = True
  return result_input

#FUNCION 2
def guess_result(user_input, random_number):
  digit_list = [digit for digit in str(user_input)]

  cows = 0
  bulls = 0
  for number in digit_list:
    if number in random_number:
      cows += 1
    if number not in random_number:
      bulls += 1
  return cows, bulls
 
#FUNCION 3
def win_the_game(user_input, random_number):
  return user_input == random_number



#JUEGO
playing = True
welcome_message = str('Welcome to Cows and Bulls!')
random_number = str(random.randint(1000, 9999))
win_message = str('You have 4 cows!')
exit_message = str('Thank you for playing cows and bulls')
tries = 0
print(random_number)

while playing:
  user_input = input('Enter a four digit number and try to guess. If you want to exit the game, type "exit"\n')
  
  if valid_input(user_input):
    if user_input == 'exit':
      print(exit_message)
      playing = False
    if not user_input == 'exit':
      cows_and_bulls = guess_result(user_input, random_number)
      if cows_and_bulls[0] != 4:
        print('You have ' + str(cows_and_bulls[0]) + ' cows and ' + str(cows_and_bulls[1]) + ' bulls')
      if win_the_game(user_input, random_number):
        print(win_message)
        playing = False
      tries += 1
      print('You tried to guess ' + str(tries) + ' times!\n')
      
