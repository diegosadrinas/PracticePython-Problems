options = ["rock", "paper", "scissors"]
playagain = ["yes", "no"]

def giveValidInput():
  userInput = ''
  while userInput not in options:
    userInput = input("Choose rock, paper or scissors\n").lower()
  return userInput

def compareInputs(anInput, anotherInput):
  if anInput == "rock" and anotherInput == 'paper':
    print('Player 2 Wins!')
  if anInput == "rock" and anotherInput == 'scissors':
    print('Player 1 Wins!')
  if anInput == "rock" and anotherInput == 'rock':
    print('It´s a Tie!')
  if anInput == "paper" and anotherInput == 'paper':
    print('It´s a Tie!')
  if anInput == "paper" and anotherInput == 'rock':
    print("Player 1 Wins!")
  if anInput == "paper" and anotherInput == 'scissors':
    print('Player 2 Wins!')
  if anInput == "scissors" and anotherInput == 'paper':
    print("Player 1 Wins!")
  if anInput == "scissors" and anotherInput == 'rock':
    print('Player 2 Wins!')
  if anInput == "scissors" and anotherInput == 'scissors':
    print('It´s a Tie!')

letsplay = True
while letsplay:
  inputplayer1 = giveValidInput()
  inputplayer2 = giveValidInput()
  compareInputs(inputplayer1, inputplayer2)

  newgame = ''
  while newgame not in playagain:
    newgame = input('Do you want to play again?\n').lower()
    if newgame == 'no':
      letsplay = False
      print('Thank you for playing!\n')
