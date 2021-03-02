# Project 1

### Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location.

### Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors.

### Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features.
### Write a one and a half to two page report on your results and include the following.
### A description of the housing data you scraped from zillow
print(homes.mean())
prices     1,272,951
no_beds    2.713555
baths      2.475703
sqft       1,730.826

print(homes.std())
prices     2,341,841
no_beds    1.272911
baths      1.624744e+00
sqft       1,623.837

print(homes.min())
prices                                           800
address     1 Scott Cir NW #601 Washington DC 20036 
no_beds                                            1
baths                                              1
sqft                                             616

print(homes.quantile(q=0.25))
prices     423,787.5
no_beds         2.0
baths           2.0
sqft          996.0

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
