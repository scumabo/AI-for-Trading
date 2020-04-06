# Decision Tree

![](images/2020-03-29-23-01-28.png)

## Entropy
![](images/2020-03-29-23-02-43.png)

Entropy measures number of possibilities to organize balls?

![](images/2020-03-29-23-03-53.png)

Entropy measures the knowledge of the color of the ball?

![](images/2020-03-29-23-07-52.png)

### Entropy Formula

Let's play a game. Pick 4 balls from the basket with replacement. Win the game if the colors of the 4 balls (order matters) matches the ones in the basket.

![](images/2020-03-29-23-11-11.png)

![](images/2020-03-29-23-11-24.png)

![](images/2020-03-29-23-12-57.png)

![](images/2020-03-29-23-14-28.png)

![](images/2020-03-29-23-15-14.png)

![](images/2020-03-29-23-17-39.png)

## Information Gain

![](images/2020-03-29-23-19-05.png)

![](images/2020-03-29-23-19-49.png)

![](images/2020-03-29-23-21-13.png)

![](images/2020-03-30-13-01-27.png)

# Model Testing and Evaluation
![](images/2020-03-30-14-07-40.png)
![](images/2020-03-30-14-08-26.png)
![](images/2020-03-30-14-11-37.png)
![](images/2020-03-30-14-12-06.png)
![](images/2020-03-30-14-13-13.png)
![](images/2020-03-30-14-13-54.png)

When accuracy doesn't work?
![](images/2020-03-30-14-17-01.png)

## False Positives and False Negatives

![](images/2020-03-30-14-20-27.png)
![](images/2020-03-30-14-20-46.png)

![](images/2020-03-30-14-22-57.png)

## Recall vs. Precision
![](images/2020-03-30-14-25-17.png)
![](images/2020-03-30-14-25-36.png)
![](images/2020-03-30-14-27-33.png)
![](images/2020-03-30-14-28-11.png)

## Types of Errors

![](images/2020-03-30-14-36-40.png)
![](images/2020-03-30-14-37-45.png)

## Model Complexity Graph
![](images/2020-03-30-14-41-43.png)
Mistake! Never use your training data for testing
![](images/2020-03-30-14-42-36.png)
![](images/2020-03-30-14-43-05.png)

### Solution: Cross Validation
![](images/2020-03-30-14-44-55.png)
![](images/2020-03-30-14-45-40.png)

## K-fold Cross Validation
Break data into K bucket. Train our model K times each time a a different bucket as testing data. Average the resulting K models.

## Cross Validation for Time-series 
![](images/2020-03-30-14-56-45.png)
![](images/2020-03-30-15-03-24.png)

## Learning Curves

![](images/2020-03-30-15-10-21.png)

# Random Forests (Ensembling)

![](images/2020-03-30-19-32-27.png)

![](images/2020-03-30-19-32-49.png)

![](images/2020-03-30-19-35-52.png)

![](images/2020-03-30-19-38-05.png)

![](images/2020-03-30-19-39-35.png)

![](images/2020-03-30-19-40-57.png)