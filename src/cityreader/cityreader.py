from csv import reader
from os import path
import sys
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"<City: {self.name}: ({self.lat}, {self.lon})>"


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
    with open(path.join(sys.path[0], "cities.csv"), "r") as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            city, state_name, county_name, lat, lng, population, density, timezone, zips = row
            cities.append(City(city, float(lat), float(lng)))

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


def parse_input(string):
    return tuple(map(lambda x: float(x), string.split(",")))


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    lower_lat = min(lat1, lat2)
    upper_lat = max(lat1, lat2)

    lower_lon = min(lon1, lon2)
    upper_lon = max(lon1, lon2)

    for c in cities:
        if c.lat >= lower_lat and c.lat <= upper_lat:
            if c.lon >= lower_lon and c.lon <= upper_lon:
                within.append(c)

    return within


if __name__ == "__main__":
    print("Input coordinates in the following format: lat, lon")
    a = parse_input(
        input("Enter the latitude and longitude of the first coordinate: "))
    b = parse_input(
        input("Enter the latitude and longitude of the second coordinate: "))

    result = cityreader_stretch(a[0], a[1], b[0], b[1], cities)

    for r in result:
        print(r)
