def even_odd (usernumber):
  result = usernumber % 2
  multipleof4 = usernumber % 4 
  if result == 0 and multipleof4 != 0:
    print ('the number ' + str(usernumber) + ' is an even number')
  if multipleof4 == 0:
    print ('the number ' + str(usernumber) + ' is an even number and multiple of 4')
  else:
    print ('the number ' + str(usernumber) +  ' is an odd number')
  return

def division(num, check):
  if num % check == 0:
    print ('the division has an integrate result\n')
  else:
    print ('this division gives you a floating number as a result\n')
  return

usernumber = int(input('Choose a number\n'))
num = int(input('Enter another number of your choice\n'))
check = int(input('And another number to divide\n'))

even_odd(usernumber)
division(num, check)
