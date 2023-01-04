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
      
   
  
confirm_complete_trip 

def trip_acceptable():
   print('Congradulations! Enjoy your trip and Thank You for choosing African Giant Enterprises. ')
   
   trip_acceptable = 'yes'
     
      
for display_info in confirm_complete_trip():
      print(trip_acceptable + display_info)
      


  

 
   
   


def print_trip(selections_list):
      for selection in selections_list:
         print(selection)
      

confirm_complete_trip()
trip_acceptable()



#Print the string and then print the completed trip within that same function. Hint: to do so, you'll
#need to return the confirmed trip from the confirm_complete_trip function into a variable, which will 
#be passed in to a parameter of the trip_acceptable() function (you will need to define that parameter)