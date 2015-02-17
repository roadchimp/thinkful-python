import random

i = 0
drink = ""
name = ""
reg_customer = False

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

names_adjectives = ["Fluffy", "Salty", "Portly", "Spritely"]
names_nouns = ["SeaMonkey", "Chinchilla", "Poodle", "Porpoise"]

customer_dict = {
  "sam": [True, True, True, True, True],
  "joe": [True, False, False, True, True]
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

def find_preferences():
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
  return answers

def test_preferences():
  for i, elem in enumerate(test_input):
    test = find_preferences(elem)
    control = test_output[i]
    print "checking that preference({}) == {}; {}".format(elem, control, test)
    assert(test == control)

def make_drink(answers, ingredients):
    drink = []
    for key, value in answers.iteritems():
      if value == True:
        #drink.append(random.choice(ingredients.get(key)))
        drink.append(random.choice(ingredients[key]))
    print "Your drink contains the following:"
    for ingredient in drink:
      print "  A {}".format(ingredient)
    return drink
  
def name_drink(ordered_drink):
  name = ""
  name = ''.join(random.sample(names_adjectives, 1))
  name += " "
  name += ''.join(random.sample(names_nouns, 1))
  print "Your drink is called the %s" %(name)
  return name
    
def evaluate_customer():
  cust_name = raw_input("Hi, what's your name?")
  while True:
    for name, prefs in customer_dict.iteritems():
      reg_customer = False
      if cust_name.lower() == name:
        reg_customer = True
        break
    if reg_customer == True:
      print "Welcome back, %s" % cust_name
    else:
      print "I guess you're new"
      customer_dict[cust_name] = ""
    return (cust_name, reg_customer)
    break


def main():
  
  #test_preferences()
  while True:
    thirsty = raw_input("Would you like something to drink?")
    if thirsty.lower() in ('yes', 'y'):
      cust_name, reg_customer = evaluate_customer()
      #print cust_name
      #print reg_customer
      if reg_customer == False:
        answers = find_preferences()
      else:
        for name, prefs in customer_dict.iteritems():
          answers[name] = customer_dict[cust_name]
        # this needs to look like output of find_preferences()
        #{'bitter': True, 'strong': True, 'salty': True, 'fruity': True, 'sweet': True}  
      print answers

      #ordered_drink = make_drink(answers, ingredients)
      #name = name_drink(ordered_drink)

    else:
      print "Okay, time to call it a night then, bye!"
      break

    
    
#print "__name__ is: ".format(__name__)
if __name__ == "__main__":
  main()