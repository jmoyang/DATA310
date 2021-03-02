# Project 1 (J.Mo Yang)

### Selected City: 
* #### Washington D.C
    * I have originally had 400 data points scrapped from Zillow. However, there were 8 data points with missing information (a couple being a studio and others missing number of bath and bedrooms). Therefore, I have dropped the 8 data points, leaving us with a total of 392 data points with its price, number of beds, baths and the square footage of the house. The descriptoin of the data points are as shown below. 
    * | Statistics | Price | # of Bed | # of Bath | Sqft |
      |------------|-------|----------|-----------|------|
      | Mean| $1,272,951 | 2.71 | 2.47 | 1,730.82|
      | Min | 25000 | 1 | 1 | 616 | 
      | 25% | 423,787.5 | 2 | 2 | 996 |
      | 50% | 619,900 | 2 | 2 | 1454 |
      | 75% | 894,000 | 3 | 3 | 1878 |
      | Max |  18,000,000 | 8 | 11 | 10823 | 

### Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors.

### Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features.
### Write a one and a half to two page report on your results and include the following.
### A description of the housing data you scraped from zillow

print(homes.quantile(q=0.5))
prices     619,900.0
no_beds         2.0
baths           2.0
sqft         1454.0


print(homes.quantile(q=0.75))
prices     894,000
no_beds         3.0
baths           3.0
sqft         1878.5

print(homes.max())
prices                         18,000,000
address     Bock Rd Oxon Hill MD 20745 
no_beds                               8
baths                                11
sqft                              10823
dtype: object

### A description of your model architecture
### An analysis of your model output



### An analysis of the output that assesses and ranks all homes from best to worst deal
### Include at least three plots that support your project report
### Stretch goal: add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?
