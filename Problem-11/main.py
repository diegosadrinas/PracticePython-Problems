def get_divisors(userinput):
    divisorslist = []
    for x in range(1, userinput + 1):
      if userinput % x == 0:
        divisorslist.append(x)
    return divisorslist

def list_count(divisorslist):
  return len(divisorslist)

def is_prime(userinput):
  divisorslist = get_divisors(userinput)
  list_count(divisorslist)
  if list_count(divisorslist) == 2:
    prime = True
  else:
    prime = False
  return prime 
 

def printprime(userinput):
  prime = is_prime(userinput)
  if prime == True:
    return print('This a prime number!')
  if prime == False:
    return print('This is not a prime number!')
  

userinput = int(input('Enter any number to check if it`s prime\n'))
printprime()
