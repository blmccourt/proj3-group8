import pandas as pd
import numpy as np
import sqlite3
import requests
import pprint

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
coords_df['lats'] = lats;
coords_df['long'] = longs;



pprint.pp(coords_df)

coords_df.to_csv("./data/coords.csv", index=False)
