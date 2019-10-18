import arcpy
import os

# Set environment settings
arcpy.env.workspace = r"H:/ArcGIS_Training/Shp/myfgdb.gdb"
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = r"H:/ArcGIS_Training/Shp/myfgdb1.gdb"

try:
    # Use ListFeatureClasses to generate a list of inputs
    for infc in arcpy.ListFeatureClasses():

        # Determine if the input has a defined coordinate system, can't project it if it does not
        dsc = arcpy.Describe(infc)
        print('Hello')
        if dsc.spatialReference.Name == "Unknown":
            print ('skipped this fc due to undefined coordinate system: ' + infc)
        else:
            # Determine the new output feature class path and name
            outfc = os.path.join(outWorkspace, infc)
            print('Working')
            # Set output coordinate system
            outCS = arcpy.SpatialReference('GCS_WGS_1966')
            print('Working1')
            # run project tool
            arcpy.Project_management(infc, outfc, outCS)
            print('Working2')
            # check messages
            print(arcpy.GetMessages())

except arcpy.ExecuteError:
    print('Failed1')
    print(arcpy.GetMessages(2))

except Exception as ex:
    print('Failed2')
    print(ex.args[0])