# Project 1 (J.Mo Yang)

### Selected City: 
* #### Washington D.C
    * I have originally had 400 data points scrapped from Zillow using their URL. The data scrapped were then translated into a Pandas Dataframe in order for me to easily train the neural network model that was first introduced in the first week of class. However, there were 8 data points with missing information (a couple being studios, empty lots/land and others missing number of bath and bedrooms). Therefore, I have dropped the 15 data points, leaving us with a total of 385 data points with its price, number of beds, baths and the square footage of the house. 

* #### Possible False Information Provided By Zillow (?)
    * Also, I have noticed that the data that were scrapped showed false information. For example, 1855 Calvert St NW APT 201, Washington, DC 20009 is a 2 bed, 1 bath 749 sqft apartment in D.C, however, according to the zillow_scrape.py script, the same apartment is listed as a 4 bed 7 bathroom with 6407 sqft. Therefore, before I moved on further into training my neural network, I checked on the website to make sure all data points are accurate. Weirdly, the prices of the data I have scraped were extremely accurate, matching almost all addresses but the number of baths, bedroom and the squarefootage of some data points were off by a mile. At first I thought that I have done something wrong in the script that it would scrape information of a different homes in D.C or the apartments have different units in which it has different layout. However, there were no patterns to the data points possibly shifting by one or multiple rows. Also, the apartment unit number is given, which means that the number of bed and bathrooms should associate with the given unit found on Zillow. 
         * Data seemed odd --> Checked on Zillow, found out that address and prices match the data scrapped, but number of bath/beds and square footage were extremly off by random numbers.
            * Another example:  1111 Oates St NE Washington DC 20002 listed as $850,000 with 4 bed, 4 bathroom, 1700 sqft home, zillow_scrape.py shows as 1 bed, 1 bath, 616 squarefoot with the same address and price

  * The descriptoin of the data points are as shown below after it was screened. 
    * | Statistics | Price | # of Bed | # of Bath | Sqft |
      |------------|-------|----------|-----------|------|
      | Mean| $1,291,785 | 2.94 | 2.78 | 1,977.5 |
      | Min | $95,009 | 1 | 1 |  331 | 
      | 25% | $428,749.75 | 2 | 2 | 956 |
      | 50% |  $631,950 | 3 | 2 | 1344.5 |
      | 75% | $899,900 | 3.25 | 3 | 1984 |
      | Max |  $18,000,000 | 11 | 17 | 13687 | 

   * As you can see from the data table as well as Figure 1, the distribution of the data points are extremly wide. However, I did not remove the outliers as the Sqft of the houses in Washington D.C could possibly be less impacted due to their dense population. 



The Mean Squared Error is:  5590766503195.333 (Not scaled) 
The Mean Squared Error is:  5270751938437.771 (Scaled)


### A description of your model architecture
* I have created a simple model based on the model we have gone over in class, using TensorFlow package. It uses number of bed rooms, bathrooms and square footage to train the model (3 layers of input). Which then, "learns" with the input datas to produce the optimal prices based on the number of beds, bathrooms and square foot. Then the predicted prices are inputted into a column called 'predict'. Then I calculated the price difference between the observed value from Zillow and the predicted value. Lastly, I created a new column called 'Deal' to distinguish whether or not the observed value is a 'Good Deal' or a 'Bad Deal'. There are 271 houses that were labeled as a "Good Deal" compared to the 114 houses that were labeld as a "Bad Deal"
   ![image](https://user-images.githubusercontent.com/78192904/109760817-5cbf2c00-7bbd-11eb-969e-5199e2c88d98.png)

 
### An analysis of your model output



### An analysis of the output that assesses and ranks all homes from best to worst deal
### Include at least three plots that support your project report
### Stretch goal: add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?
