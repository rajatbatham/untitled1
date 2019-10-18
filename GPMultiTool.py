import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"H:/ArcGIS_Training/FrameworkProject/FrameWorkProject.gdb"
#CountryName = 'Chandigarh'
CountryName = arcpy.GetParameterAsText(0)
arcpy.Select_analysis(in_features=r"G:\ArcGIS\ArcGIS Essential Training\ArcGIS Essential Training\Ex_Files_ArcGIS_EssT\Ex_Files_ArcGIS_EssT\ExerciseFiles\Chapter_00\Chapter_00_Data\States_Provinces.gdb\States_Provinces",
                      out_feature_class="H:/ArcGIS_Training/FrameworkProject/FrameWorkProject.gdb/SelState",
                      where_clause="name = '{0}'".format(CountryName))

arcpy.Buffer_analysis(in_features="SelState", out_feature_class="SelState_Buffer", buffer_distance_or_field="100 Kilometers", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field="", method="PLANAR")

arcpy.Clip_analysis(in_features=r"G:\ArcGIS\ArcGIS Essential Training\ArcGIS Essential Training\Ex_Files_ArcGIS_EssT\Ex_Files_ArcGIS_EssT\ExerciseFiles\Chapter_00\Chapter_00_Data\Populated_Places.shp", clip_features="SelState_Buffer", out_feature_class="SelState_Places_Clip", cluster_tolerance="")

arcpy.AddMessage("Thera are {0} Populated Places in or within 100 km of {1}".format(
    arcpy.GetCount_management(in_rows="SelState_Places_Clip"),CountryName))
