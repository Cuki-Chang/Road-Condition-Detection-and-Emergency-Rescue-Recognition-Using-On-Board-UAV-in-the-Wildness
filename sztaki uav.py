from glob import glob
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import plotly.graph_objects as go


np.seterr(divide='ignore', invalid='ignore')
S_sentinel_bands = glob("F:/19-ROAD/Sentinel_Download_tools/Sentinel_Download_tools/SZTAKI/*.tif")
S_sentinel_bands.sort()

l = []
for i in S_sentinel_bands:
    with rio.open(i, 'r') as f:
        l.append(f.read(1))
arr_st = np.stack(l)
ep.plot_bands(arr_st, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
plt.show()

#ndvi = es.normalized_diff(arr_st[2], arr_st[3])
ndvi = es.normalized_diff(arr_st[0], arr_st[1])

titles = [" Normalized Difference Vegetation Index (NDVI)"]

# Turn off bytescale scaling due to float values for NDVI
ep.plot_bands(ndvi, cmap="RdYlGn", cols=1, title=titles, vmin=-1.0, vmax=1.0)

#ep.plot_bands(ndvi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))
plt.show()



# Create classes and apply to NDVI results
ndvi_class_bins = [-np.inf, 0.2, 0.4,np.inf]
ndvi_landsat_class = np.digitize(ndvi, ndvi_class_bins)

# Apply the nodata mask to the newly classified NDVI data
ndvi_landsat_class = np.ma.masked_where(
    np.ma.getmask(ndvi), ndvi_landsat_class
)
np.unique(ndvi_landsat_class)



# Define color map
nbr_colors = ["gray", "tomato", "g"]
nbr_cmap = ListedColormap(nbr_colors)

# Define class names
ndvi_cat_names = [
    "good condition",
    "soil condition",
    "Vegetation",
]

# Get list of classes
classes = np.unique(ndvi_landsat_class)
classes = classes.tolist()
# The mask returns a value of none in the classes. remove that
classes = classes[0:3]

# Plot your data
fig, ax = plt.subplots(figsize=(12, 12))
im = ax.imshow(ndvi_landsat_class, cmap=nbr_cmap)

ep.plot_bands(ndvi_landsat_class, cmap=nbr_cmap, cols=1, title=titles)

ep.draw_legend(im_ax=im, classes=classes, titles=ndvi_cat_names)
ax.set_title(
    " Normalized Difference Vegetation Index (NDVI) Classes",
    fontsize=14,
)
ax.set_axis_off()

# Auto adjust subplot to fit figure size
plt.tight_layout()



ndwi = es.normalized_diff(arr_st[1], arr_st[2])

ep.plot_bands(ndwi, cmap="RdYlGn", cols=1, vmin=-0.1, vmax=0.9, figsize=(10, 14))

plt.show()
