import random

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

test_answers = {
  "strong": ["True"], 
  "salty": ["True"], 
  "bitter": ["True"], 
  "sweet": ["True"], 
  "fruity": ["False"]
}

def preferences(value):
  #do some kind of loop to iterate questions, then collect response in answers
  for (key, value) in questions.iteritems():
    while True:
      response = raw_input( "{}".format(value))
      if response.lower() not in ('yes', 'y', 'no', 'n'):
        print "Please enter Yes, Y, No or N."
      else:
        break
    if response.lower() == "yes":
      answers[key] = True
    elif response.lower() == "y":
      answers[key] = True
    elif response.lower() == "no":
      answers[key] = False
    elif response.lower() == "n":
      answers[key] = False
  print answers

def test_preferences():
  for i, elem in enumerate(test_input):
    test = preferences(elem)
    control = test_output[i]
    print "checking that preference({}) == {}; {}".format(elem, control, test)
    assert(test == control)

def make_drink(answers, ingredients):
    drink = []
    for key, value in answers.iteritems():
      print value
      if value == True:
        #print random.choice(ingredients.get(key))
        drink.append(random.choice(ingredients.get(key)))
    #print "this is {}".format(drink)
    return(drink)


    
    
    
def main():
  
  #print test_preferences()
  print preferences(drink)
  print make_drink(answers, ingredients)
  
  
#print "__name__ is: ".format(__name__)
if __name__ == "__main__":
  main()