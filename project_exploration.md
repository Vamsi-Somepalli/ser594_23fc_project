#### SERX94: Exploratory Data Munging and Visualization
#### Crime Prediction: Weekly Incident Forecasting Using Machine Learning Approach (title)
#### Vamsi Krishna Somepalli (author)
#### 10/15/2023 (date)

## Basic Questions
**Dataset Author(s):** 
Chicago Police Department

**Dataset Construction Date:** 
Created Date	November 10, 2020;
As on 10/15/2023 Updated Date October 13, 2023;

**Dataset Record Count:** 1102909

Totla entries: seven million nine hundred fourteen thousand four hundred twenty-five (7914425)

The dataset was preprocessed to only include data from 2019 to present, as older data may not be useful for analyzing crime trends.

So the record count from 2019 to present are 1102909(one million one hundred two thousand nine hundred nine).


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

**Dataset File Hash(es):** (Data set may Update in a timely manner so the Hash might chnage while grader/reviewer run)
Dataset URL: https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD

Hash:dfdd6ca0ff0a10f1b794b0098417ce3e

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
The domain of crime analytics, specifically in the context of the city of Chicago, is crucial area of study that combines data science, criminology to understand, predict, and combat crime in an urban environment.Chicago, as one of the most populous cities in the United States, faces complex challenges related to crime and safety, so analysing  the crime in such cities helps in determining the trends/patterns in crimes and possible cause of crimes. Identifing the crime hotspots helps in urban planing and resource allocation and possible crime predection(future scope).

The paper "Specialized knowledge: Understanding crime analyst's roles and responsibilities and the impact of their work" by Emma Brown and Dale Ballucci (2022)[1] provides a comprehensive overview of the field of crime analysis and discussed challenges faced by crime analysts, such as the need to stay up-to-date on the latest crime prevention and intervention strategies.this paper helped me understanding of the field of crime analysis and the importance of crime analysts' work. 

Crime analytics begins with the collection of vast amounts of data related to criminal incidents.Researchers and policymakers have come to rely especially on an annual Uniform Crime Reporting publication[2] for understanding the previous year’s crime trends[3]. important thing in collectiung crime data is all the data might not be available all the times its important to clean the
data accordingly.

Analysis: 
In this project, we are conducting a comprehensive analysis of crime data in Chicago. focusing on how crime has changed over the years, understand arrest trends, and dig into the details of who, what, and where these incidents occur.
and presenting those findings using data analysis techniques and data visualizations.



1.Brown, E., & Ballucci, D. (2022). Specialized knowledge: Understanding crime analyst’s roles and responsibilities and the impact of their work. Criminology & Criminal Justice, 0(0). https://doi.org/10.1177/17488958221095980
2.“Crime in the U.S.” FBI, FBI, 15 July 2010, ucr.fbi.gov/crime-in-the-u.s/. 
3. Kim, Noah, and Ames Grawert. “Understanding the FBI’s 2021 Crime Data.” Brennan Center for Justice, 16 Oct. 2023, www.brennancenter.org/our-work/research-reports/understanding-fbis-2021-crime-data.  

## Data Transformation
### Transformation 1
**Description:** Data Filtering for years after 2019.

The crime data was filtered to only include data from 2019 to present, as older data may not be useful for analyzing crime trends.

**Soundness Justification:** 
Crime trends can change over time, and older data may not be representative of current trends. For example, the types of crimes that are most common, the locations where crimes occur, and the demographics of crime victims and perpetrators can all change over time. By focusing on recent crime data, we can get a more accurate picture of current crime trends and identify areas where crime prevention and intervention efforts are most needed.

### Transformation 2
**Description:** Updates missing location description rows as "Unknown"

This was done to minimize the loss of data, as the location description is not essential for all types of crime analysis

**Soundness Justification:** 
 Updating missing location description rows as "Unknown" allows us to include more data in our analysis, even if the data is not perfect. This is important because crime data is often incomplete, and having more data can lead to more accurate and informative results. ans also  it allows us to use the data to answer questions about crime trends and patterns, even if we do not have complete information about every crime.

### Transformation 3
**Description:** Removes rows with missing coordinates.

The exact location of a crime is essential for many types of crime analysis, such as identifying crime hotspots, tracking the movement of crime over time, and analyzing the spatial distribution of crime. Without coordinates, it is impossible to do any of these things.

**Soundness Justification:** 
if crimes in certain neighborhoods or communities are more likely to have missing coordinates, this could lead to a biased view of crime patterns in the city. By removing rows with missing coordinates, we can help to reduce the risk of bias in our analysis.
In addition, the fact that the missing coordinates are spread across all districts, community areas, and all years suggests that there is no systematic reason for the missing data. This makes it difficult to impute the missing values, and it also raises the possibility that the missing data is biased.

## Visualization
### Visual 1 : 
Distribution of Crime Types (Log Scale)
**Analysis:** 
This bar plot shows the distribution of different crime types on a logarithmic scale. As the difference between different crime types is huge so took log scale.

### Visual 2 : 
Crime Trends Over Time on a Weekly Basis
**Analysis:** 
The line plot of weekly crime trends provides insight into how the number of crimes changes over time. It might show weekly patterns, such as fluctuations in crime rates during weekends.

### Visual 3 : 
Crime Trends Over Time on a Monthly Basis
**Analysis:** 
Similar to the weekly plot, this monthly plot highlights the broader trends in crime rates over time. It can help identify long-term patterns, chnages in crime over months.

### Visual 4 : 
Arrest vs. Non-Arrest (Pie Chart)

**Analysis:** 
This pie chart illustrates the proportion of crimes that resulted in arrests versus those that did not.
i have implemented the same in bars aswell i liked the pie chart so including this aswell.

### Visual 5 : 
Arrest vs. Non-Arrest (Bar Chart)
**Analysis:** 
This is same as above but in bars. The blue and red bars represent non-arrested and arrested incidents, respectively.

### Visual 6 : 
Domestic vs. Non-Domestic Incidents (Pie Chart)
**Analysis:** 
This pie chart shows the distribution of domestic and non-domestic incidents. Pie charts helps to show how much percentage of crime are domestic/non-domestic so implemented pie rather than bars.

### Visual 7 : 
Histogram of Year
**Analysis:** 
The histogram of years provides an overview of the distribution of crimes across different years. It may reveal trends over the years, such as increasing or decreasing crime rates.

### Visual 8 : 
Scatter Plots of Quantitative Features
**Analysis:** 
These scatter plots visualize the relationships between pairs of quantitative features (e.g., 'Beat' vs. 'Ward'). They can help identify any correlations or patterns between these features.(there are six scatter plots)