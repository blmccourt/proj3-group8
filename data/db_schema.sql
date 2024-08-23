/***********************************************************************************************
* Note:  
* The clean_data table was generated from the cleaned_df.  This dataframe was the result of
* cleaning the already agreggated raw_data source file.  The remaining tables were generated
* by disaggregating the cleaned_df dataframe in an effort to normalize the data for future use.
* As such, there are no current foreign keys between the tables.
************************************************************************************************/

CREATE TABLE "clean_data" (
"Region" TEXT,
  "Country ISO-3 Code" TEXT,
  "Country" TEXT,
  "Year" INTEGER,
  "Dimension" TEXT,
  "Dimension Value" TEXT,
  "Dimension Value Order" INTEGER,
  "Anthropometric Indicator" TEXT,
  "Prevalence Estimate %" REAL,
  "Weighted Sample Size" REAL,
  "Country Avg" REAL
);
CREATE TABLE country (
            CountryID TEXT PRIMARY KEY,
            Country_ISO_3_Code TEXT,
            Country TEXT
        );
CREATE TABLE indicator (
            IndicatorID TEXT PRIMARY KEY,
            AnthropometricIndicator TEXT
        );
CREATE TABLE region (
            RegionID TEXT PRIMARY KEY,
            Region TEXT
        );
CREATE TABLE dimension (
            DimensionID TEXT PRIMARY KEY,
            Dimension TEXT
        );
CREATE TABLE age (
            AgeID TEXT PRIMARY KEY,
            DimensionValue TEXT
        );
CREATE TABLE sex (
            SexID TEXT PRIMARY KEY,
            DimensionValue TEXT
        );
CREATE TABLE residence (
            ResidenceID TEXT PRIMARY KEY,
            DimensionValue TEXT
        );
CREATE TABLE education (
            EducationID TEXT PRIMARY KEY,
            DimensionValue TEXT
        );
CREATE TABLE economic_status (
            EconomicStatusID TEXT PRIMARY KEY,
            DimensionValue TEXT
        );
