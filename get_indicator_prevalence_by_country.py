import requests
'''
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
'''
import pandas as pd
import numpy as np
import sqlite3
import pprint
#data_df = pd.read_csv("./data/clean_data.csv")
conn = sqlite3.connect("./data/malnutrition_data.db")
query = "SELECT * FROM clean_data"

data_df = pd.read_sql_query(query, conn)

filtered_data_df = data_df.query("Dimension == 'Age (months)'")

unique_countries = filtered_data_df["Country"].unique()
unique_codes = filtered_data_df["Country ISO-3 Code"].unique()

#pprint.pp(unique_countries)
pprint.pp(unique_codes)
per_country_dfs = []

print(type(unique_countries))
print(type(unique_codes))

unique_countries = np.delete(unique_countries, 28)
unique_codes = np.delete(unique_codes, 28)

pprint.pp(unique_codes)

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
pprint.pp(country_year_indicators_lookup_dict)

prevalence_df = pd.DataFrame()

prevalence_df["code"] = unique_codes;

indicator_list = ["Overweight", "Stunting", "Underweight", "Wasting", "Wasting Severe"]
prevalence_lists_by_indicator = {}

for indicator in indicator_list:
    prevalence_lists_by_indicator[indicator] = []

pprint.pp(prevalence_lists_by_indicator)

#print(country_year_indicators_lookup_dict["CHL"])

for key, value in country_year_indicators_lookup_dict.items():
    for indicator in indicator_list:
        print(value[value["Anthropometric Indicator"] == indicator])
        temp_list = value[value["Anthropometric Indicator"] == indicator]["Prevalence Estimate %"].to_list()
        if(len(temp_list) == 1):
            prevalence_lists_by_indicator[indicator].append(temp_list[0])
        else:
            print(key)

for indicator in indicator_list:
    prevalence_lists_by_indicator[indicator] = []
for entry in country_year_indicators_lookup_dict.values():
    for indicator in indicator_list:
        prevalence = entry[entry["Anthropometric Indicator"] == indicator]["Prevalence Estimate %"]
        #print(type(prevalence))
        #print(type(prevalence["Prevalence Estimate %"]))

        val = (prevalence.to_list())[0]
        print(indicator, entry)
        #print(indicator)
        #pprint.pp(prevalence)
        prevalence_lists_by_indicator[indicator].append(val)

pprint.pp(prevalence_lists_by_indicator)
for indicator in indicator_list:
    prevalence_df[indicator] = prevalence_lists_by_indicator[indicator]
pprint.pp(prevalence_df)

#prevalence_df.to_csv("./data/prevalence.csv")
'''
for country_code in unique_codes:
    coordinates = get_country_coordinates(country_code)
    print(f"Coordinates of {country_code}: {coordinates}")
'''