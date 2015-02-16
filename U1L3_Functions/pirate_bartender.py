i = 0

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

def what_style():
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

what_style()
print answers
#dictionary['name'] = 'neo'
# print "{} => {}".format(key, value)
# print questions["strong"]
# answers = raw_input("Enter a number: ")
  
