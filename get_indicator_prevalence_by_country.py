import pandas as pd
import sqlite3
import pprint

#data_df = pd.read_csv("./data/clean_data.csv")
conn = sqlite3.connect("./data/malnutrition_data.db")
query = "SELECT * FROM clean_data"

data_df = pd.read_sql_query(query, conn)

filtered_data_df = data_df.query("Dimension == 'Age (months)'")

unique_countries = filtered_data_df["Country"].unique()
unique_countries
per_country_dfs = []

for country in unique_countries:
    temp_df = filtered_data_df.query("Country == @country")
    per_country_dfs.append(temp_df)
country_year_indicators_lookup_dict = {}
for country in unique_countries:
    current_country_df = filtered_data_df.query("Country == @country")
    current_country_years = current_country_df["Year"].unique()
    for year in current_country_years:
        grouped_by_indicator_df = current_country_df.groupby("Anthropometric Indicator")["Prevalence Estimate %"].mean().reset_index()
        country_year_indicators_lookup_dict[country] = grouped_by_indicator_df
pprint.pp(country_year_indicators_lookup_dict)
