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

stock = {
  "glug of rum" : 10,
  "slug of whisky" : 10,
  "splash of gin" : 10,
  "olive on a stick" : 10,
  "salt-dusted rim" : 10,
  "rasher of bacon" : 10,
  "shake of bitters" : 10,
  "splash of tonic" : 10,
  "twist of lemon peel" : 10,
  "sugar cube" : 10,
  "spoonful of honey" : 10,
  "spash of cola" : 10,
  "slice of orange" : 10,
  "dash of cassis" : 10,
  "cherry on top" : 10
}

names_adjectives = ["Fluffy", "Salty", "Portly", "Spritely"]
names_nouns = ["SeaMonkey", "Chinchilla", "Poodle", "Porpoise"]

customer_dict = {
  'sam': {'bitter': True, 'strong': True, 'salty': True, 'fruity': True, 'sweet': False}
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

def repeat_drink(ordered_drink):
    #take last drink and make it again
    drink = []
    for key, value in ordered_drink.iteritems():
      drink.append(ordered_drink[key])
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
  cust_name = raw_input("Welcome! What's your name?")
  while True:
    for name, prefs in customer_dict.iteritems():
      reg_customer = False
      if cust_name.lower() == name:
        reg_customer = True
        break
    if reg_customer == True:
      print "Welcome back, %s" % cust_name
    else:
      print "Good to see a new customer!"
      customer_dict[cust_name] = ""
    return (cust_name, reg_customer)
    break
    
def reduce_stock(ordered_drink):
  while True:
    for ingredient in ordered_drink:
      if ingredient in stock:
        stock[ingredient] -= 1
    return stock
      
def main():
  
  #test_preferences()
  cust_name, reg_customer = evaluate_customer()
  while True:
    thirsty = raw_input("Would you like something to drink?")
    if thirsty.lower() in ('yes', 'y'):
      if reg_customer == False:
        answers = find_preferences()
        customer_dict[cust_name]= answers
        reg_customer = True
        ordered_drink = make_drink(answers, ingredients) 
      else:
        answers = customer_dict[cust_name]
        print answers
        ordered_drink = 
      #print ordered_drink
      current_stock = reduce_stock(ordered_drink)
      #print current_stock
      #name = name_drink(ordered_drink)
    else:
      print "Okay, time to call it a night then, bye!"
      break

    
    
#print "__name__ is: ".format(__name__)
if __name__ == "__main__":
  main()