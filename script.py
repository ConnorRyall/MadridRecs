destinations = ["Sol", "Chueca", "Malasaña", "Chamberí", "Salamanca", "Lavapiés", "La Latina", "Las Letras", "Los Austrias"]

test_traveler = ['John Doe', 'Chamberí', ['bar']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = [] 
for destination in destinations:
  attractions.append([])

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

add_attraction("Chamberí", ['Bar Trafalgar', ['bar', 'cozy', 'cocktails']])
add_attraction("Chamberí", ['The Dash', ['bar', 'cozy', 'cocktails']])
add_attraction("Chamberí", ['Taberna La Mina', ['food', 'seafood', 'bar', ]])
add_attraction("Chamberí", ['Bendita Burger', ['food', 'burger', 'restaurant']])
add_attraction("Chamberí", ['Gingerboy', ['food', 'takeaway', 'thai']])
add_attraction("Chamberí", ['Mama Campo', ['food', 'terrace', 'bar', 'restaurant']])
add_attraction("Chamberí", ['Anubis Trafalgar', ['terrace', 'bar', 'restaurant']])
add_attraction("Chamberí", ['Toma Café 2', ['coffee', 'pastries', 'bakery']])
add_attraction("Chamberí", ['Alma Bakery', ['bakery', 'coffee', 'takeaway']])
add_attraction("Chamberí", ['Mercado Vallehermoso', ['foodmarket', 'streetfood']])
add_attraction("Chamberí", ['Sagaretxe', ['basque', 'spanish', 'tapas']])
add_attraction("Chamberí", ['Quesu', ['Asturian', 'dinner', 'steak']])
add_attraction("Chamberí", ['Hundred', ['burger', 'american']])
add_attraction("Chueca", ['Biang Biang Bar', ['chinese', 'restaurant']])
add_attraction("Chueca", ['Mad Mad Vegan', ['vegan', 'burgers', 'restaurant']])
add_attraction("Chueca", ['Zenith Brunch', ['restaurant', 'brunch', 'american']])
add_attraction("La Latina", ['El Cedrón Wine Bar', ['spanish', 'restaurant', 'wine']])
add_attraction("Malasaña", ['Lab 84', ['pizza', 'restaurant', 'sitdown', 'takeaway']])
add_attraction("Malasaña", ['212 NY PIZZA', ['pizza', 'takeaway']])
add_attraction("Malasaña", ['El Buda Feliz', ['chinese', 'food']])
add_attraction("Malasaña", ['Kungfu Bar', ['chinese', 'food', 'cheap']])
add_attraction("Malasaña", ['Gorila', ['bar', 'cozy', 'music']])
add_attraction("Malasaña", ['Santamaría', ['cocktails', 'cozy']])
add_attraction("Malasaña", ['1862 Dry Bar', ['cocktails', 'cozy', 'nightcap']])
add_attraction("Malasaña", ['Thunder Vegan', ['food', 'vegan', 'takeaway', 'burgers']])
add_attraction("Malasaña", ['Grosso Napoletano', ['pizza', 'sitdown', 'restaurant']])
add_attraction("Salamanca", ['Teitu', ['restaurant', 'expensive', 'meat']])
add_attraction("Salamanca", ['Museo Arqueológico Nacional', ['museum']])
add_attraction("Salamanca", ['Brindis Bar', ['bar']])
add_attraction("Sol", ['Takos Al Pastor', ['tacos', 'mexican', 'restaurant', 'cheap', 'food']])
add_attraction("Lavapiés", ['El Rincón de Marco', ['food', 'cuban', 'friedchicken']])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + str(traveler[0]) + ", we think you'll like these places around " + str(traveler[1]) + ": " + str(traveler_attractions) + ". "
  return interests_string

test = get_attractions_for_traveler(test_traveler)

print(test)