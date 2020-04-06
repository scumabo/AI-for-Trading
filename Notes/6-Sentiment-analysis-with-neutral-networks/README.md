# Introduction to Neural Networks
## **AND, OR, XOR** using neural networks

1. AND
![](images/2020-03-22-22-26-21.png)

2. OR
![](images/2020-03-22-22-27-54.png)

3. XOR
![](images/2020-03-22-22-28-41.png)
![](images/2020-03-22-22-30-35.png)

## Intuition: find the binary classification line.

Points correctly classified are good. Points are misclassified want the line to move closer to them. 

To move a line closer to a point, we just need to modify the line equation's coefficient by subtracting the points coordinates (with bias 1) (TODO: math?). We need to use a learning rate to control the speed of the line moving to the point.

![](images/2020-03-22-22-42-46.png)

Algorithm:

![](images/2020-03-22-23-34-34.png)

We need a continuous and differentiable error function in order to use gradient decent.

![](images/2020-03-23-09-41-29.png)

We use activation function to let each unit returns continuous probabilities:

![](images/2020-03-23-10-03-10.png)

### Softmax
Essentially, we want to convert the generated scores (z) to probability range in [0, 1]. Since the z could be negative, we need to apply exponential before normalization.

![](images/2020-03-23-10-13-50.png)

### One-hot Encoding
If we have multiple classes, we can not simply label then as 1, 2. 3, ... Because that will introduce dependencies, e.g, 1 is closer to 2 than 5. We can use one-hot encoding to generate independent labels.
![](images/2020-03-23-15-30-16.png)

## Maximum Likelihood
A good model should give higher probabilities to sampling events occurred. 

![](images/2020-03-23-16-33-41.png)

# Cross Entropy
Given a bunch of events and probabilities, cross entropy measures how likely the events happen based on the probabilities. If it is very likely, then we have a small cross entropy. Otherwise, we have a large cross entropy.

A good model has small cross entropy to sampling events.

![](images/2020-03-23-16-38-24.png)
![](images/2020-03-23-16-48-13.png)

## Logistic Regression (Binary Classification)
![](images/2020-03-23-16-56-18.png)

![](images/2020-03-23-17-10-56.png)

# Training Neutral Networks
Keep training the neutral network until testing error start increasing. 

![](images/2020-03-23-21-35-16.png)

## Regularization
![](images/2020-03-23-21-38-43.png)
![](images/2020-03-23-21-39-05.png)
![](images/2020-03-23-21-39-24.png)
![](images/2020-03-23-21-40-29.png)
![](images/2020-03-23-21-41-47.png)

![](images/2020-03-23-21-43-27.png)
![](images/2020-03-23-21-44-24.png)

## Vanishing Gradient
![](images/2020-03-23-21-45-14.png)
![](images/2020-03-23-21-45-52.png)
![](images/2020-03-23-21-46-09.png)

Batch vs Stochastic Gradient Descent

![](images/2020-03-23-21-49-23.png)
![](images/2020-03-23-21-50-43.png)

# Deep Learning with Pytorch
[Tensors in Pytorch](../../Quiz/m6/1.Tensors-in-PyTorch.pdf)

[Neutral Networks in Pytorch](../../Quiz/m6/2.Neural-Networks-in-PyTorch.pdf)

[Training Neutral Networks](../../Quiz/m6/3.Train-NN.pdf)

[Fashion MNIST](../../Quiz/m6/4.Fashion-MNIST.pdf)

[Inference and Validation](../../Quiz/m6/5-Inference-and-validation.pdf)

[Saving and loading models](../../Quiz/m6/6.Saving-and-loading-modules.pdf)

[Load Image Data](../../Quiz/m6/7.Load-image-data.pdf)

[Transfer Learning](../../Quiz/m6/8.Transfer-learning.pdf)

# Recurrent Neutral Networks
![](images/2020-03-25-12-09-01.png)
![](images/2020-03-25-12-15-22.png)
![](images/2020-03-25-12-12-39.png)
![](images/2020-03-25-12-20-07.png)
![](images/2020-03-25-12-21-17.png)
![](images/2020-03-25-12-22-30.png)
![](images/2020-03-25-12-31-07.png)
![](images/2020-03-25-13-23-21.png)
![](images/2020-03-25-13-23-51.png)