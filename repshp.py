import arcpy

# input data is in NAD 1983 UTM Zone 11N coordinate system
input_features = r"H:\ArcGIS_Training\Shp\myfgdb.gdb\population"

# output data
output_feature_class = r"H:\ArcGIS_Training\Shp\myfgdb.gdb\population1"

# create a spatial reference object for the output coordinate system
out_coordinate_system = arcpy.SpatialReference(4326)

# run the tool
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)