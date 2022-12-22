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


# def confirm_trip():

   
   
   
def print_trip(trip):
   for selection in trip:
      print(selection)
   
     
print_trip(trip) 

print('Does the trip suffice?')
user = input()
print(user)




# def gernerate_message():
#    msg = f'Great choice!', 'Please comfirm.'
#    user_input_result = ('yes or no')
#    if user_input_result == True:
#       print('yes')
#    else:
#       user_input_result == False
#       print('No')
