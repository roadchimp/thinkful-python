def side_effect_test(tuple1):
  # Do something to modify the value
  value[1] = "orange"
  number[1] = 1
  dictionary['name'] = 'neo'
  boolean = True
  tuple1 = ('theology')
  print "Inside the function, the value becomes {}".format(tuple1)

if __name__ == "__main__":
  # Create the value
  value = ["red", "green", "blue"]
  number = [1, 2, 3]
  dictionary = {'name': 'alice', 'job': 'falling down rabbit holes', 'enemies': 'red queen'}
  boolean = False
  tuple1 = ('physics', 'chemistry', 1997, 2000);
  print "Outside the function, the value starts as {}".format(tuple1)
  side_effect_test(tuple1)
  print "Outside the function, the value is now {}".format(tuple1)