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

   random_selections = [destination, restaurant, transportation, entertainment]
   return random_selections

trip = generate_trip()


def confirm_trip():



#  print('Does the trip suffice?')
# user = input()
# print(user)

   
   
# def print_trip(trip):
#       for selection in trip:
#          print(selection)
      
      
#       print_trip(trip)