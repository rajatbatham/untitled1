import arcpy

try: arcpy.env.workspace = "H:\ArcGIS_Training\Shp"

fcList = arcpy.ListFeatureClasses()
print fcList

for featureClass in fcList:
    arcpy.Copy_management(featureClass, "H:\ArcGIS_Training\data" + featureClass)