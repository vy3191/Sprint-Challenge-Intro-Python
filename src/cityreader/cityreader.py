# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing lat and longitude).
# from cities import csv
import csv

class City:

  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"{self.name} @ {self.lat} and {self.lon}"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # Ensure that the lat and lon valuse are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('cities.csv') as csvfile:
    spam_reader = csv.DictReader(csvfile) # Delimiter can be anything, but our file it is a comma
    for row in spam_reader:
      name = row["city"].strip() # trimming the spaces in the string using strip() just like trim() in javaScript
      lat = float(row["lat"])
      lon = float(row["lng"])
      cities.append(City(name,lat,lon))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
print("Please make sure that you separate your values with a comma")
user_input_1 = input("Please enter a valid Latitude-1 and Longitude-1 values:")
lat1 = int(user_input_1.split(",")[0].strip())
lon1 = int(user_input_1.split(",")[1].strip())

user_input_2 = input("Please enter a valid Latitude-2 and Longitude-2 values:")
lat2 = int(user_input_2.split(",")[0].strip())
lon2 = int(user_input_2.split(",")[1].strip())

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  if lat1 > lat2:
    [lat1, lat2] = [lat2, lat1]
  if lon1 > lon2:
    [lon1, lon2]   = [lon2, lon1]
  print('lat1', lat1)
  print('lat2', lat2)
  print('lon1', lon1)
  print('lon2', lon2)

  within = []  
  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  for city in cities:
    total_city = str(city).split("@")
    city_name = total_city[0]
    lat = total_city[1].split("and")[0]
    lon = total_city[1].split("and")[1]

    if float(lat) >= lat1:
      if float(lat) <= lat2:
        if float(lon) >= lon1:
          if float(lon) < lon2:
            tuple_list = []
            tuple_list.append(lat.strip())
            tuple_list.append(lon.strip())
            city_tuple = tuple(tuple_list)
            city_details = f"{city_name}: {city_tuple}"
            within.append(city_details)
  return within


final_results = cityreader_stretch(lat1, lon1, lat2, lon2, cities)

for result in final_results:
  print(result)
