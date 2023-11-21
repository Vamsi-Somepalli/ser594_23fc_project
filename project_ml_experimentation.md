#### SERX94: Experimentation
#### Crime Prediction: Weekly Incident Forecasting Using Machine Learning Approach (title)
#### Vamsi Krishna Somepalli (author)
#### 11/20/2023 (date)


## Explainable Records
### Record 1
**Raw Data:** 
2019,13,1211,12.0

This records represents in year 2019 in week 13 number of crimes or incidents recorded in area with beat code 1211 in district 12

**Prediction Explanation:** Model predicts 10 incidents that align with historical data showing a relatively lower crime rate during Week 13 in Beat 1211 of District 12.0 in the year 2019. This make scence because this incidents are only recorded in that particular area and this low crime rate might be factors like the day of the week, local events, or law enforcement measures may contribute to this lower predicted count.

### Record 2
**Raw Data:** 2020,44,512,5.0

This records represents in year 2020 in week 44 number of crimes or incidents recorded in area with beat code 512 in district 5

**Prediction Explanation:** The model predicts 19 incidents in that week, this might be reasonable if there are patterns in the historical data indicating an increased likelihood of crime during Week 44 in Beat 512 of District 5.0 in the year 2020. Changes in economic conditions, population density, or external events could influence crime rates during this period.

## Interesting Features
### Feature A
**Feature:** District
District:The police district in which the crime takes place.

**Justification:** Police districts often changes in terms of size, population density, and socioeconomic conditions. Districts with higher population density or lower socio-economic status may experience different crime dynamics than less populated districts. Policing strategies, and local conditions within districts can significantly impact crime rates.

### Feature B
**Feature:** Year
Year: The calendar year in which the crime occurs.

**Justification:** Year is an important feature because crime patterns can change over time due to various factors like economic conditions, social policies, law enforcement strategies, and community development. By looking at different years, we can see how crime patterns might be different based on what's happening in the world.

## Experiments 
### Varying A (District)
**Prediction Trend Seen:** : Changing the police district (Feature A) while keeping everything else the same makes the model predict different levels of crime. Some areas may have more predicted incidents than others. it might increse or decrease based on the change of district.

### Varying B (Year)
**Prediction Trend Seen:** When we look at different years (Feature B) while keeping the police district and other features constant, the model predicts different amounts of crime. It shows how crime patterns might change over time.

### Varying A and B together
**Prediction Trend Seen:** By changing both the police district and the year at the same time, the model predicts a combined effect. It considers how both where you are and what year it is might impact the number of predicted incidents.


### Varying A and B inversely
**Prediction Trend Seen:** When we change the police district and the year in opposite ways, the model shows how these factors work together. It predicts how crime might go up or down based on both where you are and what year it is, even when these changes go in opposite directions.

