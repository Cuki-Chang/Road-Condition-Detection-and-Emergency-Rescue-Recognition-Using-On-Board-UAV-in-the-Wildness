from platform import platform
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date


api = SentinelAPI('username', 'password', 'https://apihub.copernicus.eu/apihub')

# search by polygon, time, and SciHub query keywords
footpoint = geojson_to_wkt(read_geojson('map.geojson'))
products = api.query(footpoint,
                    date=('20210403', date(2022, 4,3)),
                    platformname='Sentinel-2',
                    area_relation='contains',
                    cloudcoverpercentage=(0,60))

# download all results from the search
api.download_all(products) 
#print(products.items())


