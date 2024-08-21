import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import pprint

coords_df = pd.read_csv("./data/coords.csv")
pprint.pp(coords_df)

geometry = [Point(xy) for xy in zip(coords_df['long'], coords_df['lats'])]
geo_df = gpd.GeoDataFrame(coords_df, geometry=geometry)

# Convert GeoDataFrame to GeoJSON
geojson_data = geo_df.to_json()

# Save to a file if necessary
with open('./data/coords.geojson', 'w') as f:
    f.write(geojson_data)