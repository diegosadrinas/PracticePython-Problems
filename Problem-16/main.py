import random
import string

valid_passinput = ['yes', 'no']
valid_strengtinput = ['strong', 'weak']

def strong_pass_list():
  all_items = []
  numbers = [all_items.append(i) for i in string.digits]
  symbols = [all_items.append(i) for i in string.punctuation]
  lowerletters = [all_items.append(i) for i in string.ascii_lowercase]
  upperletters = [all_items.append(i) for i in string.ascii_uppercase]
  return ''.join(random.sample(all_items, 12))

def weak_pass_list():
  words_list = 'As he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of light '
  split_words = words_list.split(' ')
  weak_pass = ' '.join(random.sample(split_words, 2))
  return weak_pass

def pass_gen():
  invalid_passinput = True
  while invalid_passinput:
    pass_input = input('Do you want to generate a new password?\n').lower()
    if pass_input in valid_passinput:
      invalid_passinput = False

  if pass_input == 'yes':
    invalid_strengthinput = True
    while (invalid_strengthinput):
      strength_input = input('If you want a strong password, type "strong". If you want a weak password, type "weak"\n').lower()
      if strength_input in valid_strengtinput:
        invalid_strengthinput = False

    if strength_input == 'strong':
      return strong_pass_list()
    else:
      return weak_pass_list()
  else:
    return print('Ok!')

pass_gen()
