# you'll have to use control flow to deal with two situations: one in which the user supplies command line arguments, and one where they do not.

import sys

n = 100

test_input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
test_output = ["1", "2", "fizz", "4", "buzz","fizz","7","8","fizz", "buzz","11","fizz","13","14","fizzbuzz"]

test_input2 = [100,100,80,120]
test_output2 = 100

def fizz_buzz(n):
  if n % 3 == 0:
    if n % 5 == 0:
      return "fizzbuzz"
    else: 
      return "fizz"
  elif n % 5 == 0:
    return "buzz"
  else:
    return str(n) 
    
def test_fizz_buzz():
  for i, elem in enumerate(test_input):
    t = fizz_buzz(elem)
    o = test_output[i]
    print "checking that fizz_buzz({}) == {}; {}".format(elem, o, t)
    assert(t == o)
    
def mean(l):
  return 100

def test_mean():
  print "checking that mean({}) == {}; {}".format(test_input2, test_output2, mean(test_input2))
  assert(test_output2 == mean(test_input2))
  
def main():
  
  #test_fizz_buzz()
  test_mean()

  user_input = None
  try:
    user_input = int(sys.argv[1])
  except:
    pass

  while user_input is None:
    try:
      user_input = int(raw_input("Enter a number: "))
    except:
      pass

  for i in range(1, user_input): 
    print fizz_buzz(i)

print "__name__ is: ".format(__name__)
if __name__ == "__main__":
  main()
    