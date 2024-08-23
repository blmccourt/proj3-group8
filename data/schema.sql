CREATE TABLE "country" (
"Country ID" TEXT,
  "Country ISO-3 Code" TEXT,
  "Country" TEXT
);
CREATE TABLE "indicator" (
"Indicator ID" TEXT,
  "Anthropometric Indicator" TEXT
);
CREATE TABLE "region" (
"Region ID" TEXT,
  "Region" TEXT
);
CREATE TABLE "dimension" (
"Dimension ID" TEXT,
  "Dimension" TEXT
);
CREATE TABLE "age" (
"Age ID" TEXT,
  "Dimension Value" TEXT
);
CREATE TABLE "sex" (
"Sex ID" TEXT,
  "Dimension Value" TEXT
);
CREATE TABLE "residence" (
"Residence ID" TEXT,
  "Dimension Value" TEXT
);
CREATE TABLE "economic_status" (
"Economic Status ID" TEXT,
  "Dimension Value" TEXT
);
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
CREATE TABLE "education" (
"Education ID" TEXT,
  "Dimension Value" TEXT
);
