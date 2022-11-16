from tqdm import tqdm
from osgeo import gdal,ogr,osr
import numpy as np
from glob import glob

def read_tif(tif_path):
    ds = gdal.Open('tiff_path')
    row = ds.RasterXSize
    col = ds.RasterYSize
    band = ds.RasterCount

    for i in range(band):
        data = ds.GetRasterBand(i+1).ReadAsArray()

        data = np.expand_dims(data , 2)
        if i == 0:
            allarrays = data
        else:
            allarrays = np.concatenate((allarrays, data), axis=2)
    return {'data':allarrays,'transform':ds.GetGeoTransform(),'projection':ds.GetProjection(),'bands':band,'width':row,'height':col}
    # 左上角点坐标 GeoTransform[0],GeoTransform[3] Transform[1] is the pixel width, and Transform[5] is the pixel height
