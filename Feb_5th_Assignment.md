## Informal Response 1 (Feb.5th)

1) Difference between traditional programming and ML
* Traditional programming has rules and data that goes and the answers that comes out. On the other hand, in machine learning, we input answers and data for the machine to figure out the rules. Therefore, in machine learning programmers get a lot of data and establish a rule that will match one to the other. Neural networks deal in probability, give an likelihood of an answer being correct.  ML has parameters instead of hardcoded values, but it learns those parameters from the data over time. Therefore, it is a general function that learns how to behave. 

2) Prediction model for output value of 7 
* [21.997519]
* [21.999979]
   * The output for the both are similar but not the same. As the neural network 'learns' the rules of the data, the loss function decreases becuase it is simplying 'learning' to improve the results of the output (the more the neural network is run, the more accurate the output gets).

3) Housing Model 
* ~As the image shows (below), the worst buy is the 284 Church St, a 4 Bedroom, 3 Bathroom house priced at $399,000. The best buy is the 160 Holly Point Rd, a 3 Bedroom, 1 Bathroom house priced at $97,000. The model I have created finds the relationships between the number of bedrooms and the price of the houses, leading to finding a rule that determines the price of the house based on the number of bedrooms. However, this is not the most accurate model since there are other factors that contribute to the price of houses such as, the size (square feet), the number of bathrooms, the location of the house and the year it was built in.~
  * Updated:
    * | House Address                  | Bedroom | Bathroom | Squarefeet | Current Price | Model Predict |  Good or Bad Buy? (save) |
      |:-------------------------------|:-------:|:--------:|:----------:|:-------------:|:-------------:|:-----------------:|
      | 4403 New Point Comfort Hwy     |    3    |    2     |    2,840   |   $229,000    |  $282,000     |  Good (+$53,000)  |
      | 228 Church Street              |    4    |    3     |    3,680   |   $399,000    |  $372,600     |  Bad (-$26,400)   |
      | 160 Holly Point Road           |    3    |    1     |    1,238   |   $97,000     |  $160,000     |  Good (+$63,000)  |
      | 760 New Point Comfor Hwy       |    5    |    2     |    3,051   |   $347,500    |  $304,000     |  Bad (-$43,500)   |
      | 6138 E River Road              |    4    |    2     |    3,524   |   $289,000    |  $318,600     |  Good (+$29,600)  |
      | 984 Fitchetts Wharf Road       |    2    |    1     |    1,479   |   $250,000    |  $164,300     |  Bad (-$85,700)   |
      
      Based on the updated model, the worst buy is the 984 Fitchetts Wharf Road, with the current price being $85,700 over the predicted price. On the other hand, the best buy is 160 Holly Point Road, with the current price being $63,000 under the predicted price.  


[Code for Feb.5th Assignment (Updated with number of bathrooms and size)](Feb.5.Assignment.py)
  
