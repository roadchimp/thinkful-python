foo = [1,2,3,4]

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for (key, value) in actors.iteritems():
  print "{} => {}".format(key, value) 

for key in actors:
    value = actors[key]
    print "The actor {} played the character {}".format(key, value)
    
