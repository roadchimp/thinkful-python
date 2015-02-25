from bicycles import BikeShop, Bicycle, Customer, Wheel, Frame

# Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.

#After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.
  
#  - Ask question: what would you like to do?
#      [1] buy or [2] leave
#      - display list of bicycles they can afford, ie 1.papa, 2. coolidge
#      - create list + menu they can choose, let them select a bike
#      - update inventory, update their budget, update profit on sale
      
#Create a Bicycle Shop
Store101 = BikeShop("Mike's Bikes", None, 20)
#Create 6 models of bike
Bike1 = Bicycle("PureFix Papa", 20, 337, 10)
Bike2 = Bicycle("PureFix Coolidge", 20, 299, 10)
Bike3 = Bicycle("Diamondback Century 5", 19, 999, 10)
Bike4 = Bicycle("Diamondback Interval Carbon", 18, 500, 10)
Bike5 = Bicycle("Schwinn Huntington", 28, 105, 10)
Bike6 = Bicycle("Schwinn Starlet", 25, 220, 10)
# Create 3 customers
Cust1 = Customer("Larry", "200", None)
Cust2 = Customer("Moe", "500", None)
Cust3 = Customer("Curly", "1000", None)
# Create 3 wheels
Wheel1 = Wheel("700C", 5, 30)
Wheel2 = Wheel("26", 7, 35)
Wheel3 = Wheel("20", 5, 20)
# Create 3 frames
Frame1 = Frame("aluminum", 3, 150)
Frame2 = Frame("carbon", 2, 500)
Frame3 = Frame("steel", 5, 75)

Bike1.weight = Frame1.weight + (2 * Wheel1.weight)
Bike2.weight = Frame1.weight + (2 * Wheel1.weight)
Bike3.weight = Frame2.weight + (2 * Wheel1.weight)
Bike4.weight = Frame2.weight + (2 * Wheel1.weight)
Bike5.weight = Frame3.weight + (2 * Wheel3.weight)
Bike6.weight = Frame1.weight + (2 * Wheel2.weight)

Bike1.cost = Frame1.cost + (2 * Wheel1.cost)
Bike2.cost = Frame1.cost + (2 * Wheel1.cost)
Bike3.cost = Frame2.cost + (2 * Wheel1.cost)
Bike4.cost = Frame2.cost + (2 * Wheel1.cost)
Bike5.cost = Frame3.cost + (2 * Wheel3.cost)
Bike6.cost = Frame1.cost + (2 * Wheel2.cost)



#Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
def evaluate_budget(Customer_list, storename):
  Customer_list = []
  Customer_list[0].append(Cust1)

  for customer in Customer_list:
    i = 0 
    item_price = 0
    print "The budget of %s is %d" %(customer.name, int(customer.budget))
    while i < len(storename.Inventory):
      item_price = float(storename.Inventory[i].cost) * float(1+(storename.margin/100.0))
      if int(customer.budget) > item_price:
        print customer.name, "You can afford the %s which sells for %d " %(storename.Inventory[i].model, item_price)
      else:
        #print customer.name, "You cannot afford the %s which costs %d" %(storename.Inventory[i].model, item_price)
        pass
      i += 1 

def main():
  pass

  
  
if __name__ == "__main__":
  main()
