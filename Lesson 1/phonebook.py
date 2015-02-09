phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

search = "Jamie Theakston"


for person in phone_book:
  if search == person: 
    print "{}".format(person)
  else: 
    print "no found"
    
for person in phone_book:
  try:
    search == person 
  except false:
    print "match was not found"