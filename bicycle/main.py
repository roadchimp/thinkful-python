import bicycles

# Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.

#After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

# redesign:
# create individual instances of each class
#  - instance of store, each of 6 bicycles, each of 3 customers
#  - Do classes need to be updated?
  
#  - Ask question: what would you like to do?
#      [1] buy or [2] leave
#      - display list of bicycles they can afford, ie 1.papa, 2. coolidge
#      - create list + menu they can choose, let them select a bike
#      - update inventory, update their budget, update profit on sale
      
#Create a Bicycle Shop
def initialize_shop(shopname):
  shopname = BikeShop(shopname, None, 20)
  print "Welcome to %s" %shopname.name
  return shopname