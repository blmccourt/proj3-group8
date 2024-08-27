# Global Malnutrition Estimates in Children Under 5 Years of Age

## Group presentation

[Global Malnutrition Analysis Presentation](https://docs.google.com/presentation/d/1vJtmyZMTajHY_IHafsaot_RL99pl2x4QcZPWVB5AQaY/edit?usp=sharing)

## Overview of the project and its purpose

Analyzing and visualizing global malnutrition data for children under five, with a focus on providing actionable insights to potential donors into inequality factors where resources can be focused.
Analyzing and visualizing global malnutrition data for children under five enhances fundraising efficiency and donor engagement by targeting resources effectively, increasing transparency, and communicating the urgency of the issue. This approach allows organizations to make informed decisions, build trust with donors, and optimize their impact on combating malnutrition.

## Instructions on how to use and interact with the project

### ETL
The entirety of the ETL workflow was done in the [`ETL.ipynb`](https://github.com/blmccourt/proj3-group8/blob/main/ETL.ipynb) notebook.

### Data Visualizations

1. 

2. After cloning the repository to your local machine, `index.html` can be opened in your web browser of choice and will render the Leaflet map. The GeoJSON data established in `assemble_geojson.ipynb` is hard-coded into `define_raw_geojson_data.js`, so running the Python notebook isn't necessary to see the web visual.

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

### Data Visualizations

1.

2. **Web Visualization**

- **[`assemble_geojson.ipynb`](https://github.com/blmccourt/proj3-group8/blob/main/assemble_geojson.ipynb)**

  - Jupyter notebook with scripts for retrieving geographic coordinates for countries studied, and establishing GeoJSON data for use in web visualization

- **[`index.html`](https://github.com/blmccourt/proj3-group8/blob/main/index.html)**

  - Web page with a Leaflet visualization which superimposes a user-selected anthropometric factor onto a map for spatial demonstration of malnutrition indicators. Refers to `define_raw_geojson_data.js` and `render_heatmap.js`

- **[`/static/js/define_raw_geojson_data.js`](https://github.com/blmccourt/proj3-group8/blob/main/static/js/define_raw_geojson_data.js)**

  - JavaScript file with static variable definitions, each containing the raw GeoJSON data established in `assemble_geojson.ipynb`

- **[`/static/js/render_heatmap.js`](https://github.com/blmccourt/proj3-group8/blob/main/static/js/render_heatmap.js)**

  - JavaScript file with main rendering logic, using Leaflet. Interactivity is added by establishing an event listener function that re-renders using data established in `define_raw_geojson_data.js` as a superimposed Leaflet layer
