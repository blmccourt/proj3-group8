import pandas as pd
import numpy as np
import sqlite3
import requests
import pprint

import sys

## GET COORDINATES PER ISO CODE

def get_country_coordinates(iso_code):
    # API endpoint
    url = f"https://restcountries.com/v3.1/alpha/{iso_code}"
    
    # Send GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        latlng = data[0]['latlng']  # latlng is a list [latitude, longitude]
        return latlng
    else:
        return None

skip_coords_retrieval = True

if(skip_coords_retrieval):
    coords_df = pd.read_csv("./data/coords.csv")
else:
    conn = sqlite3.connect("./data/malnutrition_data.db")
    query = "SELECT * FROM clean_data"

    data_df = pd.read_sql_query(query, conn)

    filtered_data_df = data_df.query("Dimension == 'Age (months)'")

    unique_countries = filtered_data_df["Country"].unique()
    unique_codes = filtered_data_df["Country ISO-3 Code"].unique()

    ## remove Chile from analysis
    unique_countries = np.delete(unique_countries, 28)
    unique_codes = np.delete(unique_codes, 28)

    lats = []
    longs = []

    #iso_coords_dict = {}
    for code in unique_codes:
        temp_coords = get_country_coordinates(code)
        lats.append(temp_coords[0])
        longs.append(temp_coords[1])
        print(f"added coords for {code}...")


    coords_df = pd.DataFrame();

    coords_df['country'] = unique_countries;
    coords_df['code'] = unique_codes;
    coords_df['lat'] = lats;
    coords_df['lon'] = longs;

    pprint.pp(coords_df)

    coords_df.to_csv("./data/coords.csv", index=False)

### QUERY RELEVANT DATA FROM DATABASE (all)

conn = sqlite3.connect("./data/malnutrition_data.db")
query = "SELECT * FROM clean_data"

data_df = pd.read_sql_query(query, conn)

filtered_data_df = data_df.query("Dimension == 'Age (months)'")

unique_countries = filtered_data_df["Country"].unique()
unique_codes = filtered_data_df["Country ISO-3 Code"].unique()

#pprint.pp(unique_countries)
#pprint.pp(unique_codes)
per_country_dfs = []

#print(type(unique_countries))
#print(type(unique_codes))

# remove CHL from data due to missing indicator
unique_countries = np.delete(unique_countries, 28)
unique_codes = np.delete(unique_codes, 28)

#pprint.pp(unique_codes)

#unique_countries.delete("Chile")
#unique_codes.delete("CHL")
#exit(0)
for country_code in unique_codes:
    temp_df = filtered_data_df.query("`Country ISO-3 Code` == @country_code")
    per_country_dfs.append(temp_df)

country_year_indicators_lookup_dict = {}

for country_code in unique_codes:
    current_country_df = filtered_data_df.query("`Country ISO-3 Code` == @country_code")
    current_country_years = current_country_df["Year"].unique()
    for year in current_country_years:
        grouped_by_indicator_df = current_country_df.groupby("Anthropometric Indicator")["Prevalence Estimate %"].mean().reset_index()
        country_year_indicators_lookup_dict[country_code] = grouped_by_indicator_df
        #country_year_indicators_lookup_dict[country_code].append(grouped_by_indicator_df)
        #country_year_indicators_lookup_dict[country_code].append(get_country_coordinates(country_code))
#pprint.pp(country_year_indicators_lookup_dict)
#pprint.pp(country_year_indicators_lookup_dict)

prevalence_df = pd.DataFrame()

prevalence_df["code"] = unique_codes;

indicators = ["Overweight", "Stunting", "Underweight", "Wasting", "Wasting Severe"]
prevalence_lists_by_indicator = {}

for indicator in indicators:
    prevalence_lists_by_indicator[indicator] = []

#pprint.pp(prevalence_lists_by_indicator)

#print(country_year_indicators_lookup_dict["CHL"])

