tictac_lists = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]


#función para obtener las coordenadas
def get_coordinates(user_input): 
  row, column = user_input.split(',')
  row = int(row)
  column = int(column)
  return row, column


#funcion para validar el input:
def valid_input(user_input):
  row, column = get_coordinates(user_input)
  print(tictac_lists[row-1][column-1])
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


#Variables para el ciclo
filled_square = 'This is not an empty space. Try another move!'
end_message = 'Thank you for playing tic tac toe!'
input_player_one = None
input_player_two = None

#CICLO
while emptyspace_check(tictac_lists):  #se fija si hay casilleros vacíos
  is_input_valid = False
  while not is_input_valid:
    input_player_one = input('Player 1: Enter ROW (123) and COLUMN (123) separated by comma for your next move\n')   #Primer turno
    is_input_valid = valid_input(input_player_one)
    if is_input_valid == False:
      print(filled_square)
    
  row, column = get_coordinates(input_player_one)
  player_one_move(row, column) 
  for i in tictac_lists: #imprime el tablero después de la jugada
    print(i, end = '\n')
  
  is_input_valid = False
  while not is_input_valid:
    input_player_two = input('Player 2: Enter ROW (123) and COLUMN (123) separated by comma for your next move\n') #Segundo Turno
    is_input_valid = valid_input(input_player_two)
    if is_input_valid == False:
      print(filled_square)

  row, column = get_coordinates(input_player_two)
  player_two_move(row, column)

  for i in tictac_lists:
    print(i, end = '\n')

print(end_message)

