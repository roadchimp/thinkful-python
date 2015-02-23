#Create a file named bicycles.py that contains each of your classes.
#Create a file named main.py that imports those classes, and uses them.

class Bicycle(object):
  def __init__(self, model, weight, cost, quantity):
    self.model = model
    self.weight = weight
    self.cost = cost
    self.quantity = quantity
  
class BikeShop(object):
  def __init__(self, name, inventory, margin):
    self.name = name
    self.inventory = inventory
    self.margin = margin
    
class Customer(object):
  def __init__(self, name, budget, bike):
    self.name = name
    self.budget = budget
    self.bike = bike

