# Project 1 (J.Mo Yang)

### Selected City: 
* #### Washington D.C
    * I have originally had 400 data points scrapped from Zillow using their URL. The data scrapped were then translated into a Pandas Dataframe in order for me to easily train the neural network model that was first introduced in the first week of class. However, there were 8 data points with missing information (a couple being a studio and others missing number of bath and bedrooms). Therefore, I have dropped the 8 data points, leaving us with a total of 392 data points with its price, number of beds, baths and the square footage of the house. 

* #### Possible False Information provided by Zillow (?)
    * Also, I have noticed that the data that were scrapped showed false information. For example, 1855 Calvert St NW APT 201, Washington, DC 20009 is a 2 bed, 1 bath 749 sqft apartment in D.C, however, according to the zillow_scrape.py script, the same apartment is listed as a 4 bed 7 bathroom with 6407 sqft. Therefore, before I moved on further into training my neural network, I checked on the website to make sure all data points are accurate. Weirdly, the prices of the data I have scraped were extremely accurate, but the number of baths, bedroom and the squarefootage of some data points were off by a mile. At first I thought that I have done something wrong in the script that it would scrape information of a different homes in D.C or the apartments have different units in which it has different layout. However, there were no patterns to the data points possibly shifting by one or multiple rows. Also, the apartment unit number is given, which means that the number of bed and bathrooms should associate with the given unit found on Zillow. 
  
  * The descriptoin of the data points are as shown below after it was screened. 
    * | Statistics | Price | # of Bed | # of Bath | Sqft |
      |------------|-------|----------|-----------|------|
      | Mean| $1,272,951 | 2.71 | 2.47 | 1,730.82|
      | Min | 25000 | 1 | 1 | 616 | 
      | 25% | 423,787.5 | 2 | 2 | 996 |
      | 50% | 619,900 | 2 | 2 | 1454 |
      | 75% | 894,000 | 3 | 3 | 1878 |
      | Max |  18,000,000 | 8 | 11 | 10823 | 

   * As you can see from the data table as well as Figure 1, the distribution of the data points are extremly wide. However, I did not remove the outliers as the Sqft of the houses in Washington D.C could possibly be less impacted due to their dense population. 



The Mean Squared Error is:  5590766503195.333 (Not scaled) 
The Mean Squared Error is:  5270751938437.771 (Scaled)



### Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features.
### Write a one and a half to two page report on your results and include the following.
### A description of the housing data you scraped from zillow


### A description of your model architecture
### An analysis of your model output



### An analysis of the output that assesses and ranks all homes from best to worst deal
### Include at least three plots that support your project report
### Stretch goal: add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?
