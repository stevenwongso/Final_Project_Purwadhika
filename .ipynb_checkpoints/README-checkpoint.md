# Final Project
#### JCDS08 - Steven 
<hr>

## Project Description 
<hr>

This repository contain the final project as one of the requirements to fullfill in Purwadhika Job Connector - Data Science Program.

#### Introduction

A credit card is a payment card issued to users (cardholders) to enable the cardholder to pay a merchant for goods and services based on the cardholder's promise to the card issuer to pay them for the amounts plus the other agreed charge. Credit card offer the perks of being convenience, offer reward, and having purchasing power. Despite of that, credit card also have a lot of disadvantage one of them being expensive and risky. 

Credit card use has grown year after year since their invention as a payment option. According to a 2019 report, “The Consumer Credit Card Market,” from the Consumer Financial Protection Bureau. Purchase volume of credit card grew 30% from 2015 to 2018, while balances grew 20%, credit lines grew 17% and the number of consumers with accounts, grew 10%. In Indonesia, consumer credit also continues to increase. This can be seen in the graph below which correspond to growth of consumer credit from 2016 until 2020

<p style="text-align: center;"> <b> Indonesia Consumer Credit (IDR Billion) </b> </p>

<img src = 'ReadmeImage/indonesia-consumer-credit.png' width="600" height="400" />

Banking industries received so many applications for credit card request. With all the known negatives of accepting credit card issue, the constantly rising average credit card debt and credit card delinquency rates, it’s reasonable to be hesitant for banking industry to  accept a credit card request from the applicant. 

Going through each request manually can be very time consuming, also prone to human errors. However, if we can use the historical data to build a model which can shortlist the candidates for approval means we can solve this problem. 

Beside that, The Credit Card area of a large retail bank was unable to determine the effect of their marketing on customer behaviour in credit card usage and the resulting profitability. They were unaware of the effect of loyalty programs and product offerings on different customer groups and the bottom line. That's why this project also aim to  gain an understanding of the behaviour and profitability of clients in the
credit card portfolio by segmenting the credit card customer with the data that have been provided

Customer segmentation is one of the most fundamental building blocks in getting to know customers. It is essential for industries where customer interaction is frequent and varied, as each interaction provides insight into opportunities and risks for every individual. The credit card industry is on par with telecommunications, e-commerce, and retail from this perspective, and the industry gains significant ROI from segmentation initiatives

## Project Goals

<hr>

This project aims to :
    
    1. Predict the probability of credit card late payment
    2. Develop  customer segmentation, define customer behaviour for future marketing strategy
    
## Project Datasets

<hr>

   __1. Credit Card Overdue Prediction__
   
         - https://www.kaggle.com/rikdifos/credit-card-approval-prediction
         
   __2. Credit Card Customer Segmentation__
         
         - https://www.kaggle.com/arjunbhasin2013/ccdata
         
## Features
<hr>

In this Project, There are two main feature :

#### 1. Credit Card Overdue Prediction

Data Dictionary :

<img src = 'ModelImage/Credit Approval Explanation.JPG' width="800" height="800" />

<img src = 'ModelImage/Credit record explanation.JPG' width="800" height="200" />

Model ML: 

- Logistic Regression
- K-Nearest Neighbors
- DecisionTree
- Random Forest
- Gradient Boosting classifier



#### 2. Credit Card Customer Segmentation

Data Dictionary :

<img src = 'ModelImage/Credit Segmentation Explanation.JPG' width="800" height="600" />

Model ML :

- K-Means Clustering

## WEB
<hr>

This project used Flask to build the web application. Below are some screenshoot for the web when you run ```ccapp.py```

__1. Login - Sign Up Page :__

This project use MySQL as main RDBMS for login-signup

<br>
<img src = 'ReadmeImage/login.JPG' width="800" height="400" />

<br>
<img src = 'ReadmeImage/Sign Up.JPG' width="800" height="400" />

__2. Home Page :__

<br>
<img src = 'ReadmeImage/Home.JPG' width="800" height="400" />

__3. Credit Card Overdue Prediction :__

<br>
<img src = 'ReadmeImage/Overdue.JPG' width="800" height="400" />

__4. Credit Card Customer Segmentation :__

<br>
<img src = 'ReadmeImage/Segmentation.JPG' width="800" height="400" />

__5. Data Visualization :__

<br>
<img src = 'ReadmeImage/DataViz.JPG' width="800" height="400" />

## Result
<hr>

Some Example of the result page that shown on the web

<br>
<img src = 'ReadmeImage/Result Overdue Prediction.JPG' width="800" height="400" />

<br>
<img src = 'ReadmeImage/Result Segmentation.JPG' width="800" height="400" />