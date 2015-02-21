class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
  def solo(self, length):
    for i in range(length):
      print self.sounds[i % len(self.sounds)],
    print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
  def __init__(self): # Call the __init__ method of the parent class
    super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
  def __init__(self): # Call the __init__ method of the parent class
    super(Guitarist, self).__init__(["Boink", "Bow", "Boom"]) 
  def tune(self):
    print "Be with you in a moment"
    print "Twoning, sproing, splang"

class Drummer(Musician): 
  def __init__(self):
    super(Drummer, self).__init__(["Bish", "Bang", "Boom"])
    def count(self):
      print "1, 2, and a 1, 2, 3, 4!"
    def combust(self):
      print "I will blow up now"
      
class Band(object):
  def __init__(self, hire):
    self.hire = hire
  def __init__(self, fire):
    self.hire = hire
#Bands should be able to hire and fire musicians, and have the musicians play their solos after the drummer has counted time.    

chickenlittle = Band()
chickenlittle.hire(nigel)

david = Musician(["Twang", "Thrumb", "Bling"])
derek = Musician(["Boink", "Bow", "Boom"])
david.solo(6)       

nigel = Guitarist()
nigel.solo(6)
print nigel.sounds