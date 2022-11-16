from osgeo import gdal

from skimage import io
import cv2
import matplotlib.pyplot as plt
import numpy as np


data  = gdal.Open('sat dataset/orb.TIF')

num_bands = data.RasterCount
print(num_bands)

tmp_img = data.ReadAsArray()

img = tmp_img.T


b = img[:, :, 0]  # 蓝通道
g = img[:, :, 1]  # 绿通道
r = img[:, :, 2]  # 红通道
nir = img[:, :, 3]  # 近红外通道，不可以用imshow直接查看

# 通道拼接  两种方法
#bgr = cv2.merge([b, g, r])
#rgb = np.dstack([r, g, b])

# imshow()必须有图片的名字且像素最大值255，否则会报错
cv2.imshow('b', b)
cv2.imwrite("b.tif", img)

cv2.imshow('g',g)
cv2.imwrite("g.tif", g)

cv2.imshow('r', r)
cv2.imwrite("r.tif", r)

cv2.imshow('nir',nir)
cv2.imwrite("nir.tif", nir)

cv2.waitKey(0)  # 窗口等待响应
cv2.destroyAllWindows()  # 消除窗口
