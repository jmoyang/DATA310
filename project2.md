# Project 2 (J.Mo Yang)

### Selected Country: Albania
* I have selected Albania as the country to analyze in this project. I did have thoughts on other countries, however rather recent, DHS VII data was available for Albania. Also, as a student who learned a lot about the Middle East and Muslim countries, even though Albania is in Europe, it was intriguing for me to look into this data set.
  * Locations are divided into prefectures in this data set. 

#### Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)? 
* Output Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? 

  <img src="best.png" width="750" height="405">
  
  * Model 1 (penalty of 0.0001) to Model 12 (penalty of 0.00137) had the largest Mean AUC value of 0.620, and as you can see from the graph, even though it is very slight, the graph begins to fall off from the 12th point. I beleieve this 12th model point is where irrelevent predictors are removed, becauase the AUC value begins to decrease.


* Linear Regression Plot 

  <img src="lr_plot.png" width="550" height="500">



  
#### Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? Provide justification for your selected penalty value? 
* I sliced the model at 12 or (penalty of 0.00137), because it is the last model to have an AUC of 0.620. However, major fall off of AUC value does not happen until the 24th model. Nevertheless, the gradual decrease in AUC from model 1 to model 24 is great. (0.6203214 compared to 0.6043768). Therefore, I decided to pick the model where the value of the thousandth changes first. 


#### Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes.

<img src="lr_auc.png" width="550" height="500">

* As you can see, the model 
