# QGIS environment 
layer = iface.activeLayer()

# list functions available for the object
dir(layer)

# functions to get features in a layer
for f in layer.getFeatures():
  print(f)

# Access the attributes of each feature
for f in layer.getFeatures():
  print(f['name'], f['iata_code'])

#  Access the coordinates of the feature
for f in layer.getFeatures():
  geom = f.geometry()
  print(geom.asPoint()) # asPolyline() # asPolygon()

# Calling the x cordinate of the feature
for f in layer.getFeatures():
  geom = f.geometry()
  print(geom.asPoint().x())

# Generate the desired output
for f in layer.getFeatures():
  geom = f.geometry()
  print('{},{},{:.2f},{:.2f}'.format(f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x()))


# output printed on the console
with open('/Users/oduna/Desktop/airports.txt', 'w') as file:
  for f in layer.getFeatures():
    geom = f.geometry()
    line = '{},{},{:.2f},{:.2f}\n'.format(f['name'], f['iata_code'], geom.asPoint().y(), geom.asPoint().x())
    file.write(line)

