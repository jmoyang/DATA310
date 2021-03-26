# Project 2 (J.Mo Yang)

### Selected Country: Albania
* I have selected Albania as the country to analyze in this project. I did have thoughts on other countries, however rather recent, DHS VII data was available for Albania. Also, as a student who learned a lot about the Middle East and Muslim countries, even though Albania is in Europe, it was intriguing for me to look into this data set.
  * Locations are divided into prefectures in this data set. 

#### Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)? 
* ##### Output 

  <img src="best.png" width="550" height="205">
  
  * Model 1 (penalty of 0.0001) to Model 12 (penalty of 0.00137) had the largest Mean AUC value of 0.620. As you can see from the graph, even though it is very slight, the graph begins to gradually decrease from the 12th point, then showing a sharp decrease starting from Model 26 (penalty of	0.0239). 


* ##### Linear Regression Plot 

  <img src="lr_plot.png" width="450" height="400">



  
#### Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors? Provide justification for your selected penalty value? 
* I sliced the model at 12 or (penalty of 0.00137), because it is the last model to have an AUC of 0.620. However, major fall off of AUC value does not happen until the 26th model. Nevertheless, the gradual decrease in AUC from model 1 to model 24 is great. (0.6203214 compared to 0.6043768). Therefore, I decided to pick the model where the value of the thousandth changes first. I beleieve this 12th model point is where irrelevent predictors are removed, becauase the AUC value begins to decrease.


#### Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes.
* ##### Top Model ROC Plot (Model 12)
<img src="lr_auc.png" width="450" height="400">

* ##### Where AUC Falls off ROC Plot (Model 26)
<img src="26.png" width="450" height="400">

* As we can see, the model does a good job of predicting Wealth Level 5, does a decent, but not great job of predicting Wealth Level 1 and 4. Also, it does a bad job of predicting Wealth Level 2 and 3. Also, as we can see, the Model 26 does not perform very well compared to Model 12. 

#### Set up your random forest model and produce the AUC - ROC values for the randomly selected predictors, and the minimal node size, again with wealth as the target. How did your random forest model fare when compared to the penalized logistic regression? Provide your ROC plots and interpret them. 
* AUC - ROC values of Randomly Selected Predictors & the Minimal Node Sizes
<img src="rf_res.png" width="450" height="400">

* ##### Comparison Between Random Forest and Penalized Logistic Regression
<img src="rf_lr_auc.png" width="450" height="400">

* ##### AUC Plot
<img src="last_rf_fit_auc.png" width="450" height="400">

* As we can see from the graph above the penalized logistic regression performed similarly to the random forest model. Even the AUC plot shows a similar trend as the penalized logistic regression model. Just like the penalized logistics regression, the random forest model had difficulty predicting Wealth Level 2 and 3, doing a mediocre job on predicting 1 and 4. Finally, it did a great job of predicting 5. Therefore, there aren't much change/difference between the two models' performance. 

#### Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?
* ##### Output
<img src="last_rf_fit.png" width="450" height="400">

* It is apparent that the most important feature that contributes towards the predictive power of the random forest model is age, then followed by education, size and gender. If we think that the data points are from real-life survey filled out by real life people, the importance of the features above are not suprising. With higher age, there are higher chances that people are employed, but with diminishing return. Also, education will be another huge factor, because higher education jobs pay more compared to low educaiton jobs. Therefore, the results are not very surprising. 

#### Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target.  Again produce your ROC curves and interpret the results.
* ##### Table of Outcomes 

| Wealth | Accuracy | Average_loss | Loss | AUC |
|-------|----------|--------------|------|--------|
| 1 | 0.722621 |	0.5534895 | 0.5525514 | 0.655612 |
| 2 | 0.760311   | 0.5471703  | 0.5466003 | 0.559349 |
| 3 | 0.799777 | 0.4993141 | 0.4986266 | 0.545490 |
| 4 | 0.827471  | 0.4476862  | 0.4469511 | 0.623520 |
| 5 | 0.884265 |  0.3308910  | 0.3307253 | 0.702393 | 

* ##### Group 1 (Predicted Probablities and ROC Curve)
<img src="Images/linest_pp_1.png" width="350" height="300">                         <img src="Images/linest_1.png" width="350" height="300">

* ##### Group 2 
<img src="Images/linest_pp_2.png" width="350" height="300">                      <img src="Images/linest_2.png" width="350" height="300">

* ##### Group 3 
<img src="Images/linest_pp_3.png" width="350" height="300">                      <img src="Images/linest_3.png" width="350" height="300">

* ##### Group 4
<img src="Images/linest_pp_4.png" width="350" height="300">                      <img src="Images/linest_4.png" width="350" height="300">

* ##### Group 5
<img src="Images/linest_pp_5.png" width="350" height="300">                      <img src="Images/linest_5.png" width="350" height="300">

* Interestingly, we can see a similar results here. The model does a terrible job of predicting Wealth Groups 2 and 3, and it predicted Group 1 and 4 relatively okay compared to 2 and 3. Lastly, it did a great job of predicting Group 5. Therefore, the ROC curves for the logistic regression model seem to have a similar performance compared to random forest model and the penalized linear regression model. 

#### Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. Provide evaluative metrics including a measure of accuracy and AUC. Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results.
* ##### Table of Outcomes 
| Wealth | Accuracy | Average_loss | Loss | AUC |
|-------|----------|--------------|------|--------|
| 1 |  0.726620 |	0.550428 | 0.550428|  0.661826 |
| 2 | 0.758904  |0.544950  |  0.544950 |  0.576311 |
| 3 | 0.798445| 0.500164 | 0.500164 | 0.542598 |
| 4 | 0.835024  | 0.432673  | 0.432673 |  0.632628 |
| 5 |  0.887449 | 0.323096  | 0.323096 | 0.707655 |

* ##### Group 1 (Predicted Probablities and ROC Curve)
<img src="Images/boost_pp_1.png" width="350" height="300">                         <img src="Images/boost_1.png" width="350" height="300">

* ##### Group 2 
<img src="Images/boost_pp_2.png" width="350" height="300">                         <img src="Images/boost_2.png" width="350" height="300">

* ##### Group 3 
<img src="Images/boost_pp_3.png" width="350" height="300">                         <img src="Images/boost_3.png" width="350" height="300">

* ##### Group 4
<img src="Images/boost_pp_4.png" width="350" height="300">                         <img src="Images/boost_4.png" width="350" height="300">

* ##### Group 5
<img src="Images/boost_pp_5.png" width="350" height="300">                         <img src="Images/boost_5.png" width="350" height="300">

* It seems like boosted model is not much different from the rest of the models. The AUC did improve a little bit compared to linear regression model above interms of predicting Wealth group 2. However, most results show a similar trend with each other. The models did not do a great job predicting group 2 and 3 and did extremly well with group 5. 

#### Analyze all four models. According to the evaluation metrics, which model produced the best results? 
* The boosed model produced the best result out of the 4 models that we have created in this project. From model to model (penalized linear to boosted), the results showed gradual improvement. However, the improvements aren't drastic to a point where we can tell the difference with our naked eye, through the ROC curve. Nevertheless, the AUC values show us that boosted model did have the highest AUC (average of 0.624), which is not too far from orginial penalized linear regression. 

#### Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?
<img src="Images/dis.png" width="350" height="300">

* Huge discrepancy between Wealth group 1 and 5. Wealth group 1 nearly double the count compared to group 5. 
