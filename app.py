from osgeo import gdal,ogr,osr
import json
fn="./assets/AFG_adm2.shp"
data=ogr.Open(fn,1)
layer = data.GetLayer()

def find_area_grater_than_1():
    for feature in layer:
        geom = feature.GetGeometryRef()
        area = geom.GetArea()
        if(area>=1):
         print(f"FID: {str(feature.GetFID())}, NAME_2:{feature.GetField('NAME_2')} ,area:{str(area)}")
         print(json.loads(feature.ExportToJson())['geometry']['coordinates'])

def add_field_of_distance_from_charBurjak():
    filter=next((i for i in layer if i["NAME_2"] == "Char Burjak"), None)
    new_field = ogr.FieldDefn('new_field', ogr.OFTInteger)
    layer.CreateField(new_field)
    for feature in layer:
        feature.SetField('new_field', 1)
        if(feature.GetGeometryRef().Distance(filter.GetGeometryRef())>1):
           feature.SetField("new_field",0)
        else:
          feature.SetField("new_field",1)
        layer.SetFeature(feature)

def count_neighbors(feature):
   counter=0
   for geom in layer:
        n2=geom.GetGeometryRef()
        if(feature.Touches(n2)):
           counter+=1
   return counter

def add_field_of_neigbords():
   new_field = ogr.FieldDefn('neighbors', ogr.OFTInteger)
   layer.CreateField(new_field)
   for feature in range(len(layer)):
       n1=layer.GetFeature(feature)
       geom=n1.GetGeometryRef()
       counter=count_neighbors(geom)
       n1.SetField("neighbors",counter)
       counter=0 
       layer.SetFeature(n1)  

def create_shapefile():
   driver = ogr.GetDriverByName("ESRI Shapefile")   
   ds = driver.CreateDataSource("line.shp")   
   srs =  osr.SpatialReference()
   srs.ImportFromEPSG(4326)   
   layer = ds.CreateLayer("line", srs, ogr.wkbLineString)   
   idField = ogr.FieldDefn("id", ogr.OFTInteger)
   layer.CreateField(idField)   
   ds = None

def create_feature(ft):
    DataSource=ogr.Open("line.shp",1)
    layer1 = DataSource.GetLayer()
    featureDefn = layer1.GetLayerDefn()
    feature = ogr.Feature(featureDefn)
    feature.SetGeometry(ft)
    feature.SetField("id", 1)
    layer1.CreateFeature(feature)   
    feature = None

def create_line_string_of_area_grater_than_1():
   create_shapefile()
   data=ogr.Open(fn,1)
   layer = data.GetLayer()
   for feature1 in layer:
        geom = feature1.GetGeometryRef()
        area = geom.GetArea()
        if(area>=1):
           create_feature(geom.GetGeometryRef(0))

def connect_line_between_the_tow_entitys(x1,y1,x2,y2):
   line = ogr.Geometry(ogr.wkbLineString)
   line.AddPoint(x1, y1)
   line.AddPoint(x2, y2)
   create_feature(line)

def preper_the_points_for_the_line():
   filter1 = list(filter(lambda x:x.GetGeometryRef().GetArea()>1,layer))
   max_area=max(filter1,key=lambda x: x.GetGeometryRef().GetArea())
   max_negibord=max(layer,key=lambda x: x['neighbors'])
   geom1=max_area.GetGeometryRef().GetGeometryRef(0)
   geom2=max_negibord.GetGeometryRef().GetGeometryRef(0)
   connect_line_between_the_tow_entitys(geom1.GetX(1),geom1.GetY(1),geom2.GetX(1),geom2.GetY(1))


     
         

