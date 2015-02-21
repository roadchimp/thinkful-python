distance = 102
distance_covered = 0
speed_a = 2
speed_b = 1
time = 0

while distance_covered < distance:
    time +=1
    distance_covered = ((speed_a + speed_b) * time)
    print ('Still not met yet')
else:
  print ("We've met after {} hours.").format(time)
  print ("We met {} miles outside of london.").format(time * speed_b)
    