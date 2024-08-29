# Global Malnutrition Estimates in Children Under 5 Years of Age

## Group presentation

[Global Malnutrition Analysis Presentation](https://docs.google.com/presentation/d/1vJtmyZMTajHY_IHafsaot_RL99pl2x4QcZPWVB5AQaY/edit?usp=sharing)

## Project proposal
Group 8: Brenda McCourt; Kayla Vaccaro, Krutika Desai, Naveen Chakicherla

### 1.0 Overview: 
Develop a donation portal to combat malnutrition through targeted financial contributions and resource allocation. 

### 2.0 Benefits: 
Enhance efficiency in fundraising, increase donor engagement, better tracking of donations, and more effective resource distribution. 

### 3.0  Dataset description:
🔗  Health Inequality Monitor dataset

This dataset contains data on child malnutrition indicators from household surveys disaggregated by age, economic status, education, place of residence, sex and subnational region, based on UNICEF-WHO-World Bank Joint Child Malnutrition Estimates.

### 4.0 Key Tasks and/or Goals:
### 4.1 Extraction:
Identify Data Sources: Approach used for identifying 
Data Extraction Methods:

### 4.2 Transform
Objective: Process and refine the extracted data to make it suitable for analysis.
Data Cleaning: Handle missing values, remove duplicates, and correct errors. This ensures that the data is accurate and reliable.
Data Formatting: Convert data into a consistent format, such as standardizing date formats, currency symbols, or text case.
Data Aggregation: Summarize or aggregate data as needed. This might involve calculating totals, averages, or other summary statistics.
Data Integration: Combine data from different sources into a unified format. This may involve merging tables, joining datasets, or aligning different data schemas.
Data Transformation: Apply necessary transformations such as normalization, denormalization, or applying business rules to derive new metrics or dimensions.


### 5.0 Procedure for Visualization:

- Line Graph: Showing trends in demographics versus malnutrition population 
- World Map: Visualize the percentage of children under 5 affected by malnutrition by country and year, helping users identify regions with the highest prevalence.
- Pie Charts to show the makeup of each population but gender, age, economic status, and place of residency. 

### 6.0 Expected Outcomes:

This project is expected to deliver a comprehensive, interactive platform that effectively informs and engages users on the issue of global child malnutrition. By providing clear and accessible visualizations, we anticipate increased donor understanding of the factors contributing to malnutrition and the regions most affected. This heightened awareness will likely lead to more targeted and meaningful donations, as users can see the direct impact of their contributions. Ultimately, the project aims to enhance donor participation, drive greater financial support for malnutrition relief efforts, and contribute to the broader goal of reducing child malnutrition globally.

### 7.0 Conclusion:

Our goal is to provide robust data analytics for both donors and organizations, offering insights into the impact of contributions and enabling the customization of donor options based on specific regions, types of aid, and other critical factors. By tailoring these options, we empower donors to make informed decisions and direct their support where it will have the most significant effect. Additionally, we will explore key research questions, such as the trends of malnutrition in the U.S., the role of maternal education, and the influence of economic status on child malnutrition. This comprehensive approach aims to drive more effective interventions and maximize the positive outcomes of charitable efforts.


## Overview of the project and its purpose
Analyzing and visualizing global malnutrition data for children under five, with a focus on providing actionable insights to potential donors into inequality factors where resources can be focused.
Analyzing and visualizing global malnutrition data for children under five enhances fundraising efficiency and donor engagement by targeting resources effectively, increasing transparency, and communicating the urgency of the issue. This approach allows organizations to make informed decisions, build trust with donors, and optimize their impact on combating malnutrition.

--- 

## Instructions on how to use and interact with the project

### ETL
The entirety of the ETL workflow was done in [`ETL.ipynb`](https://github.com/blmccourt/proj3-group8/blob/main/ETL.ipynb) and can be executed like a regular Jupyter notebook.

### Data Analysis
Coding done to analyze the data can be found [here](analytics.ipynb) and utilizes the [malnutrition database](https://github.com/blmccourt/proj3-group8/blob/main/data/malnutrition_data.db)

#### Dependencies
```
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from matplotlib import style
style.use('fivethirtyeight')
import numpy as np
import seaborn as sns
```

### Data Visualizations

---

#### 1. Tableau
- You dont have to create account to view dashboard and click on right hand side to see various indicators and data
- [Data Summary Interactive Dashboard](https://public.tableau.com/views/DataSummaryAll/DataSummary?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Weight Indicator Dashboard](https://public.tableau.com/views/WeightIndicatorProd/WeightInd2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Education Malnutrition Dashboard](https://public.tableau.com/views/EducationMalnutritionData/EducationDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Income Based Malnutrition Country Dashboard](https://public.tableau.com/views/MalnutritionData_17238512473000/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

#### 2. Leaflet
After cloning the repository to your local machine, `index.html` can be opened in your web browser of choice and will render the Leaflet map. The GeoJSON data established in `assemble_geojson.ipynb` is hard-coded into `define_raw_geojson_data.js`, so running the Python notebook isn't necessary to see the web visual.

## Ethical considerations
In this project, careful attention was given to ethical considerations, particularly concerning data privacy and security. No personal identifying information (PII) was included in the dataset, ensuring the anonymity of individuals. The dataset had previously undergone a thorough Extract, Transform, and Load (ETL) process by UNICEF, WHO, and the World Bank, which further safeguarded the integrity and confidentiality of the information. This prior processing ensured that only aggregated, anonymized data was used, aligning with ethical standards for data handling and protection.

## Data sources

- [Child Malnutrition Dataset (UNICEF/WHO/World Bank)](https://www.who.int/data/sets/health-inequality-monitor-dataset#nut)
- [UNICEF Data Warehouse](https://data.unicef.org/resources/data_explorer/unicef_f/?ag=UNICEF&df=GLOBAL_DATAFLOW&ver=1.0&dq=.NT_ANT_WHZ_NE3+NT_ANT_HAZ_NE2+NT_BW_LBW+NT_ANT_WHZ_NE2..&startPeriod=2016&endPeriod=2023)
- [WHO Child Malnutrition Database](https://platform.who.int/nutrition/malnutrition-database/database-search)
- [Joint Malnutrition Estimates (2023 Edition)](https://public.tableau.com/app/profile/unicefdata/viz/JointMalnutritionEstimates2023Edition_16841450949590/WHO_re)

## Files and folders

### ETL

1. **[`ETL.ipynb`](https://github.com/blmccourt/proj3-group8/blob/main/ETL.ipynb)**

- Jupyter notebook with scripts for *Part 1: Extraction, Transformation, and Loading*.

2. **[`Data`](https://github.com/blmccourt/proj3-group8/tree/main/data)**

- Folder with raw data and metadata from UNICEF/WB/WHO, database schema and files, and resulting clean data file.
  - [metadata.pdf](https://github.com/blmccourt/proj3-group8/blob/main/data/metadata.pdf)
  - [raw_data.xlsx](https://github.com/blmccourt/proj3-group8/blob/main/data/raw_data.xlsx)
  - [db_schema.sql](https://github.com/blmccourt/proj3-group8/blob/main/data/db_schema.sql)
  - [malnutrition_data.db](https://github.com/blmccourt/proj3-group8/blob/main/data/malnutrition_data.db)
  - [clean_data.xlsx](https://github.com/blmccourt/proj3-group8/blob/main/data/clean_data.csv)

### Data Analysis

#### Dimensions Analyzed
- Age group vs malnutrition (2022)
- Sex vs malnutrition (2022)
- Place of residence vs malnutrition (2022)
- Economic status vs malnutrition (2022)
- Education (mother) vs malnutrition (2022)
- Year vs Anthropometric Indicator
- Region vs Anthropometric Indicator
- Country vs Anthropometric Indicator
- Year + Country vs Anthropometric Indicators
- Comparing the countries with the largest average increase/decrease in malnutrition to the trends in education
- Education (mother) for African region (largest malnutrition population that is increasing)

--- 

#### Results

##### Age group vs malnutrition (2022)
The age group with the largest combined population for all countries in 2022 is '36-47 months' with a total population of 8701588.483398438.

![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/AgeGroups.png)


##### Sex vs malnutrition (2022)
There is not a strong correlation between sex and malnutrition. There is an almost 50/50 split for each country:

![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/Sex.png)

Country with the Largest Difference in Male vs Female Population for Under-Five:
Country: Niger
Year: 2022
Male Population: 73900848.00
Female Population: 72682044.00
Difference: 1218804.00


##### Place of residence vs malnutrition (2022)
If I were to add another database to this project a demographic set of data would be nice to compare. This would allow us to see if this is causing malnutrition or if all populations are experiencing these dimensional values.

There is not a stronger correlation between place of residence and malnutrition as it differs from country to country. This is most likely due to where the overall population is located and the makeup of each country. 80% of Mexico's population lives in an urban area, so this explains why 73.3% of their child malnourishment is located in urban areas.

![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/AfgPOR.png)
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/MexPOR.png)

Examples: Country | Population (%) living in urban area | % of malnourished children in urban areas

- Mexico | 80.0 | 73.3
- Afghanistan | 26.31 | 22.1
- Ecuador | 64.79 | 64.4
- Yemen | 38.55 | 27.3
- Kenya | 30.0% | 33.1

##### Economic status vs malnutrition (2022)

Each quartile (5) makes up a fifth of the pie. There may be a correlation between poor and wasting / rich and overweight, but overall: no single economic status is dominating the malnourished population.

![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/EconomicStatus.png)

Investigated if there was a relationship between Quintile 1 (poorest) and Quintile 5 (richest) with the type of Anthropometric Indicator, overweight or underweight. 

- Under-Five Population (approximately) underweight in Quintile 1 (poorest) for 2022: 25762.13739013672
- Under-Five Population (approximately) overweight in Quintile 5 (richest) for 2022: 18433.328399658203
- Under-Five Population (approximately) overweight in Quintile 1 (poorest) for 2022: 25730.726989746094
- Under-Five Population (approximately) underweight in Quintile 5 (richest) for 2022: 18648.14956665039

For underweight and overweight there is a larger population for both in Quintile 1 (poorest). This may be due to food deserts or no access to quality food, resulting in obesity. 


##### Education (mother) vs malnutrition (2022)

Average Population of Under-Five Children by Mother's Education Status (2022):
  Education Status: No education, Average Population: 4019.87
  Education Status: Primary education, Average Population: 2722.39
  Education Status: Secondary or higher education, Average Population: 4866.78

##### Year vs Anthropometric Indicator

- Overweight
- Stunting
- Underweight
- Wasting
- Wasting Severe
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/AIbyYear.png)

There is an average increase in all five Anthropometric Indicators fromm 1990 to 2023


##### Region vs Anthropometric Indicator

All Anthropometric Indicators populations are nearly equivalent. This graph only shows how the African Region has the largest population of malnourished children under the age of five. 
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/AIbyRegion.png)


##### Country vs Anthropometric Indicator

These trends showed the same as region vs Anthropometric Indicators. Nothing significant to note.

##### Year + Country vs Anthropometric Indicators

Some of the countries only have one or two years of data, so I removed any countries that did not have at least ten years worth of data. Along with this I removed any major outliers as they were causing issues with the graph.
`countries_with_sufficient_data = country_year_counts[country_year_counts >= 10].index`
The country with the largest average increase in all indicators is Senegal, with an average increase of approximately 792.17 children per year and an R-value of 0.47.
The country with the largest average decrease in all indicators is Malawi, with an average decrease of approximately -442.76 children per year and an R-value of -0.24.
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/Senegal.png)
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/Malawi.png)

##### Comparing the countries with the largest average increase/decrease in malnutrition to the trends in education

Malawi has an increase in secondary education, indicating that higher education can decrease malnourishment. Secondary or higher education is also greater for Malawi. Sengal has a significant uneducated population across all years available in the data. This indicated that a less educated population will cause an increase in malnourishment.
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/SenegalEd.png)
![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/MalawiEd.png)



##### Education (mother) for African region (largest malnutrition population that is increasing)

Consistantly there is a larger population of 'no education', further supporting that less education causes an increase in malnourishment.

![Alt text](https://github.com/blmccourt/proj3-group8/blob/main/Analysis/AfricanEducation.png)


### Data Visualizations

1. **Leaflet**

- **[`assemble_geojson.ipynb`](https://github.com/blmccourt/proj3-group8/blob/main/assemble_geojson.ipynb)**

  - Jupyter notebook with scripts for retrieving geographic coordinates for countries studied, and establishing GeoJSON data for use in web visualization

- **[`index.html`](https://github.com/blmccourt/proj3-group8/blob/main/index.html)**

  - Web page with a Leaflet visualization which superimposes a user-selected anthropometric factor onto a map for spatial demonstration of malnutrition indicators. Refers to `define_raw_geojson_data.js` and `render_heatmap.js`

- **[`/static/js/define_raw_geojson_data.js`](https://github.com/blmccourt/proj3-group8/blob/main/static/js/define_raw_geojson_data.js)**

  - JavaScript file with static variable definitions, each containing the raw GeoJSON data established in `assemble_geojson.ipynb`

- **[`/static/js/render_heatmap.js`](https://github.com/blmccourt/proj3-group8/blob/main/static/js/render_heatmap.js)**

  - JavaScript file with main rendering logic, using Leaflet. Interactivity is added by establishing an event listener function that re-renders using data established in `define_raw_geojson_data.js` as a superimposed Leaflet layer
 
2.  **Tableau**
- [Data Summary Interactive Dashboard](https://public.tableau.com/views/DataSummaryAll/DataSummary?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Weight Indicator Dashboard](https://public.tableau.com/views/WeightIndicatorProd/WeightInd2?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Education Malnutrition Dashboard](https://public.tableau.com/views/EducationMalnutritionData/EducationDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- [Income Based Malnutrition Country Dashboard](https://public.tableau.com/views/MalnutritionData_17238512473000/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Citations

1. **UN Habitat on Mexico's Urbanization**:
   UN-Habitat. "Mexico: Country Overview." Accessed August 28, 2024. [https://unhabitat.org/mexico#:~:text=Country%3A%20Overview,-No.&text=1970%20and%20...-,Mexico%20is%20a%20highly%20urbanized%20country%20with%20nearly%2080%20percent,population%20living%20in%20urban%20areas](https://unhabitat.org/mexico#:~:text=Country%3A%20Overview,-No.&text=1970%20and%20...-,Mexico%20is%20a%20highly%20urbanized%20country%20with%20nearly%2080%20percent,population%20living%20in%20urban%20areas).

2. **Afghanistan Urban Population 1960-2024**:
   Macrotrends. "Afghanistan Urban Population 1960-2024." Accessed August 28, 2024. [https://www.macrotrends.net/countries/AFG/urban-population](https://www.macrotrends.net/countries/AFG/urban-population).

3. **Ecuador - Urban Population (% Of Total)**:
   Trading Economics. "Ecuador - Urban Population (% Of Total)." Accessed August 28, 2024. [https://tradingeconomics.com/ecuador/urban-population](https://tradingeconomics.com/ecuador/urban-population).

4. **Yemen Urban Population 1960-2024**:
   Macrotrends. "Yemen Urban Population 1960-2024." Accessed August 28, 2024. [https://www.macrotrends.net/countries/YEM/urban-population](https://www.macrotrends.net/countries/YEM/urban-population).

5. **Our World in Data on Population Growth**:
   Ritchie, Hannah, and Max Roser. "Population Growth Over Time." Our World in Data. Accessed August 28, 2024. [https://ourworldindata.org/population-growth-over-time](https://ourworldindata.org/population-growth-over-time).

6. **Statista on Fertility Rate in Africa**:
   Statista. "Fertility Rate in Africa." Accessed August 28, 2024. [https://www.statista.com/statistics/1225857/fertility-rate-in-africa](https://www.statista.com/statistics/1225857/fertility-rate-in-africa).


