from osgeo import gdal,ogr,osr
import numpy as np
from itertools import groupby
from operator import itemgetter

raster1 = gdal.Open('./assets/1.jpg')
raster2 = gdal.Open('./assets/2.jpg')
raster3 = gdal.Open('./assets/3.jpg')

def get_max_width_betwwen_to_rasters(r1,r2):
    return 1 if (r1.RasterXSize*r1.RasterYSize)*(r1.GetGeoTransform()[1]*r1.GetGeoTransform()[5])<(r2.RasterXSize*r2.RasterYSize)*(r2.GetGeoTransform()[1]*r2.GetGeoTransform()[5]) else 2

def connectImages():
  rr=gdal.Translate('./assets/res.jpg', raster2 ,projWin = (0,0,raster2.RasterXSize,raster2.RasterYSize/2))
  sh=gdal.Translate('./assets/res.jpg', raster3,projWin =(0,raster3.RasterYSize/2,raster3.RasterXSize,raster3.RasterYSize))
  gdal.Warp('./assets/res.jpg', [sh,rr], transformerOptions = [ 'SRC_METHOD=NO_GEOTRANSFORM', 'DST_METHOD=NO_GEOTRANSFORM'],width=2500, height=1500)

def get_longest_consecutive_numbers(numbers):
    try:
        idx = max(
            (list(map(itemgetter(0), g)) for i, g in groupby(enumerate(np.diff(numbers)==1), itemgetter(1)) if i), key=len)
        return (idx[0], idx[-1]+1,idx[-1]+1-idx[0]+1)
    except:
        return (0,0,0)

def colorTheGrayLine(arr,data):
  max1=max(arr,key=lambda x: x["counte"][2])
  for i in range(max1["counte"][0],max1["counte"][1]):
      data[0][max1["index"]][i]=0

def createBandForMusk(data):
     arr=[]
     arr2=[]
     for index in range(len(data[0])):
        arr=[] 
        for i in range(len(data[0][0])):
            if(data[0][index][i]==data[1][index][i]==data[2][index][i]):
                data[0][index][i]=1
                arr.append(i)
            else:
                data[0][index][i]=2
        arr2.append({"index":index,"counte":get_longest_consecutive_numbers(list(arr))})
     colorTheGrayLine(arr2,data)                
     return data

def create_mask():
    raster_ds = gdal.Open("./assets/4.jpg", gdal.GA_ReadOnly)
    band=createBandForMusk(raster_ds.ReadAsArray())
    driver = gdal.GetDriverByName('GTiff')
    target_ds = driver.Create("./assets/mask.tif", raster_ds.RasterXSize, raster_ds.RasterYSize)
    target_ds.SetGeoTransform(raster_ds.GetGeoTransform())
    target_ds.SetProjection(raster_ds.GetProjection())
    target_ds.GetRasterBand(1).WriteArray(band[0])
    target_ds = None

connectImages()