for key, value in country_year_indicators_lookup_dict.items():
    for indicator in indicators:
        #print(value[value["Anthropometric Indicator"] == indicator])
        temp_list = value[value["Anthropometric Indicator"] == indicator]["Prevalence Estimate %"].to_list()
        if(len(temp_list) == 1):
            prevalence_lists_by_indicator[indicator].append(temp_list[0])
        else:
            print(key)

for indicator in indicators:
    prevalence_lists_by_indicator[indicator] = []
for entry in country_year_indicators_lookup_dict.values():
    for indicator in indicators:
        prevalence = entry[entry["Anthropometric Indicator"] == indicator]["Prevalence Estimate %"]
        #print(type(prevalence))
        #print(type(prevalence["Prevalence Estimate %"]))

        val = (prevalence.to_list())[0]
        #print(indicator, entry)
        #print(indicator)
        #pprint.pp(prevalence)
        prevalence_lists_by_indicator[indicator].append(val)

#pprint.pp(prevalence_lists_by_indicator)
for indicator in indicators:
    prevalence_df[indicator] = prevalence_lists_by_indicator[indicator]
#pprint.pp(prevalence_df)

### ASSEMBLE GEOJSON DATA

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import pprint
import geojson

def df_to_geojson(df, properties, lat='lat', lon='lon'):
    features=[]
    for _, row in df.iterrows():
        feature = geojson.Feature(
            geometry = geojson.Point((row[lon], row[lat])),
            properties={prop: row[prop] for prop in properties}
        )
        features.append(feature)
    return geojson.FeatureCollection(features)

#coords_df = pd.read_csv("./data/coords.csv")
pprint.pp(coords_df)
pprint.pp(prevalence_df)

'''
geometry = [Point(xy) for xy in zip(coords_df['long'], coords_df['lats'])]
geo_df = gpd.GeoDataFrame(coords_df, geometry=geometry)

# Convert GeoDataFrame to GeoJSON
geojson_data = geo_df.to_json()

# Save to a file if necessary
with open('./data/coords.geojson', 'w') as f:
    f.write(geojson_data)
'''

overweight_layer_df = coords_df.copy()
overweight_layer_df["prevalence"] = prevalence_df["Overweight"]

stunting_layer_df = coords_df.copy()
stunting_layer_df["prevalence"] = prevalence_df["Stunting"]

underweight_layer_df = coords_df.copy()
underweight_layer_df["prevalence"] = prevalence_df["Underweight"]

wasting_layer_df = coords_df.copy()
wasting_layer_df["prevalence"] = prevalence_df["Wasting"]

wasting_severe_layer_df = coords_df.copy()
wasting_severe_layer_df["prevalence"] = prevalence_df["Wasting Severe"]

print("overweight_layer_df")
pprint.pp(overweight_layer_df)
print("stunting_layer_df")
pprint.pp(stunting_layer_df)
print("underweight_layer_df")
pprint.pp(underweight_layer_df)
print("wasting_layer_df")
pprint.pp(wasting_layer_df)
print("wasting_severe_layer_df")
pprint.pp(wasting_severe_layer_df)

overweight_layer_geojson = df_to_geojson(overweight_layer_df, ["country", "prevalence"])
stunting_layer_geojson = df_to_geojson(stunting_layer_df, ["country", "prevalence"])
underweight_layer_geojson = df_to_geojson(underweight_layer_df, ["country", "prevalence"])
wasting_layer_geojson = df_to_geojson(wasting_layer_df, ["country", "prevalence"])
wasting_severe_layer_geojson = df_to_geojson(wasting_severe_layer_df, ["country", "prevalence"])
#pprint.pp(overweight_layer_geojson)

with open("./data/overweight_layer.geojson", 'w') as f:
    geojson.dump(overweight_layer_geojson, f)

with open("./data/stunting_layer.geojson", 'w') as f:
    geojson.dump(stunting_layer_geojson, f)

with open("./data/underweight_layer.geojson", 'w') as f:
    geojson.dump(underweight_layer_geojson, f)

with open("./data/wasting_layer.geojson", 'w') as f:
    geojson.dump(wasting_layer_geojson, f)

with open("./data/wasting_severe_layer.geojson", 'w') as f:
    geojson.dump(wasting_severe_layer_geojson, f)


