#### SERX94: Exploratory Data Munging and Visualization
#### Crime Analytics: City of Chicago (title)
#### Vamsi Krishna Somepalli (author)
#### 10/15/2023 (date)

## Basic Questions
**Dataset Author(s):** 
Chicago Police Department

**Dataset Construction Date:** 
Created Date	November 10, 2020;
As on 10/15/2023 Updated Date October 13, 2023;

**Dataset Record Count:** 1119596
Totla entries: Seven million nine hundred eleven thousand five hundred ninety-eight (7911598)

The dataset was preprocessed to only include data from 2019 to present, as older data may not be useful for analyzing crime trends.

So the record count from 2019 to present are 1119596.


**Dataset Field Meanings:** 

ID: An identifier or unique reference number for each recorded incident.

Case Number: A unique case number associated with each incident. This number is used for tracking and reference purposes.

Date: The date and time when the incident occurred.

Block: The block or specific location where the incident took place, usually denoted by a street address or block number.

IUCR: The Illinois Uniform Crime Reporting (IUCR) code, which is a standardized code used to classify and categorize different types of criminal offenses.

Primary Type: The primary classification of the crime or offense, which describes the nature of the incident (e.g., theft, assault, sexual assault, etc.).

Description: A more detailed description of the incident, providing additional information about the specific circumstances or details of the offense.

Location Description: A description of the location where the incident occurred (e.g., street, apartment, garage, etc.).

Arrest: A binary value indicating whether an arrest was made in connection with the incident. "True" indicates that an arrest was made, while "False" indicates that no arrest was made.

Domestic: A binary value indicating whether the incident is considered a domestic incident. "True" indicates that it is domestic, while "False" indicates that it is not.

Beat: A code or identifier for the specific geographical area or "beat" that is covered by a police officer or unit.

District: The police district associated with the incident's location.

Ward: The ward in which the incident occurred. Wards are geographical divisions within a city or municipality, often used for administrative purposes.

Community Area: The specific community area within the city where the incident took place. Community areas are neighborhood or administrative divisions within a city.

FBI Code: A code used to classify and categorize different types of criminal offenses, often based on the Federal Bureau of Investigation's classification system.

X Coordinate: The horizontal spatial coordinate (longitude) of the incident's location.

Y Coordinate: The vertical spatial coordinate (latitude) of the incident's location.

Year: The year in which the incident occurred.

Updated On: The date and time when the data entry or record was last updated.

Latitude: The geographical latitude of the incident's location, typically represented in degrees.

Longitude: The geographical longitude of the incident's location, typically represented in degrees.

Location: A combined field that provides the geographical coordinates (latitude and longitude) in a single format.

**Dataset File Hash(es):** 
0d3f739d78494e6ca14955cd7e35b77e

## Interpretable Records

### Record 1
**Raw Data:** 
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location
13210088,JG423627,2023-08-31 12:00:00,023XX W JACKSON BLVD,1153,DECEPTIVE PRACTICE,FINANCIAL IDENTITY THEFT OVER $ 300,STREET,False,False,1225,12.0,27.0,28.0,11,1160870.0,1898642.0,2023,09/16/2023 03:41:56 PM,41.877565108,-87.68479102,"(41.877565108, -87.68479102)"

**Interpretation:** 
This row of data represents a specific incident that occurred on August 31, 2023, at 12:00 PM at the location "023XX W JACKSON BLVD" 
The incident is classified as a "DECEPTIVE PRACTICE" with a description of "FINANCIAL IDENTITY THEFT OVER $300." It happened on a "STREET" 
There was no arrest made, and it was not a domestic incident. This incident falls within Beat 1225, District 12, Ward 27, and Community Area 28. 
The FBI Code for this incident is 11. The geographical coordinates of the incident are approximately (41.87756511, -87.68479102)
The data entry indicates that the incident occurred in the year 2023, and the last update to this record was on September 16, 2023, at 15:41.Further more case ID and Case number for this incident are 13210088 JG423627 respectively.

Reasonableness:
The data is reasonable. It provides detailed information about a specific non-violent criminal incident, indicating the location, type of crime, and relevant law enforcement details. The data also includes geographical coordinates for precise location identification.

### Record 2
**Raw Data:** 
ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location
13210004,JG422532,2023-07-24 21:45:00,073XX S JEFFERY BLVD,0281,CRIMINAL SEXUAL ASSAULT,NON-AGGRAVATED,APARTMENT,False,False,333,3.0,7.0,43.0,02,1190812.0,1856743.0,2023,09/16/2023 03:41:56 PM,41.7619185,-87.576209245,"(41.7619185, -87.576209245)"

**Interpretation:** 
This row represents another incident that occurred on July 24, 2023, at 21:45 at the location "073XX S JEFFERY BLVD" 
The incident is classified as "CRIMINAL SEXUAL ASSAULT" with a description of "NON-AGGRAVATED" It happened in an "APARTMENT" There was no arrest made, 
and it was not a domestic incident. This incident falls within Beat 333, District 3, Ward 7, and Community Area 43. The FBI Code for this incident is 2. 
The geographical coordinates of the incident are (41.7619185, -87.57620925). The data entry indicates that the incident occurred in the year 2023, 
the last update to this record was on September 16, 2023, at 15:41 and case ID is 13210004 with case number JG422532.

Reasonableness:
The data providing information about a specific criminal incident of a sensitive nature. It includes the location, type of crime, and relevant law enforcement details, such as beat, district, and geographical coordinates, which are crucial for law enforcement and analysis.

## Background Domain Knowledge
TODO

## Data Transformation
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)