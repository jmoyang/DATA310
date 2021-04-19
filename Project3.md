# Project 3 (April 18th) 

## Country: Albania 

### About the Data 
* This project holds raster data sets and a single shape file from GDAM and Worldpop. I am continuing this project with the country of my choice from DHS project (Project 2). 
Albania beign a small country, I decided to run LR model and RF model on the whole entire country. The country of Albania is divided into 12 different counties and 375 units of local governance.

### Linear Regression Model 
* Using the 2015 population data for Albania, I utilitzed the linear regression model that we went over in classs. 
By splitting the data into training and testing data set with the proportion of 4/5, the model was able to predict the following number of population in Albania. 
  * <img src="Images/LR_ouptut.png" width="250" height="70">  
* As we can see from the results above, the actual total population within this model of Albania is 2,762,201 and the predicted population is 2,764,784. 
* Predicted Total Sums 
   
   <img src="Images/predicted_total_sums(LR).png" width="300" height="300">                            <img src="Images/alb_density.png" width="150" height="250">  
   
* As we can see the result from above, the predicted total sums of the population is very much similar to the actual population density map of Albania. Most of the population are concentrated in the mid-coast, land area of Albania.  

#### Results 
* ##### Population Sum
<img src="Images/pop_sums.png.png" width="300" height="300"> 

* ##### Population Difference Between Worldpop and Predicted value
<img src="Images/diff_sums(alb).png" width="300" height="300"> 

   * As we can see from the results above, the population difference shows that the majority of the area in Albania were on point with the actual population data from Worldpop (colored in greenish-yellow color). The model did have a couple of under and over predictions, represented by the color green and redish pink colors respectively. The areas of the under and over predictions are in the areas that is in the middle of Albania and is represented, where it is presented by green in population sum plot. Nevertheless, the overall model was great at predicting the population of Albania, as it is shown above (total actual population of 2,762,201 and predicted population of 2,764,784). 

### Random Forest Model

<img src="Images/LR_ouptut.png" width="250" height="70">

* As we can see from above, that the random forest model also did a good job of predicting the population of Albania. As we can see from the image above, the model predicted 2,764,702, where as the acutal total population is 2,762,201. 

* ##### Population Sum
<img src="Images/rf.png" width="300" height="300"> 

* ##### Population Difference Between Worldpop and Predicted value
<img src="Images/random.png" width="300" height="300"> 



