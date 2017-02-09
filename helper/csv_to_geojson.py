import csv, os

# Read in raw data from csv
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

rawData = csv.reader(open(parent_dir + '/data/binbag/sweetgreen.csv', 'r'), dialect='excel')

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
              "name": "%s",
              "phoneFormatted": "%s",
              "phone": "%s",
              "address": "%s",
              "city": "%s",
              "country": "%s",
              "crossStreet": "%s",
              "postalCode": "%s",
              "state": "%s"
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
        name = row[0]
        longitude = row[1]
        latitude = row[2]
        altitude = row[3]
        geometry = row[4]
        phoneFormatted = row[5]
        phone = row[6]
        address = row[7]
        city = row[8]
        country = row[9]
        crossStreet = row[10]
        postalCode = row[11]
        state = row[12]
        output += template % (latitude, longitude, name, phoneFormatted, phone, address, city, country, crossStreet, postalCode, state)
        # output += template % (latitude, longitude)

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
