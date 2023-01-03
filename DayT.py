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



def confirm_complete_trip():
   response = ''
   while response != 'yes':

      trip = generate_trip()
      print_trip(trip)
      response = input('Does trip suffice?')



def trip_acceptable():
   user = input('Congradulations! Enjoy your trip and Thank You for choosing African Giant Enterprises. ')
   print(user)



def print_trip(selections_list):
      for selection in selections_list:
         print(selection)
      

confirm_complete_trip()
trip_acceptable()