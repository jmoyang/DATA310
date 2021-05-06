# Plans for the Final Project 

## Problem Statement 
* Sneaker industry is a major industry of investment. According to Cowen, an investment firm, the sneaker resell market is projected to grow up to be an $30 Billion industry by 2030. Sneakers are growing more popularity as they become an important part of the pop culture worldwide. With the rising popularity pushing consumers into the sneaker market, popular manufacturers such as Nike and Adidas keep a super tight control over its distribution through their apps (SNKRS and Adidas app) and their official retailers. However, with the rising need or the demand for these limited supply sneakers pushes consumers to the resell market, increasing the need for a resell market. Over the years, we have been seeing a huge rise in the resell market. Now there are companies like StockX and Goat, that specifically deals with sneaker and clothing resell. StockX generated up to $400 Million in revenue in 2020, despite the COVID-19 Pandemic. Nevertheless, there is a single question that I had, what makes the resell prices the resell prices? In other words, what variables have an impact on resell prices? Is it the color of the shoes? Size of the shoes? or is it the popularity of the shoes? 
  * It is kind of obvious that popular shoes should be more expensive in the resell market, but I will be defining "popular" with the shoes' transaction on StockX.
    * Specific sneakers' transaction compared to the overall transaction. 

## The Data
* The data I will be using is from Kaggle, but it was originally from the StockX Data Contest in 2019. It holds about 10,000 random sample data points of all OFF-White x Nike and Yeezy 350 sales between 9/1/2017 to 2/12/2019. There are 99,956 total sales in the data set, with 27,794 of them being Off-White sales and the rest of them being Yeezy sales (72,162). This data set consists of U.S sales only. However, in order to depict the accuracy of the model, to see which features had the most impact on the prediction prices, I will be focusing on the 72,162 transaction of Adidas Yeezy Boost 350 sneakers. Much of the information needed for the model is provided by the data set. 
  * The popularity and raity of Off-White and Adidas Yeezy Boost 350 sneakers vary. 
    * [Source](https://www.kaggle.com/hudsonstuck/stockx-data-contest)  

## Method 
* I will be extracting the Adidas Yeezy Boost data points only from the data set and of course clean the data to be ready for the model. Then, I will be using linear regression machine learning method to depict the impact of each features (size, color, popularity). I am currently in the works of building a model. However, I am building off from the model created by [Sergio Pessoa](https://www.kaggle.com/sslp23/analyzing-yeezy-s-market), which is simple and easy to interpret. I will be having a few different models with different features (size, color, popularity) as a variable rather than focusing on the shoe size like Pessoa has done in his model in order to see which is a defining feature and of course to create the best predicting model. 
  * I will definately create a model with all features as I believe that all three features of the sneakers have an impact on the resell prices. 

## Preliminary Model Performance
