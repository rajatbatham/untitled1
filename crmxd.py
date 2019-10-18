import arcpy

def print_message(msg):
    # print(msg)
     arcpy.AddMessage(msg)


arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"H:\ArcGIS_Training\Shp\myfgdb.gdb"

mxd = arcpy.mapping.MapDocument(r"H:\ArcGIS_Training\mymxd.mxd")


df = arcpy.mapping.ListDataFrames(mxd)[0]

# featureclass_name = r"H:\ArcGIS_Training\Shp\myfgdb.gdb\population1"

featureclass_name = arcpy.GetParameterAsText(0)

if featureclass_name == "":
    featureclass_name = r"H:\ArcGIS_Training\Shp\myfgdb.gdb\population1"

featcount = arcpy.GetCount_management(featureclass_name)

print_message("{0} has {1} feature(s)".format(featureclass_name,featcount))

# arcpy.Select_analysis(featureclass_name, "Gwalior", "NAME = 'Gwalior'")

arcpy.MakeFeatureLayer_management(featureclass_name,'Population_Rec')
layer = arcpy.mapping.Layer("Population_Rec")
arcpy.mapping.AddLayer(df, layer, "AUTO_ARRANGE")

# mxd.saveACopy(r"H:\ArcGIS_Training\myDocs.mxd")

del mxd
