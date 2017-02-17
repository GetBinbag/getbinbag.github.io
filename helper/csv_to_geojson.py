import csv, os
import requests
from geopy.geocoders import Nominatim

# using Google Maps API
def get_lat_lon(address, locality, city):
  response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA')
  resp_json_payload = response.json()
  latitude = resp_json_payload['results'][0]['geometry']['location'].get('lat')
  longitude = resp_json_payload['results'][0]['geometry']['location'].get('lng')
  return latitude, longitude

# using geopy library
def get_lat_lon_geopy(address, locality, city):
  geolocator = Nominatim()
  try:
    location = geolocator.geocode(address + ", " + locality + ", " + city)
    print('location 1', location)
    return location.latitude, location.longitude
  except:
    try:
      location = geolocator.geocode(locality + ", " + city)
      print('location 2', location)
      return location.latitude, location.longitude
    except:
      try:
        location = geolocator.geocode(city)
        print('location 3', location)
        return location.latitude, location.longitude
      except:
        return 0,0

# Read in raw data from csv
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

rawData = csv.reader(open(parent_dir + '/data/binbag/recyclers.csv', 'r'), dialect='excel')

# the template. where data from the csv will be formatted to geojson
template = \
    ''' \
    {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                %s,
                %s
              ]
            },
            "properties": {
              "company": "%s",
              "type": "%s",
              "plot": "%s",
              "stage": "%s",
              "industrial": "%s",
              "locality": "%s",
              "city": "%s",
              "state": "%s",
              "country": "%s"
            }
          },
    '''

# the head of the geojson file
output = \
    ''' \
{ 
    "type" : "FeatureCollection",
    "features" : [
    '''

# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    if iter >= 2:
        company_id= row[0]
        company = row[1]
        waste_type = row[2]
        plot = row[3]
        stage = row[4]
        industrial_area = row[5]
        locality = row[6]
        city = row[7]
        state = row[8]
        country = row[9]
        # latitude, longitude = get_lat_lon(locality, city)
        latitude, longitude = get_lat_lon_geopy(industrial_area, locality, city)
        output += template % (longitude, latitude, company, waste_type, plot, stage, industrial_area, locality, city, state, country)

# replace the comma after the last '},'
output = output[:-6]

# the tail of the geojson file
output += \
    ''' \
]
}
    '''
    
# opens an geoJSON file to write the output to
outFileHandle = open(parent_dir + "/data/binbag/output.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()
