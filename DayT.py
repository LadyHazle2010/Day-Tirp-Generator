# def display_welcome():
#    msg = 'Please choose your trip options!'
#    print(msg)

# print('Please choose your trip options!')

# print('Where would you like to go?') 

# list_option = ()
import random


def generate_trip():
   destinations = ["India", "Columbia", "Peru", "Africa"]
   restaurants = ["olive garden", "gestopo's", "little india", "wakanda forever"]
   transportations = ["airplane", "ship", "train", "tour bus"]
   entertainments = ["jazz concert", "opera", "bar hop", "scubba diving"]

   destination = random.choice(destinations)
   restaurant = random.choice(restaurants)
   transportation = random.choice(transportations)
   entertainment = random.choice(entertainments)

   trip =[destination, restaurant, transportation, entertainment]
   return trip






trip = generate_trip()

for selection in trip:
   print(selection)