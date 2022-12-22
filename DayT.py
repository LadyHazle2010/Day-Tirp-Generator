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

   trip = [destination, restaurant, transportation, entertainment]
   return trip

trip = generate_trip()


def confirm_trip():
   
   if confirm_trip == True:
      print('Trip approved!')
   else:
      confirm_trip == False
      print(trip)


     


for selection in trip:
   print(selection)


def gernerate_message():
   msg = f'Great choice!', 'Please comfirm.'
   user_input_result = ('yes or no')
   if user_input_result == True:
      print('yes')
   else:
      user_input_result == False
      print('No')
