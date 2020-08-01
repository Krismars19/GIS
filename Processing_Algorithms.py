{ 'COLUMN_PREFIX' : '_', 'INPUT_RASTER' : 'C:/Users/oduna/Downloads/PRISM_ppt_stable_4kmM3_2017_all_bil/PRISM_ppt_stable_4kmM3_201701_bil.bil', 'INPUT_VECTOR' : 'C:/Users/oduna/Downloads/Zip_Codes/Zip_Codes.shp', 'RASTER_BAND' : 1, 'STATISTICS' : [2] }

# Access names of all the layers
root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  print(layer.name())

#  Iterate over all raster layers, extract the custom prefix
root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  if layer.name().startswith('PRISM'):
    prefix = layer.name()[-6:-4]
    params = {'INPUT_RASTER': layer.name(), 'RASTER_BAND': 1, 'INPUT_VECTOR': 'Zip_Codes', 'COLUMN_PREFIX': prefix+'_', 'STATS': 2}
    processing.run("native:zonalstatistics", params)


# All the codes
root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  print(layer.name())
  
root = QgsProject.instance().layerTreeRoot()
for layer in root.children():
  if layer.name().startswith('PRISM'):
    prefix = layer.name()[-6:-4]
    params = {'INPUT_RASTER': layer.name(), 'RASTER_BAND': 1, 'INPUT_VECTOR': 'Zip_Codes', 'COLUMN_PREFIX': prefix+'_', 'STATS': 2}
    processing.run("qgis:zonalstatistics", params)
    