class Bicycle(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
  
class BikeShop(object):
  def __init__(self, name, inventory, margin, profit):
    self.name = name
    self.inventory = inventory
    self.margin = margin
    self.profit = profit
    
  def Add_inventory(self, bicycle, cost):
    pass
    
class Customer(object):
  def __init__(self, name, budget, bike):
    self.name = name
    self.budget = budget
    self.bike = bike
    
def main():
  #Create a Bicycle Shop
  Store101 = BikeShop("Mike's Bikes", None, 20, 100)
  print Store101.name

  #Add 6 Bikes to Inventory 
  Store101.Inventory = []
  Store101.Inventory.append(Bicycle("PureFix_Papa", 40, 337))
  Store101.Inventory.append(Bicycle("PureFix_Coolidge", 40, 299))
  Store101.Inventory.append(Bicycle("Diamondback_Century_5", 30, 999))
  Store101.Inventory.append(Bicycle("Diamondback_Interval_Carbon", 45, 500))
  Store101.Inventory.append(Bicycle("Schwinn_Huntington", 50, 105))
  Store101.Inventory.append(Bicycle("Schwinn_Starlet", 35, 220))
  print Store101.Inventory[0].model
  print Store101.Inventory[0].cost
  
  #Create three customers.
  Larry = Customer("Larry", "200", None)
  Moe = Customer("Moe", "500", None)
  Curly = Customer("Curly", "1000", None)
  print Larry.budget 
  
  #Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
  print Larry.name

  i = 0
  while i < 6:
    if int(Larry.budget) > int(Store101.Inventory[i].cost):
      print Larry.budget
      print Store101.Inventory[i].cost
      i+= 1
    else:
      print "You can't afford a bike"
      break

if __name__ == "__main__":
  main()


    