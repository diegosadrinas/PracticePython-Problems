def fibona(userinput):
    if userinput == 0:
        return 0
    if userinput == 1:
        return 1
    return fibona(userinput-1) + fibona(userinput-2)

def gen_list(userinput):
  new_list = list(range(userinput))
  if userinput >= 0:
    return new_list
    print(new_list)
  else:
    return print('Only positive numbers can integrate this list\n')
  
def fibona_list(userlist):
  fibonacci_list = []
  for index in userlist:
    fibonacci_list.append(fibona(index))
  return print('This is the fibonacci sequence with the length of ', str(userinput), ' numbers:\n', fibonacci_list)

userinput = int(input('Enter the length of the list you want to create\n')) 
userlist = gen_list(userinput)
fibona_list(userlist)
