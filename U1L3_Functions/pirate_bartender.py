i = 0
drink = ""

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

answers = {
  "strong": [""], 
  "salty": [""], 
  "bitter": [""], 
  "sweet": [""], 
  "fruity": [""]
}

test_input = ["Yes", "YeS", "yeS", "y", "YES"]
test_output = [True, True, True, True, True]

def preferences(value):
  output = True
  response = raw_input( "{}".format(value))
  try: 
    response.lower() not in ('yes', 'y', 'no', 'n')
    print "Please enter Yes, Y, No or N."
  except:
    pass
  if response.lower() == "yes":
    answers[key] = True
  elif response.lower() == "y":
    answers[key] = True
  elif response.lower() == "no":
    answers[key] = False
  elif response.lower() == "n":
    answers[key] = False
    output = answers[key]
  return output

def test_preferences():
  for i, elem in enumerate(test_input):
    test = preferences(elem)
    control = test_output[i]
    print "checking that preference({}) == {}; {}".format(elem, control, test)
    assert(test == control)


def main():
  
  #print test_preferences()
  
  #do some kind of loop to iterate questions, then collect response in answers
  for (key, value) in questions.iteritems():
    while True:
      preferences(drink)

  
print "__name__ is: ".format(__name__)
if __name__ == "__main__":
  main()