# Project 2 (J.Mo Yang)

### Selected Country: Albania
* I have selected Albania as the country to analyze in this project. I did have thoughts on other countries, however rather recent, DHS VII data was available for Albania. Also, as a student who learned a lot about the Middle East and Muslim countries, even though Albania is in Europe, it was intriguing for me to look into this data set.
  * Locations are divided into prefectures in this data set. 

#### Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)? 
* Output Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? 

  <img src="best.png" width="750" height="405">
  * Model 1 to Model 3 has the largest AUC of 0.616


* Linear Regression Plot 

  <img src="lr_plot.png" width="550" height="500">



  
#### Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? Provide justification for your selected penalty value? 
* I sliced the model at 11 (Penalty value of 0.00108), since it was the best performing model out of 15 models that we produced in the beginning. Also, it seemed to have removed some irrelavent factors because this penalty has the highest AUC when I went through all possible values(1 to 15) for slicing. However, the difference was small. 


#### Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes.

<img src="lr_auc.png" width="550" height="500">
