# CreateArcSDEConnection.py
# Description: Simple example showing use of CreateArcSDEConnectionFile tool

# Import system modules
import arcpy

# Set variables
folderName = r"C:\Users\hp\AppData\Roaming\ESRI\Desktop10.6\ArcCatalog"
fileName = "postgresDatabase.sde"
serverName = "localhost"
serviceName = "5432"
databaseName = "gismap"
authType = "DATABASE_AUTH"
username = "postgres"
password = "postgres"
saveUserInfo = "SAVE_USERNAME"
versionName = "SDE.DEFAULT"
saveVersionInfo = "SAVE_VERSION"

# Process: Use the CreateArcSDEConnectionFile function
arcpy.CreateArcSDEConnectionFile_management(folderName,
                                            fileName,
                                            serverName,
                                            serviceName,
                                            databaseName,
                                            authType,
                                            username,
                                            password,
                                            saveUserInfo,
                                            versionName,
                                            saveVersionInfo)