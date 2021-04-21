#matriz
tictac_lists = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]


#funncion del tablero
def game_board(tictac_lists):
  length = 3
  height = 3
  up_border = ('  --- ' + '--- ' * (length-1) + ' \n')
  row_one_border = ' | ' + str(tictac_lists[0][0]) + ' | ' + str(tictac_lists[0][1]) + ' | ' + str(tictac_lists[0][2]) + ' | '
  row_two_border = ' | ' + str(tictac_lists[1][0]) + ' | ' + str(tictac_lists[1][1]) + ' | ' + str(tictac_lists[1][2]) + ' | '
  row_thr_border = ' | ' + str(tictac_lists[2][0]) + ' | ' + str(tictac_lists[2][1]) + ' | ' + str(tictac_lists[2][2]) + ' | '

  board = (up_border + row_one_border +  '\n') + (up_border + row_two_border +  '\n') + (up_border + row_thr_border +  '\n')+ up_border
  return board


#función para obtener las estadísticas
def get_coordinates(user_input): 
  row, column = user_input.split(',')
  row = int(row)
  column = int(column)
  return row, column


#funcion para validar el input:
def valid_input(user_input):
  row, column = get_coordinates(user_input)
  return tictac_lists[row-1][column-1] == 0


#función para colocar las estadística en el tablero (player One y Player Two)
def player_one_move(row, column):
  tictac_lists[row-1][column-1] = 'X'


def player_two_move(row, column):
  tictac_lists[row-1][column-1] = 'O'


#funcion para chequear si hay casilleros vacíos:
def emptyspace_check(tictac_lists):
  for i in range(3):
    for j in range(3):
      if tictac_lists[i][j] == 0:
        return True
  return False

#funcion para chequear si hay ganador
def define_winner(tictac_lists):
  winner = True
  for i in range(0,3):
    if tictac_lists[i][0] != 0: #Veo que no sea un casillero sin llenar
      if tictac_lists[i][0] == tictac_lists[i][1] == tictac_lists[i][2]:
        winner = False
      return winner
      if tictac_lists[0][i] == tictac_lists[1][i] == tictac_lists[2][i]: #COLUMNS  
        winner = False
      return winner
  #SACO LAS DIAGONALES DEL FOR      
  if tictac_lists[0][0] == tictac_lists[1][1] == tictac_lists[2][2]:  #DIAGONAL 1
    winner = False
  return winner
  if tictac_lists[0][2] == tictac_lists[1][1] == tictac_lists[2][0]:  #DIAGONAL 2
    winner = False
  return winner        


#Variables para el ciclo
filled_square = 'This is not an empty space. Try another move!'
end_message = 'Thank you for playing tic tac toe!'
win_message_PlayerOne = 'Player one wins!'
win_message_PlayerTwo = 'Player Two wins!'
input_player_one = None
input_player_two = None

#CICLO
while emptyspace_check(tictac_lists):  #se fija si hay casilleros vacíos o un ganador
  
  #juega el player 1
  is_input_valid = False
  while not is_input_valid:
    input_player_one = input('Player 1: Enter ROW (123) and COLUMN (123) separated by comma for your next move\n')   #Primer turno
    is_input_valid = valid_input(input_player_one)
    if is_input_valid == False:
      print(filled_square)
  
  row, column = get_coordinates(input_player_one)
  player_one_move(row, column) 
  print(game_board(tictac_lists))
  
  #chequea si hay ganador
  compare_results = define_winner(tictac_lists)
  if compare_results == False:
    print(win_message_PlayerOne)
    break
    
  
  #juega el player 2
  is_input_valid = False
  while not is_input_valid:
    input_player_two = input('Player 2: Enter ROW (123) and COLUMN (123) separated by comma for your next move\n') #Segundo Turno
    is_input_valid = valid_input(input_player_two)
    if is_input_valid == False:
      print(filled_square)

  row, column = get_coordinates(input_player_two)
  player_two_move(row, column)
  print(game_board(tictac_lists))

  #chequea si hay ganador
  compare_results = define_winner(tictac_lists)
  if compare_results == False:
    print(win_message_PlayerTwo)
    break
    
print(end_message)
