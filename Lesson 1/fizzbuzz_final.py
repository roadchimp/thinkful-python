# you'll have to use control flow to deal with two situations: one in which the user supplies command line arguments, and one where they do not.

import sys

n = 100
i = 0
user_input = 0
string = ""

    
# if user doesn't input extra arguments
# query user for input

if len(sys.argv) == 1:
  # Checks if input was a number
  while True:
    try:
      user_input = raw_input("Enter a number:")
      i = int(user_input)
    except ValueError:
      print "Invalid character, please enter a number"
      continue
    else:
      break
  print "Fizz buzz counting up to {}".format(n)
  # traps the error, need a loop, such as while true or false etc, keep prompting. now it takes i=0
  while i < n:
    if i % 3 == 0:
      if i % 5 == 0:
        print "fizz buzz"
      else: 
        print "fizz"
    elif i % 5 == 0:
      print "buzz"
    else:
      print i
    i += 1
else:
  # user initiated script with an argument
  # Checks if input was a number
  while True:
    try:
      user_input = raw_input("Enter a number:")
      i = int(user_input)
    except ValueError:
      print "Invalid character, please enter a number"
      continue
    else:
      break
  user_input = sys.argv[1]
  print "Fizz buzz counting up to {}".format(n)
  while i < n:
    if i % 3 == 0:
      if i % 5 == 0:
        print "fizz buzz"
      else: 
        print "fizz"
    elif i % 5 == 0:
      print "buzz"
    else:
      print i
    i += 1
  