#Create a file named bicycles.py that contains each of your classes.
#Create a file named main.py that imports those classes, and uses them.

class Wheel(Bicycle):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    
class Frame(Bicycle):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    self.cost = cost

class Manufacturer(object):
  def __init__(self, name):
    self.name = name
  
class Bicycle(manufacturer):
  def __init__(self, model, frame, wheel):
    self.model = model
    self.frame = frame
    self.wheel = wheel
    
    def Bicycle_weight(self):
      return self.wheel.weight * 2 + self.frame.weight
    self.weight = weight
    self.cost = cost

class Bicycle(object):
    def __init__(self, f_wheel, r_wheel, frame, name, mfg):
        self.f_wheel = f_wheel
        self.r_wheel = r_wheel
        self.frame = frame
        self.name = name
        self.mfg = mfg

    def weight(self):
        return self.f_wheel.weight + self.r_wheel.weight + self.frame.weight

    def wholesale_cost(self):
        material_cost = self.f_wheel.cost + self.r_wheel.cost + self.frame.cost
        return  material_cost + material_cost * (self.mfg.margin/100)    


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

