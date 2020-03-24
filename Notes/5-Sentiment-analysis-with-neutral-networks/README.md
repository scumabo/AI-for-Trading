# Introduction to Neural Networks
## **AND, OR, XOR** using neural networks

1. AND
![](2020-03-22-22-26-21.png)

2. OR
![](2020-03-22-22-27-54.png)

3. XOR
![](2020-03-22-22-28-41.png)
![](2020-03-22-22-30-35.png)

## Intuition: find the binary classification line.

Points correctly classified are good. Points are misclassified want the line to move closer to them. 

To move a line closer to a point, we just need to modify the line equation's coefficient by subtracting the points coordinates (with bias 1) (TODO: math?). We need to use a learning rate to control the speed of the line moving to the point.

![](2020-03-22-22-42-46.png)

Algorithm:

![](2020-03-22-23-34-34.png)

We need a continuous and differentiable error function in order to use gradient decent.

![](2020-03-23-09-41-29.png)

We use activation function to let each unit returns continuous probabilities:

![](2020-03-23-10-03-10.png)

### Softmax
Essentially, we want to convert the generated scores (z) to probability range in [0, 1]. Since the z could be negative, we need to apply exponential before normalization.

![](2020-03-23-10-13-50.png)

### One-hot Encoding
If we have multiple classes, we can not simply label then as 1, 2. 3, ... Because that will introduce dependencies, e.g, 1 is closer to 2 than 5. We can use one-hot encoding to generate independent labels.
![](2020-03-23-15-30-16.png)

## Maximum Likelihood
A good model should give higher probabilities to sampling events occurred. 

![](2020-03-23-16-33-41.png)

# Cross Entropy
Given a bunch of events and probabilities, cross entropy measures how likely the events happen based on the probabilities. If it is very likely, then we have a small cross entropy. Otherwise, we have a large cross entropy.

A good model has small cross entropy to sampling events.

![](2020-03-23-16-38-24.png)
![](2020-03-23-16-48-13.png)

## Logistic Regression (Binary Classification)
![](2020-03-23-16-56-18.png)

![](2020-03-23-17-10-56.png)

# Training Neutral Networks
Keep training the neutral network until testing error start increasing. 

![](2020-03-23-21-35-16.png)

## Regularization
![](2020-03-23-21-38-43.png)
![](2020-03-23-21-39-05.png)
![](2020-03-23-21-39-24.png)
![](2020-03-23-21-40-29.png)
![](2020-03-23-21-41-47.png)

![](2020-03-23-21-43-27.png)
![](2020-03-23-21-44-24.png)

## Vanishing Gradient
![](2020-03-23-21-45-14.png)
![](2020-03-23-21-45-52.png)
![](2020-03-23-21-46-09.png)

Batch vs Stochastic Gradient Descent

![](2020-03-23-21-49-23.png)
![](2020-03-23-21-50-43.png)
