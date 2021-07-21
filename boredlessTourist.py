destinations = ["Paris, France" , "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt", "New York, USA", "Berlim, Germany"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)


attractions= [[] for destination in destinations]

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return 
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']] )
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("New York, USA", ["Empire State", ["skyscraper", "viewing deck"]])
add_attraction('New York, USA', ["Central Park", ["park"]])
add_attraction("New York, USA", ["Brooklyn Bridge", ["monument"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city= attractions[destination_index]
  attractions_with_interest=[]
  for i in attractions_in_city:
    possible_attraction = i
    attraction_tags = i[1]
    for interest in interests:
      if len(attraction_tags) == 1 and interest == attraction_tags[0]:
        attractions_with_interest.append( possible_attraction[0])
      elif len(attraction_tags) > 1 and (interest == attraction_tags[0] or interest == attraction_tags[1]):
        attractions_with_interest.append( possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])



def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string =  "Hi " + traveler[0] + ", we think you'll like these places around " + str(traveler_destination) + ": " + str(traveler_attractions)
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])

  
paris_monument = find_attractions("Paris, France", ["monument"])
alexa_shanghai = get_attractions_for_traveler(['Alexa Sanches', 'Shanghai, China', ['museum']])

alex_losangeles= get_attractions_for_traveler(['Alexandre Conde', "Los Angeles, USA", ["beach"]])
print(alex_losangeles)
